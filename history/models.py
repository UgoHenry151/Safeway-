from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class MedicalRecord(models.Model):
    medical_by= models.ForeignKey(User, on_delete=models.CASCADE)
    code= models.CharField(max_length=200, blank=True, null=True)
    date= models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    attachment= models.CharField(max_length=200, blank=True, null=True)
    doctor_name= models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to ='medicalrecord', default='medicalrecord.jpg', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.code

    class Meta:
        db_table = 'medicalrecord'
        managed = True
        verbose_name = 'MedicalRecord'
        verbose_name_plural = 'MedicalRecords'





class Billing(models.Model):
    billing_by= models.ForeignKey(User, on_delete=models.CASCADE)
    invoice_no= models.CharField(max_length=200, blank=True, null=True)
    item = models.TextField(blank=True, null=True)
    amount = models.IntegerField()
    paid_on = models.CharField(max_length=200, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.invoice_no

    class Meta:
        db_table = 'billing'
        managed = True
        verbose_name = 'Billing'
        verbose_name_plural = 'Billings'



STATUS=[
    ('New','New'),
    ('Pending','Pending'),
    ('Process','Process'),
    ('closed','Closed')
]

class Appointmenthistory(models.Model):
    appthistory_by= models.ForeignKey(User, on_delete=models.CASCADE)
    services= models.CharField(max_length=200, blank=True, null=True)
    booking_date= models.CharField(max_length=200, blank=True, null=True)
    appt_date= models.CharField(max_length=200, blank=True, null=True)
    follow_up = models.CharField(max_length=200, blank=True, null=True)
    status= models.CharField(max_length=100, choices=STATUS)
    amount = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.services

    class Meta:
        db_table = 'appointmenthistory'
        managed = True
        verbose_name = 'Appointmenthistory'
        verbose_name_plural = 'Appointmenthistorys'
        



class Genaral(models.Model):
    general_by= models.ForeignKey(User, on_delete=models.CASCADE)
    write_ups = models.TextField(blank=True, null=True)
    heart = models.CharField(max_length=50, blank=True, null=True)
    body = models.CharField(max_length=50, blank=True, null=True)
    glucose = models.CharField(max_length=50, blank=True, null=True)
    blood = models.CharField(max_length=50, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.write_ups

    class Meta:
        db_table = 'genaral'
        managed = True
        verbose_name = 'Genaral'
        verbose_name_plural = 'Genarals'
