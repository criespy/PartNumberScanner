from django import forms
from django.forms import ModelForm, fields, widgets, BaseInlineFormSet
from scanner.models import *
from datetime import date
from django.forms.models import inlineformset_factory
import qrcode

BarangFormset = inlineformset_factory(
    RencanaKirim, RencanaKirimDetail, fields=(['no_line','barang','qty']), labels=({'no_line':'Nomor'}), extra=4, can_delete=True, widgets={
            'no_line' : forms.TextInput({'class':'form-control', 'size':'1','value':'', }),
            'barang' : forms.Select({'class':'form-select select2 col-12', 'style':'width:850px', 'placeholder':'Pilih Barang'}),
            'qty' : forms.TextInput({'class':'form-control', 'size':'1', }),
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
        exclude = ['nomor_sj','status']
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
            'nomor_sj' : forms.TextInput({'class':'form-control', 'pattern':'[0-9]+', 'hidden':'true'}),
            'tanggal' : forms.TextInput({'class':'form-control', 'value':date.today}),
            'jam' : forms.TextInput({'class':'form-control', 'placeholder':'Format: 07:30', 'maxlength':'5'}),
            'cycle' : forms.NumberInput({'class':'form-control', 'placeholder':'1-20', 'maxlength':'2'}),
            'rencanakirimdetails-barang' : forms.Select({'class':'form-control'}),
        }

class FormRencanaKirimDetail(ModelForm):
    class Meta:
        model = RencanaKirimDetail
        fields = ['no_line','barang','qty']
        labels = {'no_line':'Nomor'}

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
            'barcode': forms.TextInput({'class':'form-control'}),
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
