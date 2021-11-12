from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('delivery', views.Delivery.as_view(), name='delivery'),
    path('print_barcode/', views.bikinPDF, name='print_barcode'),
]