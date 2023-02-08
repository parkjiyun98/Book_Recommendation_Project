from django.db import models

# Create your models here.

class FiveKeyword(models.Model):
    name = models.CharField(max_length=100)
    five_keyword = models.CharField(max_length=100)

class FiveKeyword2(models.Model):
    name = models.CharField(max_length=50)
    five_keyword1 = models.CharField(max_length=10)
    five_keyword2 = models.CharField(max_length=10)
    five_keyword3 = models.CharField(max_length=10)
    five_keyword4 = models.CharField(max_length=10)
    five_keyword5 = models.CharField(max_length=10)

class FiveKeyword3(models.Model):
    name = models.CharField(max_length=30)
    five_keyword = models.CharField(max_length=50)
    five_keyword1 = models.CharField(max_length=10)
    five_keyword2 = models.CharField(max_length=10)
    five_keyword3 = models.CharField(max_length=10)
    five_keyword4 = models.CharField(max_length=10)
    five_keyword5 = models.CharField(max_length=10)

class FiveKeyword4(models.Model):
    name = models.CharField(max_length=30)
    five_keyword = models.CharField(max_length=50)
    five_keyword1 = models.CharField(max_length=10)
    five_keyword2 = models.CharField(max_length=10)
    five_keyword3 = models.CharField(max_length=10)
    five_keyword4 = models.CharField(max_length=10)
    five_keyword5 = models.CharField(max_length=10)
