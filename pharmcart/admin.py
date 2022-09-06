from django.contrib import admin
from . models import *

# Register your models here.



class DrugscartAdmin(admin.ModelAdmin):
    list_display = ('user','pharmacy','product_name','quantity','total','order_no','item_paid')
    list_display_links= ('user','pharmacy','product_name','quantity')
    readonly_fields =('user','pharmacy','product_name','quantity','total','order_no','item_paid')

    
admin.site.register(Drugscart, DrugscartAdmin)


class CheckoutAdmin(admin.ModelAdmin):
    list_display = ('drugscart','ordr_no','itm_paid','total','fullname','date_of_birth','company_name','phone_number','email','country','address','city','state','zip','status','admin_remark')
    list_display_links = ('drugscart','ordr_no', 'itm_paid')
    readonly_fields =('drugscart','ordr_no','itm_paid','total','fullname','date_of_birth','company_name','phone_number','email','country','address','city','state','zip')

    
admin.site.register(Checkout, CheckoutAdmin)


class PaidorderAdmin(admin.ModelAdmin):
    list_display = ('id','user','total','cart_no','payment_code','paid_item','firstname')
    list_display_links = ('id','user','cart_no','paid_item')
    readonly_fields = ('id','user','total','cart_no','payment_code','paid_item','firstname')

admin.site.register(Paidorder, PaidorderAdmin)

class ShipAdmin(admin.ModelAdmin):
    list_display = ('id','user','pharmacy','things_bought','total','ordr_no','itm_paid','address','state','firstname','phone')
    list_disply_links = ('id','user','pharmacy')
    redonly_fields = ('id','user','pharmacy','total','ordr_no','itm_paid','address','state','firstname','phone')

admin.site.register(Ship, ShipAdmin)