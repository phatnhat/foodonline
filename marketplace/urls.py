from django.urls import path
from . import views

urlpatterns = [
    path('', views.marketplace, name="marketplace"),
    path('<slug:vendor_slug>/', views.vendorDetail, name="vendor-detail"),
    path('add-to-cart/<int:food_id>/', views.addToCart, name='add-to-cart'),
    path('decrease-cart/<int:food_id>/', views.decreaseCart, name='decrease-cart'),
    path('delete-cart/<int:cart_id>/', views.deleteCart, name='delete-cart'),
]
