from django.urls import path, include
from . import views
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.Home, name='news-home'),
    path('contact-us', views.ContactUs, name='contact-us'), 
    path('feedback',views.Feedback, name='Feedback'),
    path('forget',views.Forget, name='forget'),
    path('login/',auth_views.LoginView.as_view(template_name = 'newsapp/login.html'), name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name = 'newsapp/logout.html'), name='logout'),
    path('sports',views.Sports, name='sports'),
    path('technology',views.Technology, name='technology'),
    path('health',views.Health, name='health'),
    path('science',views.Science, name='science'),
    path('business',views.Business, name='business'),
    path('entertainment',views.Entertainment, name='entertainment'),
    path('register', views.register, name='register'),
    path('test', views.test, name='test'), #test url pattern
    #path('', include('pwa.urls')),
    path('serviceworker.js', (TemplateView.as_view(template_name="newsapp/serviceworker.js", 
    content_type='application/x-javascript', )), name='serviceworker.js'),
    path('webpush', include('webpush.urls')),

    path('send_push', views.send_push), # Web push url Patterns
    path('webpush/', include('webpush.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
