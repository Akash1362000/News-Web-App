from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='news-home'),
    path('contact-us', views.ContactUs, name='contact-us'), 
    path('feedback',views.Feedback, name='Feedback'),
    path('forget',views.Forget, name='forget'),
    path('login',views.Login, name='login'),
    path('registration',views.Registration, name='Registration'),
    path('sports',views.Sports, name='sports'),
    path('business',views.Business, name='business'),
    path('entertainment',views.Entertainment, name='entertainment')
]
