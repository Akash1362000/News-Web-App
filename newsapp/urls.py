from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='news-home'),
    path('contact-us', views.ContactUs, name='contact-us'), 
    path('feedback',views.feedback, name='Feedback'),
    path('registration',views.registration, name='Registration'),
    path('forgot',views.forgot_password, name='Forgot_Password')
]

