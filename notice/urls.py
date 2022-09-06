from django.conf.urls import patterns, url

urlpatterns = patterns('notice.views', 
url(r'^show/(?P<notice_id>\d+)/$', 'show_notice'), 
url(r'^delete/(?P<notice_id>\d+)/$', 'delete_notice'),

)