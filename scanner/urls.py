from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('delivery', views.Delivery.as_view(), name='delivery'),
    path('print_barcode/<int:pk>', views.PrintBarcode.as_view(), name='print_barcode'),
    re_path(r'^print_barcode/$', views.PrintBarcode.getURL, name='print_barcode2'),
]