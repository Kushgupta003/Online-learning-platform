from django.db import models

# Create your models here.
class News(models.Model):
    title=models.CharField(max_length=20,unique=True)
    desc=models.CharField(max_length=500)

class Session(models.Model):
    session=models.CharField(max_length=10)

class Branch(models.Model):
    branch=models.CharField(max_length=40)

class Course(models.Model):
    course=models.CharField(max_length=20)

class Study(models.Model):
    course=models.CharField(max_length=30)
    branch=models.CharField(max_length=30)
    session=models.CharField(max_length=30)
    subject=models.CharField(max_length=30)
    file_name=models.CharField(max_length=30)
    file=models.FileField(max_length=255,upload_to="study")