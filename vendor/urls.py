from django.urls import path, include
from . import views
from accounts import views as AccountViews

urlpatterns = [
    path('', AccountViews.vendorDashboard, name='vendor'),
    path('profile/', views.vprofile, name='vprofile'),
    path('menu-builder/', views.menuBuilder, name='menu-builder'),
    path('menu-builder/category/<int:pk>/', views.fooditemsByCategory, name='fooditems-by-category'),

    path('menu-builder/category/add/', views.addCategory, name="add-category"),
    path('menu-builder/category/edit/<int:pk>', views.editCategory, name="edit-category"),
    path('menu-builder/category/delete/<int:pk>', views.deleteCategory, name="delete-category"),

    path('menu-builder/food/add/', views.addFood, name="add-food"),
    path('menu-builder/food/edit/<int:pk>', views.editFood, name="edit-food"),
    path('menu-builder/food/delete/<int:pk>', views.deleteFood, name="delete-food"),
]
