from django.db import models

# Create your models here.
# sales_order/models.py
from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    contact_information = models.CharField(max_length=100)

    def __str__(self):
        return self.name
class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    address = models.TextField()

    def __str__(self):
        return self.name
    

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    unit = models.CharField(max_length=5)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    # Add any other fields as needed

    def __str__(self):
        return self.name
    

class SalesOrder(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"Order #{self.id} - {self.customer.name}"
    
class OrderItem(models.Model):
    sales_order = models.ForeignKey(SalesOrder, on_delete=models.CASCADE)
    product = models.CharField(max_length=100)  # Example field, replace with appropriate product field
    quantity = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Item #{self.id} - {self.product} - Qty: {self.quantity} - Price: {self.price}"