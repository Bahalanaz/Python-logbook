from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()

class Student(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()

class People(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()