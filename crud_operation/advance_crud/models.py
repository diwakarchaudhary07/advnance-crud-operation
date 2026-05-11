from django.db import models


class Student(models.Model):

    name = models.CharField(max_length=100,blank=True,null=True)

    email = models.EmailField(blank=True,null=True)

    age = models.IntegerField(blank=True,null=True)

    city = models.CharField(max_length=100,blank=True,null=True)

    contact_no = models.CharField(max_length=10,blank=True,null=True)

    def __str__(self):
        return self.name if self.name else "No Name"