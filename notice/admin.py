from django.contrib import admin
from . models import Notice
# Register your models here.


class NoticeAdmin(admin.ModelAdmin):
    list_display = ('id','topic','slug','notification_detail','image','date','created','updated')
    list_display_links= ('id','notice_by','topic','slug')
    prepopulated_fields = {'slug': ('topic',)}

admin.site.register(Notice, NoticeAdmin)