from django.shortcuts import render
from rest_framework import generics
from .serializer import ContactSerializer
from contact.models import Contact


class ContactListCreate(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

