from django.urls import path
from . import views
from django.urls import re_path

app_name = "myapp"
urlpatterns = [
    path('datetime/', views.current_datetime),
    path('multiplication/', views.multiplication_table),
    path('programmer_day/', views.programmer_day),
    path('', views.home, name='home'),  
    path('news/', views.news, name='news'),
    path('management/', views.management, name='management'),
    path('facts/', views.facts, name='facts'),
    path('contacts/', views.contacts, name='contacts'),
    re_path(r'^news(?:/.+)?/$', views.news, name='news'),
    re_path(r'^management(?:/.+)?/$', views.management, name='management'),
    re_path(r'^facts(?:/.+)?/$', views.facts, name='facts'),
    re_path(r'^contacts(?:/.+)?/$', views.contacts, name='contacts'),
    path('history/', views.history, name='history'),
    path('history/people/', views.history_people, name='history_people'),
    path('history/photos/', views.history_photos, name='history_photos'),
]