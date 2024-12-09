from django.db import models

# Create your models here.
class MediaUpload(models.Model):
    title = models.TextField(null=True, blank=True)
    description = models.TextField(default="No description provided")
    media_file = models.FileField(null=True, blank=True)
    media_type = models.TextField(null=True, blank=True)
    upload_date = models.DateField(null=True, blank=True)