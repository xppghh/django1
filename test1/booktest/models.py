from django.db import models

# Create your models here.

class student(models.Model):
    name=models.CharField(max_length=20)
    gender=models.BooleanField(default=True)
    age=models.IntegerField(default=0)
    isDelete=models.BooleanField(default=False)
    class Meta:
        db_table='student'
