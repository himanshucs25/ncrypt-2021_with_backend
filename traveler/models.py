from django.db import models
# Create your models here.
class Place(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField()
    price=models.IntegerField()
    image_main=models.ImageField(upload_to='photos/')
    image_sec=models.ImageField(upload_to='photos/')

    def __str__(self):
        return self.name
