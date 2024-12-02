from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import *
from django.contrib.auth.models import User

# Create your views here.
def chub_login(req):
    if req.method=='POST':
        uname=req.POST['uname']
        password=req.POST['password']
        data=authenticate(username=uname,password=password)
        if data:
            login(req,data)
            return redirect(home)
        else:
            messages.warning(req,'invalid username or password') 
            return redirect(chub_login)     
    else:     
        return render(req,'login.html')
    
def chub_logout(req):
    logout(req)
    return redirect(chub_login)    

def register(req):
    if req.method=='POST':
        uname=req.POST['uname']
        email=req.POST['email']
        pswd=req.POST['pswd']
        try:
            data=User.objects.create_user(first_name=uname,email=email,username=email,password=pswd)
            data.save()
        except:
            messages.warning(req,'invalid username or password')
            return redirect(register)   
        return redirect(chub_login) 
    else:
        return render(req,'register.html')    
    
def home(req):
    return render(req,'home.html')