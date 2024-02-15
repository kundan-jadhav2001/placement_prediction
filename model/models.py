from django.db import models

# Create your models here.
class user(models.Model):
    Name = models.CharField(null=False, max_length=20)
    Email = models.EmailField(null=False,primary_key=True)
    Password = models.CharField(null=False, max_length=100)


    def __str__(self):
        return self.name,self.email
