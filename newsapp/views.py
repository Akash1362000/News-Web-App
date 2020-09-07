from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Home(request):
    return render(request, 'newsapp/home.html')

def ContactUs(request):
    return render(request, 'newsapp/contact_us.html')

<<<<<<< HEAD

def Feedback(request):
    return render(request, 'newsapp/feedbacks.html')


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

=======
def forgot_password(request):
    return render(request, 'newsapp/forget.html')
    
def feedback(request):
    return render(request, 'newsapp/feedback.html')

def registration(request):
    return render(request, 'newsapp/registration.html')
>>>>>>> c267fcc8387ff7722811aba1c3b53d26c3a2689e
