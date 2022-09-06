from django.db import models
from django.contrib.auth.models import User
# Create your models here.




STATUS=[
    ('New','New'),
    ('Pending','Pending'),
    ('Process','Process'),
    ('closed','Closed')
]

class Contact_us(models.Model):
    fullname= models.CharField(max_length=250, blank=True, null=True)
    email= models.EmailField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(max_length=100, blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    created= models.DateTimeField(auto_now_add=True)
    status= models.CharField(max_length=100, choices=STATUS, default='new')
    closed= models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.fullname

    class Meta:
        db_table = 'contact-us'
        managed = True
        verbose_name = 'Contact-us'
        verbose_name_plural = 'Contact-us'




class Profile(models.Model):
    user= models.OneToOneField(User,  on_delete=models.CASCADE)
    fullname= models.CharField(max_length=150,blank=True, null=True,)
    first_name= models.CharField(max_length=100,blank=True, null=True, default='name')
    last_name= models.CharField(max_length=100,blank=True, null=True, default='name')
    email= models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=100)
    date_of_birth = models.CharField(max_length=250,blank=True, null=True)
    address= models.CharField(max_length=100,blank=True, null=True,)
    marital_status= models.CharField(max_length=10,blank=True, null=True)
    sex= models.CharField(max_length=10,blank=True, null=True)
    patient_weight = models.CharField(max_length=50,blank=True, null=True)
    patient_height= models.CharField(max_length=50,blank=True, null=True)
    blood_group= models.CharField(max_length=10)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50,blank=True, null=True)
    zip = models.CharField(max_length=50,blank=True, null=True)
    history= models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to ='profile', default='profile.jpg', blank=True, null=True)
    medication= models.BooleanField(blank=True, null=True)
    disease= models.CharField(max_length=100,blank=True, null=True)
    period= models.CharField(max_length=50,blank=True, null=True)
    family= models.CharField(max_length=50,blank=True, null=True)
    details= models.CharField(max_length=100,blank=True, null=True)
    records = models.BooleanField(blank=True, null=True)

    def __str__(self):
        return self.user.username
    
    class Meta:
        db_table = 'profile'
        managed = True
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'


class Prescription(models.Model):
    user = models.OneToOneField(User,  on_delete=models.CASCADE)
    # profile =models.ForeignKey(Profile, on_delete=models.CASCADE)
    prescrip_code = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    name_of_doc = models.CharField(max_length=50)
    image = models.ImageField(upload_to ='prescription', default='prescription.jpg', blank=True, null=True)
    created= models.DateTimeField(auto_now_add=True)
    disease = models.CharField(max_length=100)
    content = models.CharField(max_length=50)
    updated= models.DateTimeField(auto_now=True)