from django.contrib import admin
from . models import *
# Register your models here.

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('id','created_by','firstname','lastname','services','phone_number', 'email', 'apptdate','follow_up','appt_time','price','symptoms', 'notify', 'status','created','updated', 'closed')
    list_display_links= ('id','created_by','firstname')

admin.site.register(Appointment, AppointmentAdmin)




class Subscription_planAdmin(admin.ModelAdmin):
    list_display = ('id','name','slug', 'created', 'updated')
    list_display_links= ('id','name')
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Subscription_plan, Subscription_planAdmin)


class PricingAdmin(admin.ModelAdmin):
    list_display = ('id', 'subscription_plan', 'subscription_price', 'individual', 'family', 'premium','hmo', 'created', 'updated')
    list_display_links= ('id', 'subscription_plan')

admin.site.register(Pricing, PricingAdmin)

class Checkout_SubAdmin(admin.ModelAdmin):
    list_display = ('pricing','ordr_no','itm_paid','price','fullname','date_of_birth','company_name','phone_number','email','country','address','city','state','zip','status','admin_remark')
    list_display_links = ('pricing','ordr_no', 'itm_paid')
    readonly_fields =('pricing','ordr_no','itm_paid','price','fullname','date_of_birth','company_name','phone_number','email','country','address','city','state','zip')

    
admin.site.register(Checkout_Sub, Checkout_SubAdmin)


class Paid_SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('id','user','price','sub_no','payment_code','paid_item','firstname')
    list_display_links = ('id','user','sub_no','paid_item')
    readonly_fields = ('id','user','price','sub_no','payment_code','paid_item','firstname')

admin.site.register(Paid_Subscription, Paid_SubscriptionAdmin)

class Ship_SubAdmin(admin.ModelAdmin):
    list_display = ('id','user','Pricing','things_bought','ordr_no','itm_paid','price','firstname')
    list_disply_links = ('id','user','Pricing')
    redonly_fields = ('id','user','Pricing','ordr_no','itm_paid','price','firstname')

admin.site.register(Ship_Sub, Ship_SubAdmin)