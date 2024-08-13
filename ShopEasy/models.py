from django.db import models


# Create your models here.
class Services(models.Model):
    icon = models.ImageField(upload_to='icons/')
    title = models.CharField(max_length=55)
    deteil = models.TextField()
    is_added = models.DateTimeField(auto_now=True)

class AboutMe(models.Model):
    title= models.CharField(max_length=255,default='value')
    f_nam = models.CharField(max_length=44,default='value') # bu yerda ismizi kiritasiz
    staff = models.CharField(max_length=44) # bu uerda siz kib bolas deganman maslan direktor 
