from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='news-home'),
    path('contact-us', views.ContactUs, name='contact-us') 
    path('feedback',views.Feedback, name='Feedback')
]