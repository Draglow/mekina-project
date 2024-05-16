from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth
from contacts.models import Contact
from django.contrib.auth.decorators import login_required
# Create your views here.

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        
        if user is not None:
            auth.login(request,user)
            messages.success(request,'you are succesfuly logged in')
            return redirect('dashboard')
        else:
            messages.error(request,'invalid login credential')
            return redirect('login')
    return render(request,'account/login.html')

def register(request):
    if request.method=='POST':
       firstname=request.POST['firstname']
       lastname=request.POST['lastname']
       username=request.POST['username']
       email=request.POST['email']
       password=request.POST['password']
       confirm_password=request.POST['confirm_password']
       
       if password==confirm_password:
           if User.objects.filter(username=username).exists():
                messages.error(request,'username already exist')
                return redirect(register)
           else:
               if User.objects.filter(email=email).exists():
                   messages.error(request,'email alread exists!')
                   return redirect('register')
               else:
                   if len(username)<=3:
                       messages.error(request,'the length of username must grater than three')
                       return redirect('register')
                   else:
                       if len(password)<8:
                           messages.error(request,'password should be 8 character long')
                       else:
                           if not username.isalnum():
                               messages.error(request,'username should only contain alphanumeric character')
                           else:
                                user=User.objects.create_user(first_name=firstname,last_name=lastname,username=username,email=email,password=password)
                                auth.login(request,user)
                                messages.success(request,'you are logged in successfuly')
                                return redirect('dashboard')
                                user.save()
                                messages.success(request,'you are registered successfuly')
                                return redirect('login')
       else:
           messages.error(request,'password do not match')
    return render(request,'account/register.html')
@login_required(login_url=login)
def dashboard(request):
    dashboard=Contact.objects.order_by('-created_date').filter(user_id=request.user.id)
    context={
        'dashboard':dashboard
    }
    return render(request,'account/dashboard.html',context)

def logout(request):
    if request.method=='POST':
        auth.logout(request)
        messages.success(request,'you are successfully logged out.')
        return redirect('home')
    return redirect('home')