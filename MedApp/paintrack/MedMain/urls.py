from django.urls import path
from . import views


urlpatterns = [
    path('', views.registration, name='Register'),
    path('Login', views.login, name='Login'),
    path('Information', views.info, name='Info'),
    path('Congratulations', views.Congrat, name='Congratulations'),
    path('MainPage', views.Main, name='Main'),
    path('PainIntensity', views.intensity, name='PainIntensity'),
    path('sw.js', views.ServiceWorkerView.as_view(), name=views.ServiceWorkerView.name,)
]