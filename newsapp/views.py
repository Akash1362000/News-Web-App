import json

from django.conf import settings
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponse

# Imports for Web Push Notifications
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET, require_POST

# Importing News API
from newsapi import NewsApiClient

from .forms import UserRegisterForm


# Create your views here.
def Home(request):
    newsapi = NewsApiClient(api_key="492204b5fab24074b7e237e955eb3218")
    top = newsapi.get_top_headlines(sources="techcrunch")

    l = top["articles"]
    desc = []
    news = []
    img = []
    url = []

    for i in range(len(l)):
        f = l[i]
        news.append(f["title"])
        desc.append(f["description"])
        img.append(f["urlToImage"])
        url.append(f["url"])
    mylist = zip(news, desc, img, url)
    return render(request, "newsapp/home.html", context={"mylist": mylist})


def Technology(request):
    newsapi = NewsApiClient(api_key="492204b5fab24074b7e237e955eb3218")
    top = newsapi.get_top_headlines(category="technology", country="in")

    l = top["articles"]
    desc = []
    news = []
    img = []
    url = []

    for i in range(len(l)):
        f = l[i]
        news.append(f["title"])
        desc.append(f["description"])
        img.append(f["urlToImage"])
        url.append(f["url"])
    mylist = zip(news, desc, img, url)
    return render(request, "newsapp/technology.html", context={"mylist": mylist})


def Health(request):
    newsapi = NewsApiClient(api_key="492204b5fab24074b7e237e955eb3218")
    top = newsapi.get_top_headlines(category="health", country="in")

    l = top["articles"]
    desc = []
    news = []
    img = []
    url = []

    for i in range(len(l)):
        f = l[i]
        news.append(f["title"])
        desc.append(f["description"])
        img.append(f["urlToImage"])
        url.append(f["url"])
    mylist = zip(news, desc, img, url)
    return render(request, "newsapp/health.html", context={"mylist": mylist})


def Science(request):
    newsapi = NewsApiClient(api_key="492204b5fab24074b7e237e955eb3218")
    top = newsapi.get_top_headlines(category="science", country="in")

    l = top["articles"]
    desc = []
    news = []
    img = []
    url = []

    for i in range(len(l)):
        f = l[i]
        news.append(f["title"])
        desc.append(f["description"])
        img.append(f["urlToImage"])
        url.append(f["url"])
    mylist = zip(news, desc, img, url)
    return render(request, "newsapp/science.html", context={"mylist": mylist})


def ContactUs(request):
    return render(request, "newsapp/contact_us.html")


def Feedback(request):
    return render(request, "newsapp/feedback.html")


def Forget(request):
    return render(request, "newsapp/forget.html")


def Sports(request):
    newsapi = NewsApiClient(api_key="492204b5fab24074b7e237e955eb3218")
    top = newsapi.get_top_headlines(category="sports", country="in")

    l = top["articles"]
    desc = []
    news = []
    img = []
    url = []

    for i in range(len(l)):
        f = l[i]
        news.append(f["title"])
        desc.append(f["description"])
        img.append(f["urlToImage"])
        url.append(f["url"])
    mylist = zip(news, desc, img, url)
    return render(request, "newsapp/sports.html", context={"mylist": mylist})


def Entertainment(request):
    newsapi = NewsApiClient(api_key="492204b5fab24074b7e237e955eb3218")
    top = newsapi.get_top_headlines(category="entertainment", country="in")

    l = top["articles"]
    desc = []
    news = []
    img = []
    url = []

    for i in range(len(l)):
        f = l[i]
        news.append(f["title"])
        desc.append(f["description"])
        img.append(f["urlToImage"])
        url.append(f["url"])
    mylist = zip(news, desc, img, url)
    return render(request, "newsapp/entertainment.html", context={"mylist": mylist})


def Business(request):
    newsapi = NewsApiClient(api_key="492204b5fab24074b7e237e955eb3218")
    top = newsapi.get_top_headlines(category="business", country="in")

    l = top["articles"]
    desc = []
    news = []
    img = []
    url = []

    for i in range(len(l)):
        f = l[i]
        news.append(f["title"])
        desc.append(f["description"])
        img.append(f["urlToImage"])
        url.append(f["url"])
    mylist = zip(news, desc, img, url)
    return render(request, "newsapp/business.html", context={"mylist": mylist})


def register(request):
    form_class = UserRegisterForm
    form = form_class(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(
                request,
                f"Account successfully created for { username }. You can now login",
            )
            return redirect("login")
    else:
        form = UserRegisterForm()
    return render(request, "newsapp/register.html", {"form": form})
