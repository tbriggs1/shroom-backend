from django.db import models

class Mushrooms(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=40, blank=True, default='')
    user = models.CharField(max_length=40, blank=True, default='')

    class Meta:
        ordering = ['created']