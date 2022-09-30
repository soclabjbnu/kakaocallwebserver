from django.db import models

# Create your models here.
class Person(models.Model):
    first = models.CharField(max_length=32)
    last = models.CharField(max_length=32)
    born = models.CharField(max_length=32)


    def __str__(self):
        return '{0}:{1}:{2}'.format(self.first, self.last, self.born)