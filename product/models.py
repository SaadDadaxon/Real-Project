from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=228)

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=228)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='image')
    price = models.DecimalField(decimal_places=2, max_digits=4, null=True, blank=True)

    def __str__(self):
        return self.title


class SubImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='sub_image')
    image = models.ImageField(upload_to='sub_image/')


class Description(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name='description')
    text = models.TextField()


class Characteristic(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name='characteristic')
    tip_model = models.CharField(max_length=228)
    test_conditions = models.CharField(max_length=228)
    maximum_power = models.CharField(max_length=228)
    voltage = models.CharField(max_length=228)
    voltage_maximum = models.CharField(max_length=228)




