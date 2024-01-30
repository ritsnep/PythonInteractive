from imaplib import _Authenticator
from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from .models import Company, Customer, SalesOrder
from .forms import CompanyForm
from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.contrib.auth import logout  
from .forms import CustomerForm
from .models import Product
from .forms import ProductForm
from .forms import SalesOrderForm, OrderItemFormSet
from .models import OrderItem


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login page after successful registration
    else:
        form = UserRegistrationForm()
    return render(request, 'salesorder/register.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')  # Redirect to the login page after logout


def company_list(request):
    companies = Company.objects.all()
    return render(request, 'salesorder/company_list.html', {'companies': companies})

def company_create(request):
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('company_list')
    else:
        form = CompanyForm()
    return render(request, 'salesorder/company_form.html', {'form': form})

def company_edit(request, pk):
    company = get_object_or_404(Company, pk=pk)
    if request.method == 'POST':
        form = CompanyForm(request.POST, instance=company)
        if form.is_valid():
            form.save()
            return redirect('company_list')
    else:
        form = CompanyForm(instance=company)
    return render(request, 'salesorder/company_form.html', {'form': form})

def company_delete(request, pk):
    company = get_object_or_404(Company, pk=pk)
    if request.method == 'POST':
        if request.POST.get('confirm_delete') == 'yes':  # Check if user confirmed deletion
            company.delete()
            return redirect('company_list')
    return render(request, 'salesorder/company_confirm_delete.html', {'company': company})



def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'salesorder/customer_list.html', {'customers': customers})

def customer_create(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer_list')
    else:
        form = CustomerForm()
    return render(request, 'salesorder/customer_form.html', {'form': form})

def customer_edit(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('customer_list')
    else:
        form = CustomerForm(instance=customer)
    return render(request, 'salesorder/customer_form.html', {'form': form})

def product_list(request):
    products = Product.objects.all()
    return render(request, 'salesorder/product_list.html', {'products': products})

def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'salesorder/product_form.html', {'form': form})

def product_edit(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'salesorder/product_form.html', {'form': form})

def sales_order_create(request):
    if request.method == 'POST':
        form = SalesOrderForm(request.POST)
        formset = OrderItemFormSet(request.POST)
        if form.is_valid() and formset.is_valid():
            sales_order = form.save(commit=False)
            sales_order.save()  # Save the sales order to the database

            for item_form in formset:
                item = item_form.save(commit=False)
                item.sales_order = sales_order
                item.save()  # Save each order item to the database

            return redirect('sales_order_list')  # Redirect to the list page after successful submission
    else:
        form = SalesOrderForm()
        formset = OrderItemFormSet()
    return render(request, 'salesorder/sales_order_form.html', {'form': form, 'formset': formset})

def sales_order_list(request):
    orders = SalesOrder.objects.all()
    return render(request, 'salesorder/sales_order_list.html', {'orders': orders})

def sales_order_edit(request, pk):
    sales_order = get_object_or_404(SalesOrder, pk=pk)
    if request.method == 'POST':
        form = SalesOrderForm(request.POST, instance=sales_order)
        if form.is_valid():
            form.save()
            return redirect('sales_order_list')
    else:
        form = SalesOrderForm(instance=sales_order)
    return render(request, 'salesorder/sales_order_form.html', {'form': form})