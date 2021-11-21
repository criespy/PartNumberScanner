from django.urls import path, re_path
from . import views
from .views import BuatRencanaKirim, BuatRencanaKirimDetail

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('delivery/<int:pk>', views.Delivery.as_view(), name='delivery'),
    path('delivery/', views.DeliveryKosong.as_view(), name='delivery'),
    path('print_barcode/<int:pk>', views.PrintBarcode.as_view(), name='print_barcode'),
    re_path(r'^print_barcode/$', views.PrintBarcode.getURL, name='print_barcode2'),
    path('buat_rencana_kirim', views.BuatRencanaKirim.as_view(), name='buat_rencana_kirim'),
    #path('buat_rencana_kirim_a', BuatRencanaKirim.FBuatRencanaKirim),
    path('buat_rencana_kirim_detail', views.BuatRencanaKirimDetail.as_view(), name='buat_rencana_kirim_detail'),
    path('tambah_detail', BuatRencanaKirimDetail.tambah_detail)
]