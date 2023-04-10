from django.urls import path
from .views import ContactListCreate

urlpatterns = [
    path('contact-list-create/', ContactListCreate.as_view())
]
