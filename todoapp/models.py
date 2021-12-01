from django.db import models
from django.urls import reverse


class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    is_completed = models.BooleanField(default=False)
    date_created = models.DateField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('detail', args=[str(self.id)])
