from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Home(request):
    return render(request, 'newsapp/home.html')

def ContactUs(request):
    return render(request, 'newsapp/contact_us.html')

def Feedback(request):
    return render(request, 'newsapp/feedback.html')

def Registration(request):
    return render(request, 'newsapp/registration.html')

def Login(request):
    return render(request, 'newsapp/login.html')

def Forget(request):
    return render(request, 'newsapp/forget.html')

def Sports(request):
    return render(request, 'newsapp/sports.html')

def Entertainment(request):
    return render(request, 'newsapp/entertainment.html')

def Business(request):
    return render(request, 'newsapp/business.html')