from django.db import models

# Create your models here.

class student(models.Model):
    name=models.CharField(max_length=40)
    age=models.IntegerField()
    email=models.EmailField(max_length=40)
    password=models.CharField(max_length=40)

class ImageModel(models.Model):
    name=models.CharField(max_length=40)
    image=models.ImageField(upload_to="myimages")
    desc=models.TextField()
    date=models.DateTimeField(auto_now_add=True)


!