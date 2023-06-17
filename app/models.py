from django.db import models

# Create your models here.


class Product_Category(models.Model):
    pcid=models.PositiveIntegerField()
    pcname=models.CharField(max_length=100)


    def __str__(self):
        return self.pcname

class Product(models.Model):
    pcname=models.ForeignKey(Product_Category,on_delete=models.CASCADE)
    pname=models.CharField(max_length=100)
    pid=models.PositiveIntegerField()
    price=models.DecimalField(max_digits=7,decimal_places=2)
    descrption=models.TextField()
    date=models.DateField()

    def __str__(self):
        return self.pname

