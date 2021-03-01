from django.db import models
# Create your models here.

def upload_image_product(instance,filename):
    return f"{instance.id}-{filename}"

class Products(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(decimal_places=2,max_digits=10)
    image_url = models.ImageField(upload_to=upload_image_product,blank=True, null=True)