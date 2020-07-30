from django.db import models
from django.contrib.auth.models import User


class Recipe(models.Model):
    title = models.CharField(max_length=25)
    url = models.URLField()
    pub_date = models.DateTimeField()
    votes_total = models.IntegerField()
    image = models.ImageField()
    icon = models.ImageField()
    body = models.CharField(max_length=900)
    publisher = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100] + "..."
