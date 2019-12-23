from django.db import models


# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=30)
    desg = models.CharField(max_length=20, null=True)
    salary = models.IntegerField()

    def __str__(self):
        return self.name + "," + self.desg + "," + str(self.salary)

