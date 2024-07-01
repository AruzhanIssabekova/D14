from django.urls import path
from . import views

app_name = 'second_app'

urlpatterns = [
    path('', views.main, name='main'),
    path('services/', views.services, name='services'),
    path('portfolio/', views.portfolio, name='portfolio'),
]
