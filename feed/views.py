from django.shortcuts import render,redirect
from . models import Team
from django.core.mail import send_mail
from car.models import Car
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.
def home(request):
    teams=Team.objects.all()
    featured=Car.objects.order_by('-created_date').filter(is_featured=True)
    allcar=Car.objects.order_by('-created_date')
    #search_field=Car.objects.values('model','city','year','body_style')
    model_search=Car.objects.values_list('model',flat=True).distinct()
    city_search=Car.objects.values_list('city',flat=True).distinct()
    year_search=Car.objects.values_list('year',flat=True).distinct()
    body_style_search=Car.objects.values_list('body_style',flat=True).distinct()
    
    context={'teams':teams,
             'featured':featured,
             'allcar':allcar,
             #'search_field':search_field,
             'model_search':model_search,
             'city_search':city_search,
             'year_search':year_search,
             'body_style_search':body_style_search
             }
    return render(request,'feed/home.html',context)
def about(request):
    team=Team.objects.all()
    context={'team':team}
    return render(request,'feed/about.html',context)
def service(request):
    return render(request,'feed/service.html')
def contact(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        subject=request.POST['subject']
        phone=request.POST['phone']
        message=request.POST['message']
        
        email_subject='you have new message from cazone website' + subject
        message_body = 'name: ' + name + '\nemail: ' + email + '\nphone: ' + phone + '\nmessage: ' + message

        
        admin_info=User.objects.get(is_superuser=True)
        admin_email=admin_info.email
        send_mail(
                email_subject,
                message_body,
                'draglow21@gmail.com',
                [admin_email],
                fail_silently=False,
        )
    
        messages.success(request,'thank you for contact us.we will get back you soon')
        return redirect('contact')
    
    return render(request,'feed/contact.html')
def car(request):
    return render(request,'feed/car.html')