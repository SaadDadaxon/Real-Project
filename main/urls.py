from django.urls import path
from .views import index, investor, project_views, service_views, solution_views

app_name = 'main'

urlpatterns = [
    path('index/', index, name='index'),
    path('investor/', investor, name='investor'),
    path('project/', project_views, name='project'),
    path('service/', service_views, name='service'),
    path('solution/', solution_views, name='solution'),

]
