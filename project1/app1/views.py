from django.shortcuts import render,HttpResponse,redirect
from app1.models import Contact
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .utils import send_email_to_client

# Create your views here.
def index(request):
    return render(request,'index.html')
def contact(request):
        context={"success":False}
        if request.method=="POST":
             name=request.POST.get("name")
             email=request.POST.get("email")
             query=request.POST.get("query")
             instance= Contact(name=name,email=email,query=query)
             instance.save()
             context={"success":True}
        
        return render(request,'contact.html',context)
def login_view(request):
     context={"success":False}
     if request.method=="POST":
             username=request.POST.get("username")
             email=request.POST.get("email")
             pwd=request.POST.get("password")
             user = authenticate(username=username, password=pwd)
             if user is not None:
                   login(request, user)
                   context={"success":"true"}
             else:
                   context={"success":"error"}
             
     return render(request,'login.html',context)

def signup(request):
     context={"success":False}
     if request.method=="POST":
             firstname=request.POST.get("firstname")
             lastname=request.POST.get("lastname")
             username=request.POST.get("username")
             email=request.POST.get("email")
             pwd=request.POST.get("password")
             user = User.objects.create_user(username,email,pwd)
             user.first_name=firstname
             user.last_name=lastname
             user.save()
             send_email_to_client(email)
             context={"success":True}
     return render(request,'signup.html',context)

def logout_view(request):
    context={"success":False}
    logout(request)
    context={"success":"logout"}
    return render(request,"index.html",context)