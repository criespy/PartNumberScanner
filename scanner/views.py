import io
from django.http import FileResponse, HttpResponse, HttpRequest
from django.template.response import TemplateResponse
from reportlab.pdfgen import canvas
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, UpdateView, CreateView
from .models import Barang, RencanaKirim, RencanaKirimDetail
from .forms import BarangFormset, FormRencanaKirim, FormRencanaKirimDetail, FormMasterBarang
from  django.contrib.auth.mixins import LoginRequiredMixin
from django import forms
from datetime import date


class HomePageView(LoginRequiredMixin, ListView):
    login_url = 'auth/login/'
    #redirect_field_name = 'redirect_to'
    model = Barang
    template_name = 'home.html'

class Delivery(UpdateView):
    model = RencanaKirim
    template_name = 'delivery.html'
    fields = ['nomor_sj', 'status']

    #untuk menampilkan item barang di admin backend
    def get_context_data(self, **kwargs):
        detail = super(Delivery, self).get_context_data(**kwargs)
        detail['barang'] = RencanaKirimDetail.objects.all()
        return detail

class DeliveryKosong(TemplateView):
    template_name = 'delivery.html'

class PrintBarcode(DetailView):
    model = Barang
    template_name = 'print_label_produksi.html' #'print_barcode.html'

    def getURL(request):
        #bikin variabel buat simpen value dari url
        barang = request.GET.get('item')
        tanggal = request.GET.get('tanggal')
        shift = request.GET.get('shift')
        mesin = request.GET.get('mesin')

        barang = barang.split("#")
        part_number = barang[0]
        part_description = barang[1]
        tgl = tanggal.split("/")
        lot_produksi = tgl[0][2:4]+"."+tgl[1]+"."+tgl[2]+"."+shift+"."+mesin

        context = {"part_number":part_number, "part_description":part_description, "tanggal":tanggal, "shift":shift, "lot_produksi":lot_produksi}
        #return HttpResponse("Berhasil %s" % tanggal)
        #kirim id ke print_barcode.html
        return TemplateResponse(request, 'print_label_produksi.html', context)

class RencanaKirimView(ListView):
    model = RencanaKirim
    template_name = 'view_rencana_kirim.html'

class ScanBarcode(DetailView):
    model = RencanaKirim
    template_name = 'scan_barcode.html'

class BuatRencanaKirim(CreateView):
    model = RencanaKirim
    template_name = 'buat_rencana_kirim.html'
    #fields = ['nomor_sj', 'tanggal']
    #diubah dengan settingan form di forms.py
    form_class = FormRencanaKirim

    #def ini akan dihilangkan, hanya untuk test pembanding dengan class-based
    #def FBuatRencanaKirim(request):
    #    form = FormRencanaKirim
    #    konteks = {
    #        'form': form,
    #    }
    #    return render(request, 'buat_rencana_kirim.html', konteks)

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

class BuatRencanaKirimB():
    def tambahRencanaKirim():
        return(render(request, 'buat_rencana_kirim_detail.html'))

class BuatMasterBarang(CreateView):
    model = Barang
    template_name = 'buat_master_barang.html'
    form_class = FormMasterBarang

class ListMasterBarang(ListView):
    model = Barang
    template_name = 'master_barang.html'

class EditMasterBarang(UpdateView):
    model = Barang
    template_name = 'update_master_barang.html'
    form_class = FormMasterBarang


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