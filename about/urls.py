from django.urls import path
from .views import about_views

app_name = 'about'

urlpatterns = [
    path('index/', about_views, name='index')
]
