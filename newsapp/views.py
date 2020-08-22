from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Home(request):
    return render(request, 'newsapp/home.html')

def ContactUs(request):
    return render(request, 'newsapp/contact_us.html')
