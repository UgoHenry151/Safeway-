from django.db import models
from django.contrib.auth.models import User

# Create your models here.

STATUS=[
    ('New','New'),
    ('Pending','Pending'),
    ('Process','Process'),
    ('closed','Closed')
]

class Appointment(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    firstname= models.CharField(max_length=50,blank=True, null=True)
    lastname= models.CharField(max_length=50,blank=True, null=True)
    services= models.CharField(max_length=100,blank=True, null=True)
    phone_number= models.CharField(max_length=100, blank=True, null=True)
    apptdate= models.CharField(max_length=200,blank=True, null=True)
    follow_up= models.CharField(max_length=200,blank=True, null=True)
    appt_time = models.CharField(max_length=100,blank=True, null=True)
    email= models.EmailField(max_length=100,blank=True, null=True)
    notify= models.BooleanField(blank=True, null=True)
    symptoms= models.TextField(blank=True, null=True)
    price = models.FloatField(max_length=2, default=10)
    status= models.CharField(max_length=100, choices=STATUS, default='new')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    closed= models.DateTimeField(blank=True, null=True)
    

    def __str__(self):
        return self.created_by.username

    class Meta:
        db_table = 'appointment'
        managed = True
        verbose_name = 'Appointment'
        verbose_name_plural = 'Appointments'


class Subscription_plan(models.Model):
    name = models.CharField(max_length=150)
    slug= models.SlugField(unique=True, null=False)
    created= models.DateTimeField(auto_now_add=True)
    updated= models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'subscription_plan'
        managed = True
        verbose_name = 'Subscription_plan'
        verbose_name_plural = 'Subscription_plans'


class Pricing(models.Model):
    # user= models.ForeignKey(User, on_delete=models.CASCADE)
    subscription_plan= models.ForeignKey(Subscription_plan, on_delete=models.CASCADE)
    subscription_price = models.IntegerField()
    individual= models.BooleanField()
    family= models.BooleanField()
    premium= models.BooleanField()
    hmo= models.BooleanField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subscription_plan.name

    class Meta:
        db_table = 'pricing'
        managed = True
        verbose_name = 'Pricing'
        verbose_name_plural = 'Pricings'

    'user', 'subscription_plan', 'subscription_price', 'individual', 'family', 'premium','hmo', 'created', 'updated'


STATUS = [
    ('New','New'),
    ('Pending','Pending'),
    ('Processing','Processing'),
    ('Shipping','Shipping'),
    ('Delivered','Delivered'),
]

class Checkout_Sub(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    pricing= models.ForeignKey(Pricing, on_delete=models.CASCADE)
    ordr_no= models.CharField(max_length=50)
    itm_paid= models.BooleanField(default=False)
    price= models.FloatField()
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
        return self.user.username
    
    class Meta:
        db_table = 'checkout_sub'
        managed = True
        verbose_name = 'Checkout_Sub'
        verbose_name_plural = 'Checkout_Subs'


class Paid_Subscription(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.FloatField()
    sub_no = models.CharField(max_length=36, blank=True, null=True)
    payment_code = models.CharField(max_length=50)
    paid_item = models.BooleanField(default=False)
    firstname= models.CharField(max_length=50)


    def __str__(self):
        return self.user.username

    class Meta:
        db_table = 'paid_subscription'
        managed = True
        verbose_name = 'Paid_Subscription'
        verbose_name_plural = 'Paid_Subscriptions'
    

class Ship_Sub(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    Pricing= models.ForeignKey(Pricing, on_delete=models.CASCADE,blank=True, null=True)
    ordr_no= models.CharField(max_length=50)
    things_bought= models.CharField(max_length=300, blank=True, null= True)   
    itm_paid= models.BooleanField(default=False)
    price= models.FloatField()
    firstname= models.CharField(max_length=200,blank=True, null=True)

    def __str__(self):
        return self.user.username
    

    class Meta:
        db_table = 'ship_sub'
        managed = True
        verbose_name = 'Ship_Sub'
        verbose_name_plural = 'Ship_Subs'