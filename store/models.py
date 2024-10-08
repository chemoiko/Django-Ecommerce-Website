from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True) #this means a user can have only one customer and vice versa
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)


    def __str__(self):
            return self.name

class Product(models.Model):
    name = models.CharField(max_length=200, null=True) 
    price = models.IntegerField()
    digital = models.BooleanField(default=False, null=True, blank=False)
    image = models.ImageField(null=True, blank=True)        #this provide field for u to upload images for a specific product
    
    def __str__(self):
            return self.name

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True) 
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=200, null=True)

    def __str__(self):
          return str(self.id)
    
    @property   #if the product doesnt need shipping, the shipping form wont show up 
    def shipping(self):
        shipping = False
        orderitems = self.orderitem_set.all()
        for i in orderitems:
              if i.product.digital == False:
                   shipping = True
        return shipping
    
    @property
    def get_cart_total(self):        #this is dependent on the total from the orderitem property
         orderitems = self.orderitem_set.all()
         total = sum([item.get_total for item in orderitems])
         return total

    @property
    def get_cart_items(self):      
         orderitems = self.orderitem_set.all()
         total = sum([item.quantity for item in orderitems])
         return total
    
class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL,  null=True) 
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):        #this gives us the total of our order item
         total = self.product.price * self.quantity
         return total

class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True) 
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=200, null=True)
    zipcode = models.CharField(max_length=200, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
          return self.address