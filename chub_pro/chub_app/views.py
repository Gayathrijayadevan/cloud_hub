from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import *
from django.contrib.auth.models import User
from django.http import HttpResponse

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

def support(req):
    return render(req,'support.html')

def upload(req):
    if req.method == 'POST':
        title = req.POST['title']
        description = req.POST['description']
        media_file = req.FILES.get('media')
        upload_date = req.POST['date']

        media_type = ''
        if media_file:
            if 'image' in media_file.content_type:
                media_type = 'image'
            elif 'video' in media_file.content_type:
                media_type = 'video'
            elif 'audio' in media_file.content_type:
                media_type = 'audio'
            elif 'text' in media_file.content_type:
                media_type = 'text'

        media_upload = MediaUpload(title=title, description=description,media_file=media_file,media_type=media_type,upload_date=upload_date)
        media_upload.save()
        return redirect(home)

    return render(req,'upload.html')

def display_media(request):
    media_files = MediaUpload.objects.all()

    return render(request, 'media_view.html', {'media_files': media_files})