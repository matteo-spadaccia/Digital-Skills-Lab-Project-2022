from django.db import models

# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, default='')
    image = models.ImageField(default= 'logo_luiss.png')

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, default='')
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Event(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, default='')
    department  = models.ForeignKey(Department, on_delete=models.CASCADE, default=None, null=True)
    image = models.ImageField(default= 'logo_luiss.png')
    datetime = models.DateTimeField(default=None, null=True)

    def __str__(self):
        return self.name