from django.contrib.auth import views as auth_views

from django.contrib import admin
from django.urls import include, path

from salesorder_api import views

urlpatterns = [
    path('register/', views.register, name='register'),  
    path('logout/', views.user_logout, name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    # path('login/', views.login, name='login'),  # URL pattern for login using built-in view

    path('companies/', views.company_list, name='company_list'),
    path('companies/create/', views.company_create, name='company_create'),
    path('companies/<int:pk>/edit/', views.company_edit, name='company_edit'),
    path('companies/<int:pk>/delete/', views.company_delete, name='company_delete'),

    path('customers/', views.customer_list, name='customer_list'),
    path('customers/create/', views.customer_create, name='customer_create'),
    path('customers/<int:pk>/edit/', views.customer_edit, name='customer_edit'),

    path('products/', views.product_list, name='product_list'),
    path('products/create/', views.product_create, name='product_create'),
    path('products/<int:pk>/edit/', views.product_edit, name='product_edit'),

    path('sales_orders/', views.sales_order_list, name='sales_order_list'),
    path('sales_orders/create/', views.sales_order_create, name='sales_order_create'),
    path('sales_orders/<int:pk>/edit/', views.sales_order_edit, name='sales_order_edit'),


]

