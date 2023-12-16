from django.shortcuts import render
from . models import Team

# Create your views here.
def home(request):
    teams=Team.objects.all()
    context={'teams':teams}
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