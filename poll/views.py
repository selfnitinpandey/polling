from django.shortcuts import render
from django.contrib import messages
from .forms import UserRegistration
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login,authenticate,logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect,HttpResponse
from .models import Addpoll
# Create your views here.

# homepage
def home(request):
    if request.user.is_authenticated:
        addpoll=Addpoll.objects.all()
        context={
            'addpoll':addpoll
        }
        return render(request,'dashboard.html',context)
    else:
        return HttpResponseRedirect('/login/')
# register
def register(request):
    if request.method=='POST':
        form=UserRegistration(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Registration has been Done,Please LogIn')
            return HttpResponseRedirect('/login/')
        else:
            messages.warning(request,'Registration has been Failed ,Try to repeat')
            return HttpResponseRedirect('/signup/')

    else:
        form=UserRegistration()
        context={
            'form':form,
        }
        return render(request,'register.html',context)

# login
def login(request):
    if request.method=="POST":
        form=AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(username=username,password=password)
            if user.is_superuser:
                if user is not None:
                    auth_login(request, user)
                    return HttpResponseRedirect('/admin/')
            else:
                if user is not None:
                    auth_login(request,user)
                    return HttpResponseRedirect('/')
                else:
                    messages.error(request,'Invalid username and password!')
        else:
            messages.error(request,'Invalid username and password!')
            
    form=AuthenticationForm()
    return render(request,'login.html',{'fm':form})

# logout
import time
def logout(request):
    time.sleep(1)
    auth_logout(request)
    return HttpResponseRedirect('/login/')
    
# add_poll
def add_poll(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            question=request.POST.get('question')
            first_c=request.POST.get('first_c')
            second_c=request.POST.get('second_c')
            third_c=request.POST.get('third_c')
            fourth_c=request.POST.get('fourth_c')
            if len(question and first_c and second_c and third_c and fourth_c)!=0:
                user=request.user
                addpoll=Addpoll.objects.create(user=user,question=question,first_c=first_c,second_c=second_c,third_c=third_c,fourth_c=fourth_c)
                addpoll.save()
                messages.success(request,'Data Has been saved.')
                return HttpResponseRedirect('/add_poll/')
            else:
                messages.success(request,'Please fill the all fields..')
                return HttpResponseRedirect('/add_poll/')
        else:        
            return render(request,'addpoll.html')
    else:
        return HttpResponseRedirect('/login/')

# profile
def profile(request):
    if request.user.is_authenticated:
        user=request.user
        userdetails=User.objects.filter(username=user)
        addpoll=Addpoll.objects.filter(user=user)
        context={
            'userdetails':userdetails,
            'addpoll':addpoll
        }
        return render(request,'profile.html',context)
    else:
        return HttpResponseRedirect('/login/')

def addpolledit(request,pk):
    if request.user.is_authenticated:
        if request.method=="POST":
            question=request.POST.get('question')
            first_c=request.POST.get('first_c')
            second_c=request.POST.get('second_c')
            third_c=request.POST.get('third_c')
            fourth_c=request.POST.get('fourth_c')
            if len(question and first_c and second_c and third_c and fourth_c)!=0:
                user=request.user
                addpoll=Addpoll.objects.create(user=user,question=question,first_c=first_c,second_c=second_c,third_c=third_c,fourth_c=fourth_c)
                addpoll.save()
                messages.success(request,'Data Has been Updated.')
                return HttpResponseRedirect('/profile/')
            else:
                messages.success(request,'Please fill the all fields..')
                return HttpResponseRedirect('/add_poll/')
        else:
            addpoll=Addpoll.objects.filter(id=pk)
            context={
                'addpoll':addpoll
            }
            return render(request,'addpolledit.html',context)
    else:
        return HttpResponseRedirect('/login/')

def delete(request,pk):
    addpoll=Addpoll.objects.get(id=pk)
    addpoll.delete()
    messages.success(request,'Data Deleted..')

    return HttpResponseRedirect('/profile/')