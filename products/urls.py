from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('management/', views.product_management, name='product_management'),
    path('add/', views.add_item, name='add_item'),
    path('edit/<product_id>/', views.edit_item, name='edit_item'),
    path('delete/<product_id>/', views.delete_item, name='delete_item'),
]

