from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Home(request):
    return render(request, 'newsapp/home.html')

def ContactUs(request):
    return render(request, 'newsapp/contact_us.html')

def forgot_password(request):
    return render(request, 'newsapp/forget.html')
    
def feedback(request):
    return render(request, 'newsapp/feedback.html')

def registration(request):
    return render(request, 'newsapp/registration.html')
