from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),  # Список задач
    path('create/', views.task_create, name='task_create'),  # Создание задачи
    re_path(r'^edit/(?P<task_id>\d+)/$', views.task_edit, name='task_edit'),  # Редактирование задачи
    re_path(r'^delete/(?P<task_id>\d+)/$', views.task_delete, name='task_delete'),  # Удаление задачи
    re_path(r'^detail/(?P<task_id>\d+)/$', views.task_detail, name='task_detail'),  # Детали задачи
    re_path(r'^status/(?P<task_id>\d+)/$', views.task_status, name='task_status'),  # Обновление статуса задачи
    path('search/', views.task_search, name='task_search'),  # Поиск задач
    re_path(r'^filter/(?P<filter_type>\w+)/$', views.task_filter, name='task_filter'),  # Фильтрация задач
    path('export/', views.task_export, name='task_export'),  # Экспорт задач
    path('import/', views.task_import, name='task_import'),  # Импорт задач
]
