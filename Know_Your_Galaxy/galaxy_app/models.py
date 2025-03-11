from django.db import models

# Create your models here.
class Review(models.Model):
    firstname= models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    address= models.CharField(max_length=150)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    desc = models.TextField()

    def __str__(self):
        return self.firstname
    
