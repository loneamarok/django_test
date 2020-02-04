from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Router(models.Model):
    router_name = models.CharField(max_length=100)
    router_ip = models.CharField(max_length=100)
    router_apps = ArrayField(models.CharField(max_length=100))
