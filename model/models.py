from django.db import models

# Create your models here.
class user(models.Model):
    Name = models.CharField(null=False, max_length=20)
    Email = models.EmailField(null=False,primary_key=True)
    Password = models.CharField(null=False, max_length=100)


    def __str__(self):
        return self.name,self.email

class predicted(models.Model):
    Name = models.CharField(null=False, max_length=20)
    Email = models.EmailField(null=False,primary_key=True)
    Tenthmarks = models.IntegerField(null=False)
    Twelthmarks = models.IntegerField(null=False)
    CETmarks = models.IntegerField(null=False)
    AggOfAllSem = models.IntegerField(null=False)
    NumberOfInternships = models.IntegerField(null=False)
    ReadyToRelocate = models.BooleanField(null=False)
    Python = models.CharField(null=False, max_length=20)
    WebDevelopment = models.CharField(null=False, max_length=20)
