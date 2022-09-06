from django.contrib import admin
from . models import *

# Register your models here.



class MedicalRecordAdmin(admin.ModelAdmin):
    list_display = ('id','medical_by','code','date','description','attachment','doctor_name','image','created','updated')
    list_display_links= ('medical_by','code','date','description')

    
admin.site.register(MedicalRecord, MedicalRecordAdmin)



class BillingAdmin(admin.ModelAdmin):
    list_display = ('id','billing_by','invoice_no','item','amount','paid_on','created','updated')
    list_display_links= ('billing_by','invoice_no','item')

    
admin.site.register(Billing, BillingAdmin)



class AppointmenthistoryAdmin(admin.ModelAdmin):
    list_display = ('appthistory_by','services','booking_date','appt_date','follow_up','status','amount','created','updated')
    list_display_links= ('appthistory_by','services','booking_date')

    
admin.site.register(Appointmenthistory, AppointmenthistoryAdmin)




class GenaralAdmin(admin.ModelAdmin):
    list_display = ('general_by','write_ups','heart','body','glucose','blood','created','updated')
    list_display_links= ('general_by','write_ups','heart')

    
admin.site.register(Genaral, GenaralAdmin)