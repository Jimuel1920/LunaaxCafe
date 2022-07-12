from django.db import models
from django.contrib.auth.models import User
from backend.models import Product

# Create your models here.

class Customer(models.Model):
    user =   models.OneToOneField(User, on_delete=models.CASCADE,null=True, blank=True)
    name  =   models.CharField(max_length=200, null=True)
    email =   models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

class order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100, null=True)

    def __str__(self):
        return  str(self.id)

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total
    
    @property
    def shipping(self):
        shipping = False
        orderitems = self.orderitem_set.all()
        for i in orderitems:
            if i.products.digital == False:
                    shipping = True
        return shipping





class orderitem(models.Model):
    products = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    orders =  models.ForeignKey(order, on_delete=models.SET_NULL , null=True, blank=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added= models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.products.pro_price * self.quantity
        return total


class Shippingaddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(order,on_delete=models.SET_NULL, null=True, blank=True)
    address = models.CharField(max_length=200, null=False)
    state= models.CharField(max_length=200, null=False)
    city = models.CharField(max_length=200, null=False)
    zipcode = models.CharField(max_length=200, null=False)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address


    
    