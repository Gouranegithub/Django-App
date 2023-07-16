from django.db import models

from django.utils import timezone
from django.contrib.auth.models import User

from django.urls import reverse  #not like redirect it just return the url as a string for the viewor whatever
class POST(models.Model):
    title = models.CharField(max_length= 100)
    content = models.TextField()
    date=models.DateTimeField(default =timezone.now)
    author = models.ForeignKey( User , on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})