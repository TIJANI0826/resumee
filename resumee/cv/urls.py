from . import views
from django.urls import path
app_name = 'cv'
urlpatterns =[
    path('home', views.index,name = 'home'),
]