from django import forms
from django.forms import ModelForm, fields, widgets, BaseInlineFormSet, BaseModelFormSet
from scanner.models import *
from datetime import date
from django.forms.models import inlineformset_factory
import qrcode

#class BaseBarangFormSet(BaseModelFormSet):
#    def __init__(self, *args, **kwargs):
#        super().__init__(*args, **kwargs)
#        self.queryset = RencanaKirimDetail.objects.filter(barang__status="Disabled")

class CreateRencanaKirimForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['barang'].queryset = Barang.objects.filter(status="Aktif")


BarangFormset = inlineformset_factory(
    RencanaKirim, RencanaKirimDetail, form=CreateRencanaKirimForm, fields=(['no_line','barang','qty']), labels=({'no_line':'Nomor'}), extra=4, can_delete=True, widgets={
            'no_line' : forms.TextInput({'class':'form-control', 'size':'1','value':'', }),
            'barang' : forms.Select({'class':'form-select select2 col-12', 'style':'width:850px'}),
            'qty' : forms.TextInput({'class':'form-control', 'size':'1', }),
        }
)
#statusbarang = RencanaKirimDetail.objects.get(barang.status=="Disabled")
#AktifBarangFormset = BarangFormset(instance=statusbarang)



#Form yang dipakai Update Rencana Kirim
UpdateBarangFormset = inlineformset_factory(
    RencanaKirim, RencanaKirimDetail, form=CreateRencanaKirimForm, fields=(['no_line','barang','qty']), labels=({'no_line':'Nomor'}), extra=1, can_delete=True, widgets={
            'no_line' : forms.TextInput({'class':'form-control', 'size':'1','value':''}),
            'barang' : forms.Select({'class':'form-select select2 col-12', 'style':'width:850px'}),
            'qty' : forms.TextInput({'class':'form-control', 'size':'1'}),
        }
)

#Form untuk Delivery Scan
DeliveryFormset = inlineformset_factory(
    RencanaKirim, RencanaKirimDetail, fields=(['no_line','barang','qty','box_scanned', 'pcs_scanned']), extra=0, can_delete=False, widgets={
        'no_line' : forms.TextInput({'class':'form-control', 'size':'1','value':''}),
        'barang' : forms.TextInput({'class':'form-control', 'readonly':'readonly'}),
        'qty' : forms.TextInput({'class':'form-control', 'size':'1'}),
        'additional1' : forms.TextInput({'class':'form-control', 'size':'1'}),
        'box_scanned': forms.TextInput({'class':'form-control', 'size':'1'}),
        'pcs_scanned': forms.TextInput({'class':'form-control', 'size':'1'}),
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
        exclude = ['nomor_sj','status']
        labels = {'nomor_sj':'No. Rencana Kirim'}

        widgets = {
            'nomor_sj' : forms.TextInput({'class':'form-control', 'pattern':'[0-9]+', 'hidden':'true'}),
            'tanggal' : forms.TextInput({'class':'form-control', 'value':date.today}),
            'jam' : forms.TextInput({'class':'form-control', 'placeholder':'Format: 07:30', 'maxlength':'5'}),
            'cycle' : forms.NumberInput({'class':'form-control', 'placeholder':'1-20', 'maxlength':'2'}),
            'rencanakirimdetails-barang' : forms.Select({'class':'form-control'}),
        }

class FormRencanaKirimDetail(ModelForm):

    #def __init__(self, *args, barang__status, **kwargs):
    #    self.status = barang__status
    #    super().__init__(*args, **kwargs)
    #    self.fields['barang'].queryset = RencanaKirimDetail.objects.filter(status="Disabled")

    class Meta:
        model = RencanaKirimDetail
        fields = ['no_line','barang','qty']
        labels = {'no_line':'Nomor'}

        #form.barang.queryset = RencanaKirimDetail.objects.filter(barang__status='Disabled')

        widgets = {
            'no_line' : forms.TextInput({'class':'form-control', 'size':'2','value':'1','disabled':'true'}),
            'rencana_kirim' : forms.Select({'class':'form-control'}),
            #'barang' : forms.Select({'class':'form-control'}),
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
        fields = ['part_number', 'description', 'part_number_customer', 'barcode', 'position_code', 'color_code', 'qty_per_box', 'status']
        labels = {'barcode':'QR Code File', 'color_code':'Child Code', 'position_code':'Parent Code'}
        #exclude = ['barcode']

        widgets = {
            'part_number': forms.TextInput({'class':'form-control'}),
            'description': forms.TextInput({'class':'form-control'}),
            'part_number_customer': forms.TextInput({'class':'form-control'}),
            'barcode': forms.TextInput({'class':'form-control'}),
            'color_code': forms.TextInput({'class':'form-control'}),
            'position_code': forms.TextInput({'class':'form-control'}),
            'qty_per_box': forms.TextInput({'class':'form-control'}),
            'status': forms.Select({'class':'form-control'}),
        }

class FormMasterBarangCreate(ModelForm):
    class Meta:
        model = Barang
        fields = ['part_number', 'description', 'part_number_customer', 'barcode', 'position_code', 'color_code', 'qty_per_box']
        labels = {'barcode':'QR Code File', 'color_code':'Child Code', 'position_code':'Parent Code'}
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
