import io
from django.http import FileResponse, HttpResponse, HttpRequest
from django.template.response import TemplateResponse
from reportlab.pdfgen import canvas
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, UpdateView, CreateView
from .models import Barang, RencanaKirim, RencanaKirimDetail
from .forms import BarangFormset, FormRencanaKirim, FormRencanaKirimUpdate, FormRencanaKirimDetail, FormMasterBarangUpdate, UpdateBarangFormset, FormRencanaKirimDetailUpdate, FormMasterBarangCreate, DeliveryFormset
from  django.contrib.auth.mixins import LoginRequiredMixin
import qrcode
from django.templatetags.static import static
from pathlib import os
from django import forms
from datetime import date, timedelta


class HomePageView(LoginRequiredMixin, ListView):
    login_url = 'auth/login/'
    model = Barang
    template_name = 'home.html'

class Delivery(LoginRequiredMixin, UpdateView):
    model = RencanaKirim
    template_name = 'delivery.html'
    fields = ['status']

    def get_queryset(self):
        id = self.kwargs['pk']
        return RencanaKirim.objects.filter(pk=id)

    #untuk menampilkan item barang di admin backend
    def get_context_data(self, **kwargs):
        detail = super(Delivery, self).get_context_data(**kwargs)
        #detail['form'] = FormRencanaKirimUpdate(self.request.POST, instance=self.object)
        #detail['barang'] = RencanaKirimDetail.objects.all()
        if self.request.POST:
            detail['form'] = FormRencanaKirimUpdate(self.request.POST, instance=self.object)
            detail['konteks'] = DeliveryFormset(self.request.POST, instance=self.object)
        else:
            detail['konteks'] = DeliveryFormset(instance=self.object)
        return detail

    def form_valid(self, form):
        context = self.get_context_data()
        konteks = context["konteks"]
        self.object = form.save()
        if konteks.is_valid():
            konteks.instance = self.object
            konteks.save()
        return super().form_valid(form)

class PrintBarcode(LoginRequiredMixin, DetailView):
    model = Barang
    template_name = 'print_label_produksi.html'

    def getURL(request):
        #bikin variabel buat simpen value dari url
        barang = request.GET.get('item')
        tanggal = request.GET.get('tanggal')
        shift = request.GET.get('shift')
        mesin = request.GET.get('mesin')

        barang = barang.split("#")
        part_number = barang[0]
        part_description = barang[1]
        part_color = barang[2]
        part_position = barang[3]
        part_qty = barang[4]
        tgl = tanggal.split("/")
        lot_produksi = tgl[0][2:4]+"."+tgl[1]+"."+tgl[2]+"."+shift+"."+mesin

        context = {"part_number":part_number, "part_description":part_description, "part_color":part_color, "part_position":part_position, "tanggal":tanggal, "shift":shift, "lot_produksi":lot_produksi, "part_qty": part_qty}
        #return HttpResponse("Berhasil %s" % tanggal)
        #kirim id ke print_barcode.html
        return TemplateResponse(request, 'print_label_produksi.html', context)

class RencanaKirimView(LoginRequiredMixin, ListView):
    model = RencanaKirim
    template_name = 'rencanakirim_listview.html'
    #paginate_by = 10
    queryset = RencanaKirim.objects.filter(status='Open')

    #def get_context_data(self, **kwargs):
    #    context = super(RencanaKirimView, self).get_context_data(**kwargs)
    #    context['tanggal'] = self.queryset. .tanggal
    #    if context['tanggal'] < date.today():
    #        contect['warning'] = "Ya"

class BuatRencanaKirim(LoginRequiredMixin, CreateView):
    model = RencanaKirim
    template_name = 'rencanakirim_createview.html'
    #fields = ['nomor_sj', 'tanggal']
    #diubah dengan settingan form di forms.py
    form_class = FormRencanaKirim

    #buat tampilkan rencana kirim detail
    def get_context_data(self, **kwargs):
        form_class = FormRencanaKirimDetail
        detail = super(BuatRencanaKirim, self).get_context_data(**kwargs)
        detail['konteks'] = RencanaKirimDetail.objects.all()

        if self.request.POST:
            detail["konteks"] = BarangFormset(self.request.POST)
        else:
            detail["konteks"] = BarangFormset()

        return detail

    def form_valid(self, form):
        context = self.get_context_data()
        konteks = context["konteks"]
        self.object = form.save()
        if konteks.is_valid():
            konteks.instance = self.object
            konteks.save()
        return super().form_valid(form)

class UpdateRencanaKirim(LoginRequiredMixin, UpdateView):
    model = RencanaKirim
    template_name = 'rencanakirim_updateview.html'
    form_class = FormRencanaKirimUpdate

    def get_queryset(self):
        id = self.kwargs['pk']
        return RencanaKirim.objects.filter(pk=id)

    def get_context_data(self, **kwargs):
        detail = super(UpdateRencanaKirim, self).get_context_data(**kwargs)
        if self.request.POST:
            detail['form'] = FormRencanaKirimUpdate(self.request.POST, instance=self.object)
            detail['konteks'] = UpdateBarangFormset(
                self.request.POST, instance=self.object)
        else:
            detail['form'] = FormRencanaKirimUpdate(instance=self.object)
            detail['konteks'] = UpdateBarangFormset(instance=self.object)

        return detail

    def form_valid(self, form):
        context = self.get_context_data()
        konteks = context["konteks"]
        self.object = form.save()
        if konteks.is_valid():
            konteks.instance = self.object
            konteks.save()
        return super().form_valid(form)

class BuatRencanaKirimDetail(CreateView):
    model = RencanaKirimDetail
    template_name = 'buat_rencana_kirim_detail.html'
    form_class = FormRencanaKirimDetail

    def tambah_detail(request):
        if request.POST:
            form = FormRencanaKirimDetail(request.POST)
            if form.is_valid():
                form.save()

                
                return(render(request, 'buat_rencana_kirim_detail.html'))
            else:
                
                return(render(request, 'buat_rencana_kirim_detail.html'))

class BuatMasterBarang(LoginRequiredMixin, CreateView):
    model = Barang
    template_name = 'barang_createview.html'
    form_class = FormMasterBarangCreate

    def form_valid(self, form):
        qrcode = form.cleaned_data['part_number']
        self.valid_submission_callback(qrcode)
        return super(BuatMasterBarang, self).form_valid(form)

    def valid_submission_callback(self, data):
        # send an email or other backend call back
        input_data = data
        qr = qrcode.QRCode(
            version=1,
            box_size=5,
            border=2)
        qr.add_data(input_data)
        qr.make(fit=True)
        #img = qr.make_image(fill='black', back_color='white')
        #img.save('.'+static('/images/part_qrcodes/' + data + '.png'))
        img = qr.make_image(fill='black', back_color='white')
        imgfile = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'static/images/part_qrcodes/' + data + '.png')
        img.save((imgfile))

class ListMasterBarang(LoginRequiredMixin, ListView):
    model = Barang
    template_name = 'barang_listview.html'

class UpdateMasterBarang(LoginRequiredMixin, UpdateView):
    model = Barang
    template_name = 'barang_updateview.html'
    form_class = FormMasterBarangUpdate

    def form_valid(self, form):
        qrcode = form.cleaned_data['part_number']
        self.valid_submission_callback(qrcode)
        return super(UpdateMasterBarang, self).form_valid(form)

    def valid_submission_callback(self, data):
        # send an email or other backend call back
        input_data = data
        qr = qrcode.QRCode(
            version=1,
            box_size=5,
            border=2)
        qr.add_data(input_data)
        qr.make(fit=True)
        img = qr.make_image(fill='black', back_color='white')
        imgfile = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'static/images/part_qrcodes/' + data + '.png')
        img.save((imgfile))
        #img.save('.'+static('/images/part_qrcodes/' + data + '.png'))

class MonitoringDelivery(LoginRequiredMixin, TemplateView):
    template_name = "monitoring_delivery.html"

    def jumlahCycle(self):
        cycle = []
        for i in range(10):
            cycle.append(i+1)
        return cycle

    def barangDipilih(self):
        barang = Barang.objects.filter(part_number='HM01-GFQ0100-XL-S0')
        return barang

    def groupingCycle(self):
        q = RencanaKirimDetail.objects.filter(rencana_kirim__cycle='1')# tanggal='2022-11-28')
        return q

    def get_context_data(self, **kwargs):
        context = super(MonitoringDelivery, self).get_context_data(**kwargs)
        context['cycles'] = self.jumlahCycle()
        context['barangs'] = Barang.objects.all()
        context['tanggal'] = date.today() - timedelta(days=1)
        context['barangterpilih'] = self.barangDipilih()
        context['rkd'] = self.groupingCycle()
        return context


def bikinPDF(request):
    # Create a file-like buffer to receive PDF data.
    buffer = io.BytesIO()

    # Create the PDF object, using the buffer as its "file."
    p = canvas.Canvas(buffer)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(100, 100, "Hello world.")

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()

    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='hello.pdf')