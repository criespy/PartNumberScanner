from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('delivery/<int:pk>', views.Delivery.as_view(), name='delivery'),
    path('delivery/', views.RencanaKirimView.as_view(), name='delivery'),
    path('print_barcode/<int:pk>', views.PrintBarcode.as_view(), name='print_barcode'),
    re_path(r'^print_barcode/$', views.PrintBarcode.getURL, name='print_barcode2'),
    path('buat_rencana_kirim', views.BuatRencanaKirim.as_view(), name='buat_rencana_kirim'),
    #path('buat_rencana_kirim_a', BuatRencanaKirim.FBuatRencanaKirim),
    path('buat_rencana_kirim_detail', views.BuatRencanaKirimDetail.as_view(), name='buat_rencana_kirim_detail'),
    #path('tambah_detail', BuatRencanaKirimDetail.tambah_detail),
    path('rencana_kirim', views.RencanaKirimView.as_view(), name='view_rencana_kirim'),
    path('update_rencana_kirim/<int:pk>', views.UpdateRencanaKirim.as_view(), name='update_rencana_kirim'),
    path('update_rencana_kirim/', views.UpdateRencanaKirim.as_view(), name='update_rencana_kirim'),
    path('buat_master_barang', views.BuatMasterBarang.as_view(), name='buat_master_barang'),
    path('list_barang', views.ListMasterBarang.as_view(), name='list_barang'),
    path('edit_master_barang/<int:pk>', views.UpdateMasterBarang.as_view(), name='edit_master_barang'),
    path('print_label_produksi', views.HomePageView.as_view(), name='print_label_produksi'),
    path('delivery/monitoring', views.MonitoringDelivery.as_view(), name='monitoring_delivery'),
]