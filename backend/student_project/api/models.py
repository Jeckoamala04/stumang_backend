from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.TextField()
    image = models.ImageField(upload_to='students/')

    def __str__(self):
        return self.name
