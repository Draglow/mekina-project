from django.shortcuts import render,get_object_or_404
from .models import Car
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator

def cars(request):
    cars=Car.objects.order_by('-created_date')
    paginator=Paginator(cars,4)
    page=request.GET.get('page')
    car_page=paginator.get_page(page)
    context={'cars':car_page}
    return render(request,'car/cars.html',context)
def detail_car(request,id):
    detail=get_object_or_404(Car,pk=id)
    context={'detail':detail}
    return render(request,'car/detail.html',context)

# Create your views here.
