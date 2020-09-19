from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login

from .models import *

# Create your views here.


def about(request):
    return render(request, 'about.html')


def index(request):
    if not request.user.is_authenticated:
        return redirect('login')

    doctors = Doctor.objects.all()
    patient = Patient.objects.all()
    appointment = Appointment.objects.all()

    d = 0;
    p = 0;
    a = 0;

    for i in doctors:
        d+=1;
    for i in patient:
        p+=1;
    for i in appointment:
        a+=1;
    
    d1 = {'d':d,'p':p,'a':a}
    return render(request, 'index.html',d1)


def contact(request):
    return render(request, 'contact.html')


def view_Doctor(request):
    doc = Doctor.objects.all()
    d = {'doc':doc}
    return render(request, 'view_doctor.html',d)

def add_Doctor(request):
    error=""
    if request.method=="POST":
        n = request.POST['name']
        c = request.POST['contact']
        sp = request.POST['special']
        try:
            Doctor.objects.create(name=n,mobile=c, special = sp)
            error="no"
        except:
            error="Yes"

    d = {'error':error}
    return render(request,'add_doctor.html',d)

def Delete_Doctor(request, pid):

    doctor = Doctor.objects.get(id=pid)
    doctor.delete()
    return redirect('view_doctor')

def view_Patient(request):
    pat = Patient.objects.all()
    p = {'pat': pat}

    return render(request, 'view_patient.html' , p)

def add_Patient(request):
    error=""
    if request.method=="POST":
        n = request.POST['name']
        g = request.POST['gender']
        c = request.POST['contact']
        add = request.POST['address']
        try:
            Patient.objects.create(name=n,gender=g,mobile=c, address = add)
            error="no"
        except:
            error="Yes"

    d = {'error':error}
    return render(request,'add_patient.html',d)



def Delete_Patient(request, pid):
    
    patient = Patient.objects.get(id=pid)
    patient.delete()
    return redirect('view_patient')

def view_Appointment(request):

    appoint = Appointment.objects.all()
    d = {'appoint':appoint}
    return render(request,'view_appointment.html',d)

def add_Appointment(request):
    error = ""
    doctor1 = Doctor.objects.all()
    patient1 = Patient.objects.all()
    if request.method=="POST":
        d = request.POST['doctor']
        p = request.POST['patient']
        d1 = request.POST['date']
        t = request.POST['time']
        doctor = Doctor.objects.filter(name=d).first()
        patient = Patient.objects.filter(name=p).first()

        try:   
            Appointment.objects.create(doctor=doctor,patient=patient,date1=d1,time1=t)
            error = "no"
        except:
            error = "Yes"

    d = {'doctor':doctor1,'patient':patient1, 'error':error}
    return render(request, 'add_appointment.html',d)

def Delete_Appointment(request, pid):
    
    appointment = Appointment.objects.get(id=pid)
    appointment.delete()

    return redirect('/view_appointment')





def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("/")

        else:
            messages.info(request, 'Invalid credentials, Please Try Again.')
            return redirect('login')

    else:
        return render(request, 'login.html')


def logout(request):

    auth.logout(request)
    return redirect('/')


def register(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('register')

            elif User.objects.filter(email=email).exists():
                messages.info(request, 'email Taken')
                return redirect('register')

            else:
                user = User.objects.create_user(
                    first_name=first_name, last_name=last_name, username=username,  email=email, password=password1)
                user.save()
                print('user created')
                return redirect('login')

        else:
            messages.info(request, 'password not maching')
            return redirect('register')

        return HttpResponseRedirect('/')

    else:
        return render(request, 'register.html')


# def Login(request):
#     error=""
    # if request.method=="POST":
    #     u = request.POST['uname']
    #     p = request.POST['pwd']
    #     user = authenticate(username=u,password=p)
    #     #user.save();
    #     try:
    #         if user.is_staff:
    #             #login(request, user)
    #             return render(request, 'index.html')
    #             error="no"
    #         else:
    #             error="Yes"
    #     except:
    #         error="Yes"
    # d = {'error':error}
    # return render(request,'login.html',d)

# def Logout(request):
#     if not request.user.is_staff:
#         return redirect('login')
#     logout(request)
#     return redirect('login')
