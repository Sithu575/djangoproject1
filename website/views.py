from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages


def home(request):
    if request.method =="POST":
        username=request.POST['username']  #name in the [] bracket is same as in the form name
        password=request.POST['password']
        #authenticate
        user= authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"you have been loged in")
            return redirect('home')
        else:
            messages.success(request,"there was an error login")
            return redirect('home')
    else:
        return render(request,'home.html',{})

# Create your views 


def logout_user(request):
	logout(request)
	messages.success(request, "You Have Been Logged Out...")
	return redirect('home')

def register_user(request):
	   return render(request,'register.html',{})
