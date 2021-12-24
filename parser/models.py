from django.db import models


class Film(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='anime/')

    def __str__(self):
        return f'{self.title}'


class Smartphone(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='smartphone/')
    price = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.title}'
