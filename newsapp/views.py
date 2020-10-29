from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserRegisterForm
from django.contrib import messages
# Importing News API
from newsapi import NewsApiClient

# Imports for Web Push Notifications
from django.http.response import JsonResponse, HttpResponse
from django.views.decorators.http import require_GET, require_POST
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from webpush import send_user_notification
import json
from django.conf import settings

# Create your views here.
def Home(request):
    newsapi = NewsApiClient(api_key ='492204b5fab24074b7e237e955eb3218')
    top = newsapi.get_top_headlines(sources ='techcrunch')

    l = top['articles']
    desc =[]
    news =[]
    img =[]
    url = []

    for i in range(len(l)):
        f = l[i]
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
        url.append(f['url'])
    mylist = zip(news, desc, img, url)
    webpush_settings = getattr(settings, 'WEBPUSH_SETTINGS', {})
    vapid_key = webpush_settings.get('VAPID_PUBLIC_KEY')
    user = request.user
    return render(request, 'newsapp/home.html', context ={"mylist":mylist, "user": user, 'vapid_key': vapid_key})

def Technology(request):
    newsapi = NewsApiClient(api_key ='492204b5fab24074b7e237e955eb3218')
    top = newsapi.get_top_headlines(category='technology', country='in')

    l = top['articles']
    desc =[]
    news =[]
    img =[]
    url = []

    for i in range(len(l)):
        f = l[i]
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
        url.append(f['url'])
    mylist = zip(news, desc, img, url)
    return render(request, 'newsapp/technology.html', context ={"mylist":mylist})

def Health(request):
    newsapi = NewsApiClient(api_key ='492204b5fab24074b7e237e955eb3218')
    top = newsapi.get_top_headlines(category='health', country='in')

    l = top['articles']
    desc =[]
    news =[]
    img =[]
    url = []

    for i in range(len(l)):
        f = l[i]
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
        url.append(f['url'])
    mylist = zip(news, desc, img, url)
    return render(request, 'newsapp/health.html', context ={"mylist":mylist})

def Science(request):
    newsapi = NewsApiClient(api_key ='492204b5fab24074b7e237e955eb3218')
    top = newsapi.get_top_headlines(category='science', country='in')

    l = top['articles']
    desc =[]
    news =[]
    img =[]
    url = []

    for i in range(len(l)):
        f = l[i]
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
        url.append(f['url'])
    mylist = zip(news, desc, img, url)
    return render(request, 'newsapp/science.html', context ={"mylist":mylist})


def ContactUs(request):
    return render(request, 'newsapp/contact_us.html')

def Feedback(request):
    return render(request, 'newsapp/feedback.html')

def Forget(request):
    return render(request, 'newsapp/forget.html')

def Sports(request):
    newsapi = NewsApiClient(api_key ='492204b5fab24074b7e237e955eb3218')
    top = newsapi.get_top_headlines(category='sports', country='in')

    l = top['articles']
    desc =[]
    news =[]
    img =[]
    url = []

    for i in range(len(l)):
        f = l[i]
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
        url.append(f['url'])
    mylist = zip(news, desc, img, url)
    return render(request, 'newsapp/sports.html', context ={"mylist":mylist})

def Entertainment(request):
    newsapi = NewsApiClient(api_key ='492204b5fab24074b7e237e955eb3218')
    top = newsapi.get_top_headlines(category='entertainment', country='in')

    l = top['articles']
    desc =[]
    news =[]
    img =[]
    url = []

    for i in range(len(l)):
        f = l[i]
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
        url.append(f['url'])
    mylist = zip(news, desc, img, url)
    return render(request, 'newsapp/entertainment.html', context ={"mylist":mylist})

def Business(request):
    newsapi = NewsApiClient(api_key ='492204b5fab24074b7e237e955eb3218')
    top = newsapi.get_top_headlines(category='business', country='in')

    l = top['articles']
    desc =[]
    news =[]
    img =[]
    url = []

    for i in range(len(l)):
        f = l[i]
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
        url.append(f['url'])
    mylist = zip(news, desc, img, url)
    return render(request, 'newsapp/business.html', context ={"mylist":mylist})

#Test view for Materialized Home Page - Feel free to delete it
def test(request):
    return render(request, 'newsapp/test.html')

# View for Web Push Notifications
@require_POST
@csrf_exempt
def send_push(request):
    try:
        body = request.body
        data = json.loads(body)

        if 'head' not in data or 'body' not in data or 'id' not in data:
            return JsonResponse(status=400, data={"message": "Invalid data format"})

        user_id = data['id']
        user = get_object_or_404(User, pk=user_id)
        payload = {'head': data['head'], 'body': data['body']}
        send_user_notification(user=user, payload=payload, ttl=1000)

        return JsonResponse(status=200, data={"message": "Web push successful"})
    except TypeError:
        return JsonResponse(status=500, data={"message": "An error occurred"})


def register(request):
    form_class = UserRegisterForm
    form = form_class(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account successfully created for { username }. You can now login')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'newsapp/register.html', {'form': form })

