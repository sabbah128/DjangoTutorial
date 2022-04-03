from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updateed_date = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ('-created_date',)
    def __str__(self):
        return self.name

class Newsletter(models.Model):
    email = models.EmailField()    
    def __str__(self):
        return self.email