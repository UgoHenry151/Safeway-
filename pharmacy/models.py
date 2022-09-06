from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Drug_type(models.Model):
    name = models.CharField(max_length=150)
    slug= models.SlugField(unique=True, null=False)
    image = models.ImageField(upload_to= 'drug_type', default='drug_type.jpg', blank=True, null=True)
    created= models.DateTimeField(auto_now_add=True)
    updated= models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'drug_type'
        managed = True
        verbose_name = 'Drug_type'
        verbose_name_plural = 'Drug_types' 




class Pharmacy(models.Model):
    drug_type= models.ForeignKey(Drug_type, on_delete=models.CASCADE)
    details= models.TextField()
    product= models.CharField(max_length=150, unique=True, null=False)
    slug= models.SlugField(unique=True, null=False)
    image= models.ImageField(upload_to = 'pharmacy', default= 'pharmacy.jpg', blank=True, null=True)
    min_order = models.IntegerField(default=1)
    max_order = models.IntegerField(default=5)
    price = models.IntegerField()
    malaria= models.BooleanField()
    antibiotics = models.BooleanField()
    c_f_c = models.BooleanField()
    supplements = models.BooleanField()
    overview= models.TextField()
    effect= models.TextField()
    ingredient= models.CharField(max_length=300, blank=True,null=True)
    how_to_use= models.TextField()
    advice= models.TextField()
    display = models.BooleanField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product
    
    class Meta:
        db_table = 'pharmacy'
        managed = True
        verbose_name = 'Pharmacy'
        verbose_name_plural = 'Pharmacys'



class Upload_Prescrip(models.Model):
    fullname = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=50, blank=True, null=True)
    document= models.FileField(upload_to='prescriptions')
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.fullname
    
    class Meta:
        db_table = 'upload_prescrip'
        managed = True
        verbose_name = 'Upload_Prescrip'
        verbose_name_plural = 'Upload_Prescrips'
