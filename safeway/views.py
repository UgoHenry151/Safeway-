import email
import uuid
import requests
import json


from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.core.paginator import Paginator
from django.conf import settings
from django.core.mail import EmailMessage
from hospital.settings import EMAIL_HOST_USER


from safeway.forms import *
from userprofile.models import *
from pharmacy.models import *
from notice.models import *
from .models import *
from pharmcart.models import *
from history.models import *

# Create your views here.
def index(request):
    return render(request, "henry.html")


def newappoint(request):
    apptform = AppointmentForm()
    if request.method == 'POST':
        # appty = Appointment.objects.filter(created_by__username = request.user.username)
        apptform = AppointmentForm(request.POST)
        if apptform.is_valid():
            newapoint = apptform.save(commit=False)
            newapoint.created_by = request.user
            newapoint.save()
            messages.success(request, 'Please check your notification in your profile once the payment is made. Appointments could be Approved, Cancelled or Shifted to appropriates date')
            return redirect ('checkout_appointment')
        else:
            messages.error(request, apptform.errors)
            return redirect ('newappoint')
        
    context={
        'apptform':apptform,
    }
    return render(request, 'newappoint.html', context)


def department(request):
    return render(request, 'department.html')


def pricing(request):
    individual = Pricing.objects.filter(individual=True)
    family = Pricing.objects.filter(family=True)
    premium = Pricing.objects.filter(premium=True)
    hmo = Pricing.objects.filter(hmo=True)
    sub_plan = Subscription_plan.objects.all()


    context={
        'individual':individual,
        'family':family,
        'premium':premium,
        'hmo':hmo,
        'sub_plan':sub_plan,
    }

    return render(request, 'pricing.html', context)


def checkout_sub(request, id):
    pricy= Pricing.objects.filter(subscription_plan_id = id)
    profile= Profile.objects.get(user__username= request.user.username)

    subscription_price=0
    vat=0
    price=0

    for item in pricy:
        if item:
            subscription_price +=subscription_price + item.subscription_price
    

    vat = 0.075 * subscription_price
    price= subscription_price + vat



    context ={
        'pricy':pricy,
        'subscription_price':subscription_price,
        'vat':vat,
        'price':price,
        'profile':profile
    }

    return render (request, 'checkout_sub.html', context)      


def checkout_appointment(request):
    profile= Profile.objects.get(user__username= request.user.username)
    appointy= Appointment.objects.filter(created_by__username = request.user.username).first()
    ship = Ship_Sub.objects.filter(user__username = request.user.username)

    vat=0
    price=0
    # for item in appointy:
    appt_price = appointy.price


    vat = 0.075 * appt_price
    price= appt_price + vat

    context ={
        'appointy':appointy,
        'appt_price':appt_price,
        'ship': ship,
        'vat':vat,
        'price':price,
        'profile':profile
    }

    return render (request, 'checkout_appointment.html', context)  



def paid_subscription(request):
    if request.method == 'POST':
        # api_key= 'sk_test_371cb1fe66df8f063548bf77f615d1a8c2411f24'
        # curl= 'https://api.paystack.co/transaction/initialize'
        # cburl = 'http://127.0.0.1:2000/thankyou/'
        ref_num = str(uuid.uuid4())
        
        price = float(request.POST['get_price'])*100
    
        prices = float(request.POST['get_appt_price'])*100

        plan =  request.POST['get_appt_plan']

        plan_appt =  request.POST['get_plan']
        phone =  request.POST['phone_number']
        
        cartup = Profile.objects.get(user__username = request.user.username)
        order_num = cartup.id
        user= User.objects.get(username= request.user.username)
        email = user.email
        first_name = user.first_name
        last_name = user.last_name
        # name of the product purchased
        # pricy= Pricing.objects.filter(subscription_plan_id= id)
        # prisy= pricy.id
        # appointy= Appointment.objects.filter(created_by = request.user)

        headers= {'Authorization': f'Bearer {api_key}'}
        data = {'reference':ref_num, 'order_number':order_num, 'amount': int(price), 'amount': int(prices), 'callback_url': cburl, 'email':email, 'currency':'NGN'}


        try:
            r = requests.post(curl, headers=headers, json=data)
        except Exception:
            messages.error(request, 'Please refresh and try again, issue being resolved')
        else:
            transback = json.loads(r.text)
            rd_url = transback['data']['authorization_url']


            paid_subscription = Paid_Subscription()
            paid_subscription.user = user
            paid_subscription.price = price/100 or prices/100
            paid_subscription.sub_no = order_num
            paid_subscription.payment_code = ref_num
            paid_subscription.paid_item =True
            paid_subscription.firstname = user.first_name
            # paid_subscription.name_on_crd = user.first_name and user.last_name
            paid_subscription.save()


            ship_sub =Ship_Sub()
            ship_sub.user = user
            ship_sub.things_bought = plan or plan_appt
            ship_sub.price = price/100 or prices/100
            ship_sub.ordr_no = order_num
            ship_sub.itm_paid =True
            ship_sub.firstname = user.first_name
            ship_sub.save()

            email = EmailMessage(
                'New Transaction alert !', #subject
                f'Admin, a client {first_name} {last_name}, with the phone number {phone} has just completed a transaction. \n kindly follow up on his transaction.', #message
                settings.EMAIL_HOST_USER, #HOST EMAIL
                ['mdpeter28@gmail.com'] #sender
            )
            email.fail_silently = True
            email.send()

            return redirect(rd_url)

        return redirect('index')


def signup(request):
    form = SignupForm()
    if request.method == 'POST':
        phone_number = request.POST['phone_number']
        image = request.POST['image']
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            newuser = Profile(user = user)
            newuser.first_name= user.first_name
            newuser.last_name= user.last_name
            newuser.phone_number = phone_number
            newuser.image = image
            newuser.email = user.email
            newuser.save()
            newappoint = Appointment(created_by = user)
            newappoint.firstname= user.first_name
            newappoint.lastname= user.last_name
            newappoint.phone_number = phone_number
            newappoint.email = user.email
            newappoint.save()
            login(request, user)
            messages.success(request, 'You can now book your appointment with the doctor')
            return redirect('index')
        else:
            messages.error(request, form.errors)
            return redirect('signup')
    
    context={
        'form': form,
    }

    return render(request, 'signup.html', context)



def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user:
            login(request, user)
            messages.success(request, f'Welcome back {user.first_name}')
            return redirect('index')
        else:
            messages.info(request, 'make sure both username and password are correct')
            return redirect('signin')

    return render(request, 'signin.html')


def signout(request):
    logout(request)
    return redirect('signin')



def contact_us(request):
    cform = ContactForm()
    if request.method == 'POST':
        cform = ContactForm(request.POST)
        if cform.is_valid():
            cform.save()
            messages.success(request, 'Thank you for contacting us, our customer care will reach you soon')
            return redirect('index')
        else:
            messages.error(request, cform.errors)
            return redirect('contact_us')

    context={
        'cform':cform
    } 

    return render(request, 'contact_us.html', context)



@login_required(login_url='signin')
def profile(request):
    profile = Profile.objects.get(user__username= request.user.username)
    notify = Notice.objects.all()

    context ={
        'profile': profile,
        'notify': notify,
    }
    return render (request, 'profile.html', context)



@login_required(login_url='signin')
def proedit(request):
    load_profile = Profile.objects.get(user__username= request.user.username)
    notify = Notice.objects.all()
    form = ProfileForm(instance=request.user.profile)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form=form.save()
            messages.success(request, f'Dear {form.fullname} your profile updates is successful')
            return redirect('profile')
        else:
            messages.error(request, f' Dear {form.fullname} kindly follow the following instructions {form.errors}, thank you.')
            return redirect('profile')

    context = {
        'load_profile': load_profile,
        'form':form,
        'notify': notify,
    }
    return render(request, 'proedit.html', context)



def show_notice(request, slug, notice_id):
    notify = Notice.objects.get(id=notice_id)

    context={
        'notify': notify
    }

    return render (request, 'profile.html', context)


def delete_notice(request, slug, notice_id):
    notify = Notice.objects.get(id=notice_id)
    notify.viewed = True
    notify.save()

    context={
        'notify': notify
    }

    return redirect ('signin', context)



@login_required(login_url='signin')
def recovery(request):
    load_profile = Profile.objects.get(user__username= request.user.username)
    notify = Notice.objects.filter(notice_by= request.user)
    form = PasswordChangeForm(request.user)
    if request.method == 'POST':
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Password Change Successful')
            return redirect('profile')
        else:
            messages.error(request, form.errors)
            return redirect('recovery')

    context ={
        'load_profile':load_profile,
        'form':form,
        'notify': notify,
    }

    return render(request, 'recovery.html', context)




def pharmacy(request):
    malaria = Pharmacy.objects.filter(malaria=True, display=True).order_by('-id')[:3]
    antibiotics = Pharmacy.objects.filter(antibiotics=True, display=True).order_by('-id')[:3]
    c_f_c= Pharmacy.objects.filter(c_f_c=True, display=True).order_by('-id')[:3]
    supplements = Pharmacy.objects.filter(supplements=True, display=True).order_by('-id')[:3]
    drug = Drug_type.objects.all()

    context ={
        'malaria':malaria,
        'antibiotics':antibiotics,
        'c_f_c':c_f_c,
        'supplements':supplements,
        'drug':drug,
    }
    return render(request, 'pharmacy.html', context)


def searched(request):
    if request.method == 'POST':
        searched = request.POST['itemsearch']
        searched_item = Q(Q(product__icontains=searched) | Q(details__icontains=searched))
        searched_drugs = Pharmacy.objects.filter(searched_item)
        # if searched_drugs is None:
        #     print("we can't find what you looking for ")
    else:
        searched_drugs = Pharmacy.objects.all()

    context={
        'searched_drugs':searched_drugs,
    }
    return render(request, 'searched.html', context)


@login_required(login_url='signin')
def all_drugs(request):
    # shop= Pharmacy.objects.all()

    paginator= Paginator(Pharmacy.objects.all(),6)
    page_number= request.GET.get('page',all)
    shop=paginator.get_page(page_number)

    context ={
        'shop':shop,
    }

    return render(request, 'all_drugs.html', context)



@login_required(login_url='signin')
def details(request, id, slug):
    detail= Pharmacy.objects.get(pk=id)
    # description= Pharmacy.objects.filter(drug_type_id=id)
    shop= Pharmacy.objects.all().order_by('-id')[:3]

    context={
        'detail':detail,
        'shop':shop,
        # 'description':description,
    }

    return render(request, 'details.html', context)



# cart
@login_required(login_url='signin')
def addtocart(request):
    cartup = Profile.objects.get(user__username = request.user.username)
    cart_code = cartup.id
    if request.method == 'POST':
        addquantity = int(request.POST['quantity'])
        addid = request.POST['drugid']
        drugid =Pharmacy.objects.get(pk=addid)
        # instantiate the cart for prospertive users
        drugscart= Drugscart.objects.filter(user__username=request.user.username,item_paid=False)
        if drugscart:
            more = Drugscart.objects.filter(pharmacy_id=drugid.id, quantity = addquantity, user__username= request.user.username).first()
            if more:
                more.quantity=addquantity
                more.save()
                messages.success(request, 'Item has been added to your cart')
                return redirect('pharmacy')
            
            else:
                newcart = Drugscart()
                newcart.user=request.user
                newcart.pharmacy = drugid
                newcart.quantity = addquantity
                newcart.order_no= drugscart[0].order_no
                newcart.item_paid =False
                newcart.save()
                messages.success(request, 'Item has been added to your cart')
                return redirect('pharmacy')
        else:
            newcart = Drugscart()
            newcart.user=request.user
            newcart.pharmacy = drugid
            newcart.quantity = addquantity
            newcart.order_no=cart_code
            newcart.item_paid=False
            newcart.save()
            messages.success(request, 'Item has been added to your cart')
            return redirect('pharmacy')



@login_required(login_url='signin')
def cart(request):
    carty= Drugscart.objects.filter(user__username = request.user.username,item_paid=False)

    subtotal=0
    vat=0
    total= 0
    for item in carty:
        if item:
            subtotal += item.pharmacy.price * item.quantity
    #vatis at 7.5% of the subtotal, that is 7.5/100 * subtotal
    vat = 0.075 * subtotal

    #addition of vat and subtotal gives the total value to be charged
    total= subtotal + vat
    context ={
        'carty':carty,
        'subtotal':subtotal,
        'vat':vat,
        'total':total,
    }
    return render(request, 'cart.html', context)


def upload_prescrip(request):
    
    # upload = Upload_Prescrip.objects.get()
    form = Upload_PrescripForm()
    if request.method == 'POST':
        form = Upload_PrescripForm(request.POST, request.FILES)
        if form.is_valid():
            form=form.save()
            messages.success(request, f'Upload successfull')
            return redirect('checkout')
        else:
            messages.error(request, f'kindly follow the following instructions {form.errors}, thank you.')
            return redirect('cart')


@login_required(login_url='signin')
def remove_item(request):
    deleteitem = request.POST['deleteitem']
    Drugscart.objects.filter(pk=deleteitem).delete()
    messages.success(request, 'item successfully deleted from your cart')
    return redirect('pharmacy')



@login_required(login_url='signin')
def checkout(request):
    carty= Drugscart.objects.filter(user__username= request.user.username, item_paid=False)
    profile = Profile.objects.get(user__username= request.user.username)

    subtotal=0
    vat=0
    total= 0
    for item in carty:
        if item:
            subtotal += item.pharmacy.price * item.quantity
    #vatis at 7.5% of the subtotal, that is 7.5/100 * subtotal
    vat = 0.075 * subtotal

    #addition of vat and subtotal gives the total value to be charged
    total= subtotal + vat
    context ={
        'carty':carty,
        'subtotal':subtotal,
        'vat':vat,
        'total':total,
        'profile':profile
    }

    return render(request, 'checkout.html', context)



@login_required(login_url='signin')
def dashboard(request):
    medical = MedicalRecord.objects.filter(medical_by = request.user)
    # billing = Billing.objects.filter(billing_by = request.user)
    appointy= Appointment.objects.filter(created_by__username = request.user.username)
    billings = Ship.objects.filter(user=request.user)
    billing = Ship_Sub.objects.filter(user=request.user)
    # appt_history = Appointmenthistory.objects.filter(appthistory_by = request.user)
    general = Genaral.objects.filter(general_by=request.user)
    profile = Profile.objects.get(user__username= request.user.username)
    notify = Notice.objects.filter(notice_by= request.user)
    prescripy = Prescription.objects.filter(user__username=request.user.username)

    context ={
        'medical': medical,
        'appointy': appointy,
        'billing': billing,
        'billings': billings,
        # 'appt_history': appt_history,
        'general': general,
        'profile': profile,
        'notify': notify,
        'prescripy': prescripy,
    }
    return render (request, 'dashboard.html', context)



@login_required(login_url='signin')
def prescription(request):
    prescripy = Prescription.objects.filter(user__username=request.user.username)
    notify = Notice.objects.all()

    context ={
        'prescripy': prescripy,
        'notify': notify,
    }
    return render(request, 'prescription.html', context)




@login_required(login_url='signin')
def remove_prescription(request):
    deleteprescrip = request.POST['deleteprescrip']
    Prescription.objects.filter(pk=deleteprescrip).delete()
    messages.success(request, 'prescription successfully deleted')
    return redirect('prescription')



@login_required(login_url='signin')
def paidorder(request):
    if request.method == 'POST':
        # api_key= 'sk_test_371cb1fe66df8f063548bf77f615d1a8c2411f24' 
        # curl= 'https://api.paystack.co/transaction/initialize' 
        # cburl = 'http://127.0.0.1:8000/thankyou/' 
        ref_num = str(uuid.uuid4())
        total = float(request.POST['get_total'])*100
        address= request.POST['address']
        state= request.POST['state']
        phone= request.POST['phone_number']
        cartup = Profile.objects.get(user__username = request.user.username)
        order_num = cartup.id
        user= User.objects.get(username= request.user.username)

        headers= {'Authorization': f'Bearer {api_key}'}
        data = {'reference':ref_num, 'order_number':order_num, 'amount': int(total), 'callback_url': cburl, 'email': user.email, 'currency':'NGN'}



        try:
            r = requests.post(curl, headers=headers, json=data)
        except Exception:
            messages.error(request, 'Please refresh and try again, issue being resolved')
        else:
            transback = json.loads(r.text)
            rd_url = transback['data']['authorization_url']


            # take record of transaction made
            paidorder = Paidorder()
            paidorder.user = user
            paidorder.total = total/100
            paidorder.cart_no = order_num
            paidorder.payment_code = ref_num
            paidorder.paid_item =True
            paidorder.firstname = user.first_name
            # paidorder.name_on_crd = user.first_name and user.last_name
            paidorder.save()


            ship =Ship()
            ship.user = user
            ship.total = total/100
            ship.phone = phone
            ship.state = state
            ship.address = address
            ship.ordr_no = order_num
            ship.itm_paid =True
            ship.firstname = user.first_name
            ship.save()

            return redirect(rd_url)
        return redirect('checkout')


def thankyou(request):
    carty= Drugscart.objects.filter(user__username= request.user.username, item_paid=False)
    for item in carty:
        item.item_paid = True
        item.save()
    return render(request, 'thankyou.html')