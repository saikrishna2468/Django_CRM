from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
# Create your views here.
def Home(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        #authenticate
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"you have logged In!")
            return redirect('home')
        else:
            messages.success(request,"There was an error Logging In ,please try agian")
    else:
        return render(request,'home.html')
    return render(request,'home.html')

def logout_user(request):
    logout(request)
    messages.success(request,"you have been logged out...")
    return redirect('home')
def register(request):
    return render(request,'register.html')