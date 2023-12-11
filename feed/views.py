from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'feed/home.html')
def about(request):
    return render(request,'feed/about.html')
def service(request):
    return render(request,'feed/service.html')
def contact(request):
    return render(request,'feed/contact.html')
def car(request):
    return render(request,'feed/car.html')