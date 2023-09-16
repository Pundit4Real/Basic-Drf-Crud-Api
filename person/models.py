from django.db import models

# persons class..
class Person(models.Model):
    name = models.CharField(max_length=100, default='')
    country = models.CharField(max_length=50,default='')
    stack = models.CharField(max_length=30,default='')
    added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name