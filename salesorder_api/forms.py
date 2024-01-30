# sales_order/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Company
from .models import Customer
from .models import Product
from .models import SalesOrder

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'address', 'contact_information']


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'email', 'phone_number', 'address']


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description','unit','price']


class SalesOrderForm(forms.ModelForm):
    class Meta:
        model = SalesOrder
        fields = ['customer', 'total_amount']

    products = forms.ModelChoiceField(queryset=Product.objects.all(), empty_label="(Select Product)")
    quantities = forms.IntegerField(min_value=1, initial=1)
    rates = forms.DecimalField(min_value=0, max_digits=10, decimal_places=2)

    def __init__(self, *args, **kwargs):
        super(SalesOrderForm, self).__init__(*args, **kwargs)
        
OrderItemFormSet = forms.formset_factory(SalesOrderForm, extra=1)