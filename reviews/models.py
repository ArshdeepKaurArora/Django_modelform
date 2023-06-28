from django.db import models

# Create your models here.

class Reviews(models.Model):
    """Table for collecting reviews from users"""
    username = models.CharField(max_length=100)
    review_text = models.TextField()
    rating = models.IntegerField()