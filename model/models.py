from django.db import models

# Create your models here.
class user(models.Model):
    Name = models.CharField(null=False, max_length=20)
    Email = models.EmailField(null=False,primary_key=True)
    Password = models.CharField(null=False, max_length=100)


    def __str__(self):
        return self.name,self.email

class predicted(models.Model):
    Id = models.AutoField(primary_key=True,null=False)
    Name = models.CharField(null=False, max_length=20)
    Email = models.EmailField(null=False)
    Age = models.IntegerField(null=False)
    Gender = models.CharField(null=False, max_length=10)
    Stream = models.CharField(null=False,max_length=30)
    NumberOfInternships = models.IntegerField(null=False)
    CGPA = models.IntegerField(null=False)
    Backlogs = models.IntegerField(null=False)
    Prediction = models.CharField(null=False, max_length=10)
