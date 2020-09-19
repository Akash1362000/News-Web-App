from django.shortcuts import render
from django.http import HttpResponse
# Importing News API
from newsapi import NewsApiClient

# Create your views here.
def Home(request):
    newsapi = NewsApiClient(api_key ='492204b5fab24074b7e237e955eb3218')
    top = newsapi.get_top_headlines(sources ='techcrunch')

    l = top['articles']
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    mylist = zip(news, desc, img)
    return render(request, 'newsapp/home.html', context ={"mylist":mylist})

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

""" def index(request):
    
    newsapi = NewsApiClient(api_key ='492204b5fab24074b7e237e955eb3218')
    top = newsapi.get_top_headlines(sources ='techcrunch')

    l = top['articles']
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    mylist = zip(news, desc, img)


    return render(request, 'newsapp/index.html', context ={"mylist":mylist})
 """
#Test view for Materialized Home Page - Feel free to delete it
def test(request):
    return render(request, 'newsapp/test.html')

