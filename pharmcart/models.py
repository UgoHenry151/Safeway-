from django.db import models
from django.contrib.auth.models import User
from pharmacy.models import Pharmacy
# Create your models here.



class Drugscart(models.Model):
    user= models.ForeignKey(User, on_delete= models.CASCADE)
    pharmacy= models.ForeignKey(Pharmacy, on_delete=models.CASCADE)
    quantity= models.IntegerField()
    product_name= models.CharField(max_length=100)
    total = models.IntegerField(default=1)
    order_no= models.CharField(max_length=50)
    item_paid = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

    class Meta:
        db_table = 'drugscart'
        managed = True
        verbose_name = 'Drugscart'
        verbose_name_plural = 'Drugscarts'


STATUS = [
    ('New','New'),
    ('Pending','Pending'),
    ('Processing','Processing'),
    ('Shipping','Shipping'),
    ('Delivered','Delivered'),
]

class Checkout(models.Model):
    drugscart= models.ForeignKey(Drugscart,on_delete=models.CASCADE)
    ordr_no= models.CharField(max_length=50)
    itm_paid= models.BooleanField(default=False)
    total= models.FloatField()
    fullname= models.CharField(max_length=150,blank=True, null=True,)
    date_of_birth = models.CharField(max_length=250,blank=True, null=True)
    company_name = models.CharField(max_length=250,blank=True, null=True)
    phone_number = models.CharField(max_length=100)
    email= models.EmailField(max_length=100)
    country= models.CharField(max_length=100,blank=True, null=True)
    address= models.CharField(max_length=100,blank=True, null=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50,blank=True, null=True)
    zip = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length = 50, choices=STATUS)
    admin_remark= models.CharField(max_length=250)

    def __str__(self):
        return self.drugscart.user.username
    
    class Meta:
        db_table = 'checkout'
        managed = True
        verbose_name = 'Checkout'
        verbose_name_plural = 'Checkouts'
    

class Paidorder(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    total = models.FloatField()
    cart_no = models.CharField(max_length=36, blank=True, null=True)
    payment_code = models.CharField(max_length=50)
    paid_item = models.BooleanField(default=False)
    firstname= models.CharField(max_length=50)


    def __str__(self):
        return self.user.username

    class Meta:
        db_table = 'paidorder'
        managed = True
        verbose_name = 'Paidorder'
        verbose_name_plural = 'Paidorders'
    

class Ship(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    pharmacy= models.ForeignKey(Pharmacy, on_delete=models.CASCADE,blank=True, null=True)
    ordr_no= models.CharField(max_length=50)
    things_bought= models.CharField(max_length=500, blank=True, null=True)
    itm_paid= models.BooleanField(default=False)
    phone= models.IntegerField(blank=True, null=True)
    total= models.FloatField()
    address= models.CharField(max_length=50,blank=True, null=True)
    state= models.CharField(max_length=50,blank=True, null=True)
    firstname= models.CharField(max_length=200,blank=True, null=True)

    def __str__(self):
        return self.user.username