from django.shortcuts import render
from . models import Team
from car.models import Car

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
    return render(request,'feed/contact.html')
def car(request):
    return render(request,'feed/car.html')