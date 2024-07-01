from django.urls import path
from . import views

app_name = 'bboard'

urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<int:item_id>/', views.detail, name='detail'),
    path('add/', views.add, name='add'),
]
