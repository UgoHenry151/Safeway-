from django.contrib import admin
from . models import *


# Register your models here.

class Contact_usAdmin(admin.ModelAdmin):
    list_display = ('fullname','email','phone_number','message','created','status','closed')
    list_display_links= ('fullname','message','status')
    readonly_fields =('fullname','email','phone_number','message','created','status','closed')

admin.site.register(Contact_us, Contact_usAdmin)


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id','user','fullname','first_name','last_name','email','phone_number','date_of_birth','address','marital_status','sex','patient_weight','patient_height','blood_group','city','state','zip','history','image','medication','disease','period','family','details','records')
    list_display_links = ('id','user','fullname','email','phone_number','blood_group','records')
    # readonly_fields = ('id','user','fullname','first_name','last_name','email','phone_number','date_of_birth','address','marital_status','sex','patient_weight','patient_height','blood_group','city','state','zip','history','medication','disease','period','family','details','records')

admin.site.register(Profile, ProfileAdmin)


class PrescriptionAdmin(admin.ModelAdmin):
    list_display = ('id','user','prescrip_code','title','name_of_doc','image','created','disease','content','updated')
    list_display_links = ('id','user','prescrip_code')
    
admin.site.register(Prescription, PrescriptionAdmin)



