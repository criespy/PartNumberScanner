from django import forms
from django.forms import ModelForm, fields, widgets, BaseInlineFormSet
from scanner.models import *
from datetime import date
from django.forms.models import inlineformset_factory
import qrcode

BarangFormset = inlineformset_factory(
    RencanaKirim, RencanaKirimDetail, fields=(['no_line','barang','qty']), extra=1, can_delete=True, widgets={
            'no_line' : forms.TextInput({'class':'form-control', 'size':'1','value':''}),
            'rencana_kirim' : forms.Select({'class':'form-control'}),
            'barang' : forms.Select({'class':'form-select', 'data-live-search':'true'}),
            'description' : forms.TextInput({'class':'form-control'}),
            'qty' : forms.TextInput({'class':'form-control', 'size':'1'}),
        }
)

#Form yang dipakai Update Rencana Kirim
UpdateBarangFormset = inlineformset_factory(
    RencanaKirim, RencanaKirimDetail, fields=(['no_line','barang','qty']), extra=1, can_delete=True, widgets={
            'no_line' : forms.TextInput({'class':'form-control', 'size':'1','value':''}),
            'rencana_kirim' : forms.Select({'class':'form-control'}),
            'barang' : forms.Select({'class':'form-select', 'data-live-search':'true'}),
            'description' : forms.TextInput({'class':'form-control'}),
            'qty' : forms.TextInput({'class':'form-control', 'size':'1'}),
        }
)

class FormRencanaKirim(ModelForm):

    class Meta:
        model = RencanaKirim
        fields = '__all__'
        exclude = ['status']
        labels = {'nomor_sj':'No. Rencana Kirim'}

        widgets = {
            'nomor_sj' : forms.TextInput({'class':'form-control', 'pattern':'[0-9]+'}),
            'tanggal' : forms.TextInput({'class':'form-control', 'value':date.today}),
            'jam' : forms.TextInput({'class':'form-control', 'placeholder':'Format: 07:30', 'maxlength':'5'}),
            'cycle' : forms.NumberInput({'class':'form-control', 'placeholder':'1-20', 'maxlength':'2'}),
            'rencanakirimdetails-barang' : forms.Select({'class':'form-control'}),
        }

class FormRencanaKirimUpdate(ModelForm):

    class Meta:
        model = RencanaKirim
        fields = '__all__'
        exclude = ['status']
        labels = {'nomor_sj':'No. Rencana Kirim'}

        widgets = {
            'nomor_sj' : forms.TextInput({'class':'form-control', 'pattern':'[0-9]+', 'disabled':'disabled'}),
            'tanggal' : forms.TextInput({'class':'form-control', 'value':date.today}),
            'jam' : forms.TextInput({'class':'form-control', 'placeholder':'Format: 07:30', 'maxlength':'5'}),
            'cycle' : forms.NumberInput({'class':'form-control', 'placeholder':'1-20', 'maxlength':'2'}),
            'rencanakirimdetails-barang' : forms.Select({'class':'form-control'}),
        }

class FormRencanaKirimDetail(ModelForm):
    class Meta:
        model = RencanaKirimDetail
        fields = ['no_line','barang','qty']

        widgets = {
            'no_line' : forms.TextInput({'class':'form-control', 'size':'2','value':'1','disabled':'true'}),
            'rencana_kirim' : forms.Select({'class':'form-control'}),
            'barang' : forms.Select({'class':'form-control'}),
            'description' : forms.TextInput({'class':'form-control'}),
            'qty' : forms.TextInput({'class':'form-control'}),
        }

class FormRencanaKirimDetailUpdate(ModelForm):
    class Meta:
        model = RencanaKirimDetail
        fields = '__all__'

        widgets = {
            'no_line' : forms.TextInput({'class':'form-control', 'size':'2','value':'1','disabled':'true'}),
            'rencana_kirim' : forms.Select({'class':'form-control'}),
            'barang' : forms.Select({'class':'form-control'}),
            'description' : forms.TextInput({'class':'form-control'}),
            'qty' : forms.TextInput({'class':'form-control'}),
        }

class FormMasterBarangUpdate(ModelForm):
    class Meta:
        model = Barang
        fields = '__all__'
        labels = {'barcode':'QR Code File'}
        #exclude = ['barcode']

        widgets = {
            'part_number': forms.TextInput({'class':'form-control'}),
            'description': forms.TextInput({'class':'form-control'}),
            'part_number_customer': forms.TextInput({'class':'form-control'}),
            'barcode': forms.HiddenInput({'class':'form-control', 'hidden':'true'}),
            'color_code': forms.TextInput({'class':'form-control'}),
            'position_code': forms.TextInput({'class':'form-control'}),
            'qty_per_box': forms.TextInput({'class':'form-control'}),
        }

class FormMasterBarangCreate(ModelForm):
    class Meta:
        model = Barang
        fields = '__all__'
        labels = {'barcode':'QR Code File'}
        #exclude = ['barcode']

        widgets = {
            'part_number': forms.TextInput({'class':'form-control'}),
            'description': forms.TextInput({'class':'form-control'}),
            'part_number_customer': forms.TextInput({'class':'form-control'}),
            'barcode': forms.TextInput({'class':'form-control'}),
            'color_code': forms.TextInput({'class':'form-control'}),
            'position_code': forms.TextInput({'class':'form-control'}),
            'qty_per_box': forms.TextInput({'class':'form-control'}),
        }

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
        img.save('./scanner/static/images/part_qrcodes/'+data)
