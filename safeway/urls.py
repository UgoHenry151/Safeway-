from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),
    path('profile/', views.profile, name='profile'),
    path('proedit/', views.proedit, name='proedit'),
    path('pharmacy/', views.pharmacy, name='pharmacy'),
]


urlpatterns=[
    path('', views.index, name='index'),
    path('newappoint', views.newappoint, name='newappoint'),
    path('department/', views.department, name='department'),
    path('pricing/', views.pricing, name='pricing'),
    path('checkout_sub/<str:id>', views.checkout_sub, name='checkout_sub'),
    path('checkout_appointment', views.checkout_appointment, name='checkout_appointment'),
    path('paid_subscription/', views.paid_subscription, name='paid_subscription'),
    path('signin/', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),
    path('signup/', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),
    path('proedit/', views.proedit, name='proedit'),
    path('show_notice/<str:id>', views.show_notice, name='show_notice'),
    path('delete_notice/<str:id>', views.delete_notice, name='delete_notice'),
    path('recovery/', views.recovery, name='recovery'),
    path('contact_us/', views.contact_us, name='contact_us'),
    path('pharmacy/', views.pharmacy, name='pharmacy'),
    path('all_drugs/', views.all_drugs, name='all_drugs'),
    path('details/<str:id>/<str:slug>', views.details, name='details'),
    path('searched/', views.searched, name='searched'),
    path('addtocart/', views.addtocart, name='addtocart'),
    path('cart/', views.cart, name='cart'),
    path('upload_prescrip/', views.upload_prescrip, name='upload_prescrip'),
    path('remove_item/', views.remove_item, name='remove_item'),
    path('checkout/', views.checkout, name='checkout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('prescription/', views.prescription, name='prescription'),
    path('remove_prescription/', views.remove_prescription, name='remove_prescription'),
    path('paidorder/', views.paidorder, name='paidorder'),
    path('thankyou/', views.thankyou, name='thankyou'),
]