from django.shortcuts import render

def cars(request):
    return render(request,'car/cars.html')

# Create your views here.
