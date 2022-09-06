from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

from django.forms import ModelForm
from userprofile.models import *
from .models import *
from pharmacy.models import *
from pharmcart.models import *


class SignupForm(UserCreationForm):
    username = forms.CharField(max_length=250)
    first_name = forms.CharField(max_length=250)
    last_name = forms.CharField(max_length=250)
    email = forms.EmailField(max_length=50)
    phone_number = forms.CharField(max_length=20)

    class Meta:
        model = User
        fields = ['username','first_name', 'last_name',"phone_number", 'email', 'password1', 'password2']



class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact_us
        fields = ['fullname','phone_number','email','message']


MARITAL =[
    ('Mr', 'Mr'),
    ('Mrs', 'Mrs'),
    ('Miss', 'Miss'),
    ('bruv', 'bruv'),
    ('sis', 'sis'),
]

SEX =[
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other'),
]

GROUP =[
    ('A+', 'A+'),
    ('A-', 'A-'),
    ('O+', 'O+'),
    ('O-', 'O-'),
    ('B+', 'B+'),
    ('B-', 'B-'),
    ('AB+', 'AB+'),
    ('AB-', 'AB-'),
]

STATE=[
    ('Abia', 'Abia'),
    ('Abuja', 'Abuja'),
    ('Edo', 'Edo'),
    ('Kano', 'Kano'),
    ('Lagos', 'Lagos'),
    ('Ogun', 'Ogun'),
    ('Ph', 'Ph'),
]

FAMILY=[
    ('Father', 'Father'),
    ('Mother', 'Mother'),
]
MEDICATION=[
    ('yes', 'yes'),
    ('no', 'no'),
]

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'fullname', 'date_of_birth', 'email', 'marital_status', 'phone_number', 'sex', 'patient_weight', 'patient_height', 'address', 'blood_group', 'city', 'state', 'zip', 'history', 'disease', 'period', 'family', 'details']
        widgets ={
            'image': forms.FileInput(attrs={'class':'rounded-circle', 'placeholder':'upload image file'}),
            'fullname': forms.TextInput(attrs={'class':'form-control', 'PlaceHolder':'fullname'}),
            'date_of_birth': forms.TextInput(attrs={'class':'form-control', 'PlaceHolder':'date_of_birth'}),
            'email': forms.EmailInput(attrs={'class':'form-control', 'placeholder':'email'}),
            'marital_status': forms.Select(attrs={'class':'form-control', 'PlaceHolder':'Marital_status'}),
            'phone_number': forms.TextInput(attrs={'class':'form-control', 'PlaceHolder':'phone_number'}),
            'sex': forms.Select(attrs={'class':'form-control', 'PlaceHolder':'sex'}),
            'patient_weight': forms.TextInput(attrs={'class':'form-control', 'PlaceHolder':'patient_weight'}),
            'patient_height': forms.TextInput(attrs={'class':'form-control', 'PlaceHolder':'patient_height'}),
            'address': forms.TextInput(attrs={'class':'form-control', 'PlaceHolder':'address'}),
            'blood_group': forms.Select(attrs={'class':'form-control', 'PlaceHolder':'blood_group'}),
            'city': forms.TextInput(attrs={'class':'form-control', 'PlaceHolder':'city'}),
            'state': forms.Select(attrs={'class':'form-control', 'PlaceHolder':'state'}),
            'zip': forms.NumberInput(attrs={'class':'form-control', 'PlaceHolder':'zip'}),
            'history': forms.TextInput(attrs={'class':'form-control', 'PlaceHolder':'history'}),
            'disease': forms.TextInput(attrs={'class':'form-control', 'PlaceHolder':'disease'}),
            'period': forms.TextInput(attrs={'class':'form-control', 'PlaceHolder':'period'}),
            'family': forms.Select(attrs={'class':'form-control', 'PlaceHolder':'family'}),
            'details': forms.TextInput(attrs={'class':'form-control', 'PlaceHolder':'details'}),
        }

class DrugscartForm(forms.ModelForm):
    class Meta:
        model = Drugscart
        fields= ['quantity', 'product_name']

SERVICES =[
    ('Select Your Service', 'Select Your Service'),
    ('Therapy Session', 'Therapy Session'),
    ('Treatment', 'Treatment'),
    ('Family Planning', 'Family Planning'),
    ('Dental', 'Dental'),
    ('Optical', 'Optical'),
    ('Paediatrics', 'Paediatrics'),
    ('Gynecology', 'Gynecology'),
    ('Surgical', 'Surgical'),
]

DATE =[
    ('Day', 'Day'),
    ('Monday', 'Monday'),
    ('Tuesday', 'Tuesday'),
    ('Wednesday', 'Wednesday'),
    ('Friday', 'Friday'),
    ('Saturday', 'Saturday'),
]

TIME =[
    ('Time', 'Time'),
    ('10:00am - 11:00am', '10:00am - 11:00am'),
    ('11:30am - 12:30pm', '11:30am - 12:30pm'),
    ('1:00pm - 2:00pm', '1:00pm - 2:00pm'),
    ('2:30pm - 3:30pm', '2:30pm - 3:30pm'),
    ('4:00pm - 5:00pm', '4:00pm - 5:00pm'),
]

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields= ['firstname', 'lastname', 'services', 'phone_number','follow_up', 'apptdate', 'appt_time', 'email','price', 'symptoms', 'notify']
        widgets ={
            'firstname': forms.TextInput(attrs={'class':'form-control frm1', 'placeholder':'First Name'}),
            'lastname': forms.TextInput(attrs={'class':'form-control frm1', 'PlaceHolder':'Last Name'}),
            'services': forms.Select(attrs={'class':'form-control frm1 mt-3', 'PlaceHolder':'Select Your Services'},choices=SERVICES),
            'phone_number': forms.TextInput(attrs={'class':'form-control frm1 mt-3', 'PlaceHolder':'phone_number'}),
            'follow_up': forms.TextInput(attrs={'class':'form-control frm1 mt-3', 'PlaceHolder':'follow up'}),
            'apptdate': forms.Select(attrs={'class':'form-control frm1 mt-3', 'PlaceHolder':'Select the Day'}, choices= DATE),
            'appt_time': forms.Select(attrs={'class':'form-control frm1 mt-3', 'placeholder':'Select your Time'}, choices= TIME),
            'email': forms.EmailInput(attrs={'class':'form-control frm1 mt-3', 'placeholder':'email'}),
            'price': forms.TextInput(attrs={'class': 'frm3'}),
            'symptoms': forms.TextInput(attrs={'class':'form-control frm1 mt-3', 'PlaceHolder':'symptoms'}),
            'notify': forms.CheckboxInput()
        }


class Upload_PrescripForm(forms.ModelForm):
    class Meta:
        model = Upload_Prescrip
        fields= ['fullname', 'email', 'phone', 'document', 'message']
        widgets ={
            'fullname': forms.TextInput(attrs={'class':'form-control', 'placeholder':'fullname'}),
            'email': forms.EmailInput(attrs={'class':'form-control', 'placeholder':'email'}),
            'phone': forms.TextInput(attrs={'class':'form-control', 'PlaceHolder':'phone_number'}),
            'document': forms.FileInput(attrs={'class':'form-control', 'PlaceHolder':'documents'}),
            'message': forms.TextInput(attrs={'class':'form-control', 'PlaceHolder':'message'}),
        }

















# used for users to create account for theirs
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms


from pharmacycart.models import *
from userprofile.models import Contact_us, Profile
from . models import Appointment
from pharmacy.models import Upload_Prescrip





class SignupForm(UserCreationForm):
    username = forms.CharField(max_length=10)
    first_name = forms.CharField(max_length=250)
    last_name = forms.CharField(max_length=250)
    email = forms.EmailField(max_length=50)


    class Meta:
        model = User
        fields = ['username', 'first_name','last_name','email', 'password1', 'password2']


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact_us
        fields = ['fullname','phone_number','email','message']


MARITAL =[
    ('Mr', 'Mr'),
    ('Mrs', 'Mrs'),
    ('Miss', 'Miss'),
    ('bruv', 'bruv'),
    ('sis', 'sis'),
]

SEX =[
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other'),
]

GROUP =[
    ('A+', 'A+'),
    ('A-', 'A-'),
    ('O+', 'O+'),
    ('O-', 'O-'),
    ('B+', 'B+'),
    ('B-', 'B-'),
    ('AB+', 'AB+'),
    ('AB-', 'AB-'),
]

STATE=[
    ('Abia', 'Abia'),
    ('Abuja', 'Abuja'),
    ('Edo', 'Edo'),
    ('Kano', 'Kano'),
    ('Lagos', 'Lagos'),
    ('Ogun', 'Ogun'),
    ('Ph', 'Ph'),
]

FAMILY=[
    ('Father', 'Father'),
    ('Mother', 'Mother'),
]
MEDICATION=[
    ('yes', 'yes'),
    ('no', 'no'),
]

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'fullname', 'date_of_birth', 'email', 'marital_status', 'phone_number', 'sex', 'patient_weight', 'patient_height', 'address', 'blood_group', 'city', 'state', 'zip', 'history', 'disease', 'period', 'family', 'details']
        widgets ={
            'image': forms.FileInput(attrs={'class':'rounded-circle', 'placeholder':'upload image file'}),
            'fullname': forms.TextInput(attrs={'class':'form-control', 'PlaceHolder':'fullname'}),
            'date_of_birth': forms.TextInput(attrs={'class':'form-control', 'PlaceHolder':'date_of_birth'}),
            'email': forms.EmailInput(attrs={'class':'form-control', 'placeholder':'email'}),
            'marital_status': forms.Select(attrs={'class':'form-control', 'PlaceHolder':'Marital_status'}, choices=MARITAL ),
            'phone_number': forms.TextInput(attrs={'class':'form-control', 'PlaceHolder':'phone_number'}),
            'sex': forms.Select(attrs={'class':'form-control', 'PlaceHolder':'sex'}, choices= SEX),
            'patient_weight': forms.TextInput(attrs={'class':'form-control', 'PlaceHolder':'patient_weight'}),
            'patient_height': forms.TextInput(attrs={'class':'form-control', 'PlaceHolder':'patient_height'}),
            'address': forms.TextInput(attrs={'class':'form-control', 'PlaceHolder':'address'}),
            'blood_group': forms.Select(attrs={'class':'form-control', 'PlaceHolder':'blood_group'}, choices=GROUP),
            'city': forms.TextInput(attrs={'class':'form-control', 'PlaceHolder':'city'}),
            'state': forms.Select(attrs={'class':'form-control', 'PlaceHolder':'state'}, choices=STATE),
            'zip': forms.NumberInput(attrs={'class':'form-control', 'PlaceHolder':'zip'}),
            'history': forms.TextInput(attrs={'class':'form-control', 'PlaceHolder':'history'}),
            'disease': forms.TextInput(attrs={'class':'form-control', 'PlaceHolder':'disease'}),
            'period': forms.TextInput(attrs={'class':'form-control', 'PlaceHolder':'period'}),
            'family': forms.Select(attrs={'class':'form-control', 'PlaceHolder':'family'}, choices=FAMILY),
            'details': forms.TextInput(attrs={'class':'form-control', 'PlaceHolder':'details'}),
        }




class DrugscartForm(forms.ModelForm):
    class Meta:
        model = Drugscart
        fields= ['quantity', 'product_name']


SERVICES =[
    ('Select Your Service', 'Select Your Service'),
    ('Therapy Session', 'Therapy Session'),
    ('Treatment', 'Treatment'),
    ('Family Planning', 'Family Planning'),
    ('Dental', 'Dental'),
    ('Optical', 'Optical'),
    ('Paediatrics', 'Paediatrics'),
    ('Gynecology', 'Gynecology'),
    ('Surgical', 'Surgical'),
]

DATE =[
    ('Day', 'Day'),
    ('Monday', 'Monday'),
    ('Tuesday', 'Tuesday'),
    ('Wednesday', 'Wednesday'),
    ('Friday', 'Friday'),
    ('Saturday', 'Saturday'),
]

TIME =[
    ('Time', 'Time'),
    ('10:00am - 11:00am', '10:00am - 11:00am'),
    ('11:30am - 12:30pm', '11:30am - 12:30pm'),
    ('1:00pm - 2:00pm', '1:00pm - 2:00pm'),
    ('2:30pm - 3:30pm', '2:30pm - 3:30pm'),
    ('4:00pm - 5:00pm', '4:00pm - 5:00pm'),
]



class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields= ['firstname', 'lastname', 'services', 'phone_number','follow_up', 'apptdate', 'appt_time', 'email','price', 'symptoms', 'notify']
        widgets ={
            'firstname': forms.TextInput(attrs={'class':'form-control frm1', 'placeholder':'First Name'}),
            'lastname': forms.TextInput(attrs={'class':'form-control frm1', 'PlaceHolder':'Last Name'}),
            'services': forms.Select(attrs={'class':'form-control frm1 mt-3', 'PlaceHolder':'Select Your Services'},choices=SERVICES),
            'phone_number': forms.TextInput(attrs={'class':'form-control frm1 mt-3', 'PlaceHolder':'phone_number'}),
            'follow_up': forms.TextInput(attrs={'class':'form-control frm1 mt-3', 'PlaceHolder':'follow up'}),
            'apptdate': forms.Select(attrs={'class':'form-control frm1 mt-3', 'PlaceHolder':'Select the Day'}, choices= DATE),
            'appt_time': forms.Select(attrs={'class':'form-control frm1 mt-3', 'placeholder':'Select your Time'}, choices= TIME),
            'email': forms.EmailInput(attrs={'class':'form-control frm1 mt-3', 'placeholder':'email'}),
            'price': forms.TextInput(attrs={'class': 'frm3'}),
            'symptoms': forms.TextInput(attrs={'class':'form-control frm1 mt-3', 'PlaceHolder':'symptoms'}),
            'notify': forms.CheckboxInput()
        }



class Upload_PrescripForm(forms.ModelForm):
    class Meta:
        model = Upload_Prescrip
        fields= ['fullname', 'email', 'phone', 'document', 'message']
        widgets ={
            'fullname': forms.TextInput(attrs={'class':'form-control', 'placeholder':'fullname'}),
            'email': forms.EmailInput(attrs={'class':'form-control', 'placeholder':'email'}),
            'phone': forms.TextInput(attrs={'class':'form-control', 'PlaceHolder':'phone_number'}),
            'document': forms.FileInput(attrs={'class':'form-control', 'PlaceHolder':'documents'}),
            'message': forms.TextInput(attrs={'class':'form-control', 'PlaceHolder':'message'}),
        }

