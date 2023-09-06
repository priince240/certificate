from django.shortcuts import render,HttpResponseRedirect,redirect,HttpResponse
from .form import signform
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from .models import uploads
from datetime import datetime
from rest_framework import viewsets
from . serializer import api_serializer
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.

def home(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            name=request.POST.get('name')
            file=request.FILES.get('file')
            data=uploads(name=name,file=file,date=datetime.now())
            data.save()
            return redirect("/table")
        return render(request,"home.html")
    else:
        return HttpResponseRedirect("/login")


def signup(request):
    if request.method == 'POST':
        data=signform(data=request.POST)
        if data.is_valid():
            messages.success(request,"signup succesfull-----------------")
            data.save()
            return redirect("/")
    else:
        data=signform()
        
    return render(request,"signup.html",{'data':data})

def loginn(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            data=AuthenticationForm(request=request,data=request.POST)
            if  data.is_valid():
                username=data.cleaned_data['username']
                password=data.cleaned_data['password']
                user=authenticate(username=username,password=password)
                if user is not None:
                    messages.success(request,'login success')
                    login(request,user)
                    return HttpResponseRedirect("/")
        else:
            data=AuthenticationForm()
            
    return render(request,"login.html",{'data':data})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/login")                

def table(request):
    if request.user.is_authenticated:
        data=uploads.objects.all()
    return render (request , "table.html",{'data':data} )

def download(request,id):
    upload_file=uploads.objects.get(id=id)
    response=HttpResponse(upload_file.file,content_type="application/force-download")
    response['content-Disposition']=f'attachment:filename="{upload_file.file.name}"'
    return response
    
class api_viewset(viewsets.ModelViewSet):
    queryset = uploads.objects.all()
    serializer_class=api_serializer
    authentication_classes=[SessionAuthentication]
    permission_classes=[IsAuthenticated]
    
        