from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import UserRegisterForm
from .services import get_news


def Home(request):
    news_data = get_news(country="in", category="general")
    return render(request, "newsapp/home.html", context={"mylist": news_data})


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


def Technology(request):
    news_data = get_news(country="in", category="technology")
    return render(request, "newsapp/technology.html", context={"mylist": news_data})


def Health(request):
    news_data = get_news(country="in", category="health")
    return render(request, "newsapp/health.html", context={"mylist": news_data})


def Science(request):
    news_data = get_news(country="in", category="science")
    return render(request, "newsapp/science.html", context={"mylist": news_data})


def Sports(request):
    news_data = get_news(country="in", category="sports")
    return render(request, "newsapp/sports.html", context={"mylist": news_data})


def Entertainment(request):
    news_data = get_news(country="in", category="entertainment")
    return render(request, "newsapp/entertainment.html", context={"mylist": news_data})


def Business(request):
    news_data = get_news(country="in", category="business")
    return render(request, "newsapp/business.html", context={"mylist": news_data})
