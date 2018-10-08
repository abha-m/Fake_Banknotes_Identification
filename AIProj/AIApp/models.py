from django.db import models

# Create your models here.

class UploadImg(models.Model):
   # name = models.CharField(max_length = 50)
   picture = models.ImageField(upload_to = 'Uploaded')


