from django.db import models
from django.db.models import Count
from django.core.validators import MaxValueValidator, MinValueValidator

class Category(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name

class Post(models.Model):
    PURCHASE_CHOICES = (
            ('T1', 'Type1 $7,800'),
            ('T2', 'Type2 $10,000'), 
            ) 
    title = models.CharField(max_length=255)
    totalfund = models.CharField(max_length=20, null = True, blank = True)
    def __str__(self):
        return self.totalfund
    body = models.TextField()
    purchasetype = models.CharField(max_length= 60, choices=PURCHASE_CHOICES, null = True) 
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField('Category', related_name='posts')
    images = models.ImageField(upload_to ='blog/images', max_length = 550, null = True, blank = True)
    def __str__(self):
        return self.title

class Order(models.Model):
    #PURCHASE_CHOICES = (
    #        ('T1', 'Type1 $7,800'),
    #        ('T2', 'Type2 $10,000'), 
    #        )
    author = models.CharField(max_length = 60)
    #purchasetype = models.CharField(max_length= 60, choices=PURCHASE_CHOICES, null = True)
    option = models.CharField(max_length = 60, null = True)
    quantity = models.IntegerField(validators = [MinValueValidator(1), MaxValueValidator(10)])
    email = models.CharField(max_length = 60, null = True, blank = False)
    phone = models.CharField(max_length = 120, null = False, blank = False)
    message_store = models.CharField(max_length=256)
    post = models.ForeignKey('Post', on_delete=models.CASCADE, null = True) #forDB
    created_on = models.DateTimeField(auto_now_add = True, null = True)

#class Comment(models.Model):
#    author = models.CharField(max_length=60)
#    body = models.TextField()
#    created_on = models.DateTimeField(auto_now_add=True)
#    post = models.ForeignKey('Post', on_delete=models.CASCADE)
#    def __str__(self):
#        return self.body

# Create your models here.
