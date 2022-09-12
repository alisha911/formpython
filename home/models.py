from django.db import models

# Create your models here.
class Students(models.Model):
    student_id = models.IntegerField()
    name= models.CharField(max_length=20)
    phone = models.IntegerField()
    email = models.CharField(max_length=20)