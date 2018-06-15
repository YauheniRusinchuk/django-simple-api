from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100, blank=False)
    body = models.TextField(blank=False)
    date = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-date']
    def __str__(self):
        return self.title
