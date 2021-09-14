from django.db import models

# Create your models here.

class Owner(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=300)
    age = models.IntegerField(null=True)

    class Meta:
        db_table = 'owner'

class Dog(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField(null=True)
    owner = models.ForeignKey('Owner', on_delete=models.CASCADE)

    class Meta:
        db_table = 'dogs'