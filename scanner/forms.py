from django import forms
from django.forms import ModelForm, fields, widgets, BaseInlineFormSet
from scanner.models import *
from django import forms
from datetime import date
from django.forms.models import inlineformset_factory

BarangFormset = inlineformset_factory(
    RencanaKirim, RencanaKirimDetail, fields=(['nomor_line','barang','qty']), extra=1, can_delete=True, widgets={
            'nomor_line' : forms.TextInput({'class':'form-control', 'size':'2','value':''}),
            'rencana_kirim' : forms.Select({'class':'form-control'}),
            'barang' : forms.Select({'class':'form-select'}),
            'description' : forms.TextInput({'class':'form-control'}),
            'qty' : forms.TextInput({'class':'form-control'}),
        }
)

class FormRencanaKirim(ModelForm):
    class Meta:
        model = RencanaKirim
        fields = '__all__'
        exclude = ['status']

        widgets = {
            'nomor_sj' : forms.TextInput({'class':'form-control', 'pattern':'[0-9]+'}),
            'tanggal' : forms.TextInput({'class':'form-control', 'value':date.today}),
            'cycle' : forms.TextInput({'class':'form-control'}),
            'rencanakirimdetails-barang' : forms.Select({'class':'form-control'}),
        }

class FormRencanaKirimDetail(ModelForm):
    class Meta:
        model = RencanaKirimDetail
        fields = ['nomor_line','barang','qty']

        widgets = {
            'nomor_line' : forms.TextInput({'class':'form-control', 'size':'2','value':'1','disabled':'true'}),
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
            'nomor_line' : forms.TextInput({'class':'form-control', 'size':'2','value':'1','disabled':'true'}),
            'rencana_kirim' : forms.Select({'class':'form-control'}),
            'barang' : forms.Select({'class':'form-control'}),
            'description' : forms.TextInput({'class':'form-control'}),
            'qty' : forms.TextInput({'class':'form-control'}),
        }
