from django.db import models
from PIL import Image

# Create your models here.
class My_Cars(models.Model):

    Name = models.CharField(max_length=100)
    Title_Price = models.CharField(max_length=100)
    Description = models.TextField(default=" ")
    Image = models.ImageField(upload_to='rohan/', default='rohandjango/rohan/static/img.jpg')
    inside_car = models.ImageField(upload_to='rohan/',default='rohandjango/rohan/static/img.jpg')
    backside_car= models.ImageField(upload_to='rohan/',default='rohandjango/rohan/static/img.jpg')



    def __str__(self):
        return self.Name