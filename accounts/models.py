from django.contrib.auth.models import User
from django.db import models
from django.db.models.deletion import CASCADE


class Customer (models.Model):

    user =models.OneToOneField(User, null=True,blank=True, on_delete=CASCADE)
    name = models.CharField(max_length=200, null=True,blank=True)
    email = models.CharField(max_length=200, null=True,blank=True)
    phone = models.CharField(max_length=200, null=True,blank=True)
    date_created = models.DateTimeField(auto_now_add=True,blank=True)
    profile_pic = models.ImageField( default="profile1.jpg", null=True, blank=True)


    def __str__(self):
        return str(self.name)

      
class Tag (models.Model):

    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name
        
class Product(models.Model):

    CATEGORY = (
            ('Indoor', 'Indoor'),
            ('Out Door', 'Out Door'),
            )

    name = models.CharField(max_length=200, null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    description=models.CharField(max_length=200, null=True, blank=True)
    date_created=models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name
        


class Order (models.Model):
    STATUS=(
            ('Pending', 'Pending'),
            ('Out for delivery', 'Out for delivery'),
            ('Delivered', 'Delivered'),
            )

    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    date_created=models.DateTimeField(auto_now_add=True, null=True)
    status=models.CharField(max_length=200, null=True, choices=STATUS)
   
    def __str__(self):
        return self.product.name