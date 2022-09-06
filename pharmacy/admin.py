from django.contrib import admin
from . models import *
# Register your models here.

class Drug_typeAdmin(admin.ModelAdmin):
    list_display = ('id','name','slug','image','created','updated')
    list_display_links= ('id','name','slug')
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Drug_type, Drug_typeAdmin)



class PharmacyAdmin(admin.ModelAdmin):
    list_display = ('id', 'drug_type', 'slug', 'product', 'image', 'details', 'min_order', 'max_order', 'price', 'display', 'created', 'updated')
    list_display_links= ('id', 'drug_type','product', 'slug')
    prepopulated_fields = {'slug': ('product',)}
    list_editable= ['display','price']

admin.site.register(Pharmacy, PharmacyAdmin)


class Upload_PrescripAdmin(admin.ModelAdmin):
    list_display = ('id', 'fullname', 'email', 'phone', 'document', 'message','created', 'updated')
    list_display_links= ('id', 'fullname')

admin.site.register(Upload_Prescrip, Upload_PrescripAdmin)