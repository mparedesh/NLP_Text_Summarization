from django.db import models

# Create your models here.

class Contact(models.Model):
    email=models.CharField(max_length=122)
    text=models.TextField()
    date=models.DateField()

#This method will show email inplace of object in admin module
    def __str__(self):
        return self.email
