from django.db import models
STATUS=(('In Stock','In Stock'),('Out Stock','Out Stock'))
# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=200)
    slug=models.CharField(max_length=200,unique=True)
    image=models.CharField(max_length=200,blank=True)
    def __str__(self):
        return self.name

class Slider(models.Model):
    name=models.CharField(max_length=200)
    image=models.TextField(max_length=200)
    description=models.TextField(max_length=200)
    url=models.TextField(blank=True)

    def __str__(self):
        return self.name

class Ad(models.Model):
    name=models.CharField(max_length=300)
    rank=models.IntegerField(unique=True)
    image=models.TextField()
    description=models.TextField(blank=True)

    def __str__(self):
        return self.name

class Brand(models.Model):
    name=models.CharField(max_length=200)
    image=models.TextField(max_length=300)
    rank=models.IntegerField(unique=True)

    def __str__(self):
        return self.name

class Items(models.Model):
    title=models.CharField(max_length=300)
    name=models.CharField(max_length=300)
    price=models.IntegerField()
    slug=models.CharField(max_length=100,unique=True)
    discounted_price=models.IntegerField(default=0)
    description=models.TextField()
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    brand= models.ForeignKey(Brand, on_delete=models.CASCADE)
    status=models.CharField(max_length=50,choices=STATUS)

    def __str__(self):
        return self.title