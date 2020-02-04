from django.db import models

# Create your models here.
class App(models.Model):
    app_name = models.CharField(max_length=100)
    app_disc = models.CharField
    app_version = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    docker_image = models.FileField(upload_to='docker_images/')
    datetime = models.DateTimeField()