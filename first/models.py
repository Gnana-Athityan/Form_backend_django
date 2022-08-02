from django.db import models

# Create your models here.

class Contact(models.Model):
    name=models.CharField( max_length=50)
    age=models.CharField(max_length = 50)
    know=models.TextField()
    review=models.TextField()
    date=models.DateTimeField( auto_now=False, auto_now_add=False)


    def __str__(self):
        return self.name




