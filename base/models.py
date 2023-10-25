from django.db import models

class Product(models.Model):
    desc = models.CharField(max_length=50,null=True,blank=True)
    price = models.DecimalField(max_digits=5,decimal_places=2)
    cat_id=models.IntegerField()
    fields =['desc','price']
 
    def __str__(self):
           return self.desc

# Create your models here.
