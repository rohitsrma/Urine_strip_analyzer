from django.db import models

# Create your models here.
class UrineStrip(models.Model):
    image = models.ImageField(upload_to='images/')
    upload_datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image uploaded on {self.upload_datetime}"