from django.shortcuts import render
from . models import Team
from car.models import Car

# Create your views here.
def home(request):
    teams=Team.objects.all()
    featured=Car.objects.order_by('-created_date').filter(is_featured=True)
    allcar=Car.objects.order_by('-created_date')
    context={'teams':teams,
             'featured':featured,
             'allcar':allcar,
             }
    return render(request,'feed/home.html',context)
def about(request):
    team=Team.objects.all()
    context={'team':team}
    return render(request,'feed/about.html',context)
def service(request):
    return render(request,'feed/service.html')
def contact(request):
    return render(request,'feed/contact.html')
def car(request):
    return render(request,'feed/car.html')