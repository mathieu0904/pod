from django.db import models



# Create your models here.


class Custommer(models.Model):
    id = models.AutoField( primary_key=True )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    contact = models.CharField(max_length=100)
    address = models.CharField(max_length=100)

    def __str__(self):
        return '%s' % (self.last_name)

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    designation = models.CharField(max_length=30)

    def __str__(self):
        return '%s' % (self.designation)

class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    designation = models.CharField(max_length=30)

    def __str__(self):
        return '%s' % (self.designation)

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    designation = models.CharField(max_length=50)
    price = models.FloatField(default=0)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE)

    def __str__(self):
        return '%s' % (self.designation)
    

class Order(models.Model):
    id = models.AutoField( primary_key=True )
    quantity = models.IntegerField()
    products = models.ForeignKey(Product,on_delete=models.CASCADE)
    custommer = models.ForeignKey(Custommer,on_delete=models.CASCADE)


