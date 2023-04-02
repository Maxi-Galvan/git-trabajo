from django.db import models

# Create your models here.
class Post(models.Model):
    carosuel_caption_title = models.CharField(max_length=30)
    carosuel_caption_description = models.CharField(max_length=30)
    heading = models.CharField(max_length=12)
    description = models.CharField(max_length=120)

    def __str__(self):
        return f"{self.id} - {self.heading}"