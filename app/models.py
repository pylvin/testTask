from django.db import models

# Create your models here.
class Link(models.Model):
    active = models.BooleanField(default=False)
    response = models.BooleanField(default=False)
    interval = models.PositiveIntegerField(default=60)
    link = models.URLField()
    class Meta:
        verbose_name = "Link"
        verbose_name_plural = "Link"
    def __str__(self):
        return f"Link: {self.link}"