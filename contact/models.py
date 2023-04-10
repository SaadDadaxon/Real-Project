from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=228)
    phone = models.CharField(max_length=17)
    descriptions = models.CharField(max_length=228)

    def __str__(self):
        return self.name
