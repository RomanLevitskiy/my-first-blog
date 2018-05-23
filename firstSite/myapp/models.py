from django.db import models

# Create your models here.

class myapp(models.Model):
	primKey = models.AutoField(primary_key=True)
	dataCreating = models.DateField(auto_now_add=True)
	dataLastModifaed = models.DateField(auto_now=True)
	autor = models.CharField(max_length=128)
	textMessage = models.CharField(max_length=1024)
