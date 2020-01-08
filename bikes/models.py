from django.db import models
from django.utils import timezone


class Bike(models.Model):
    """
    A single Bike post
    """
    name = models.CharField(max_length=200, default="")
    price = models.DecimalField(max_digits=6 , decimal_places=2, default="100.00")
    description = models.TextField()
    image = models.ImageField(upload_to="img", blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    views = models.IntegerField(default=0)
    tag = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.name