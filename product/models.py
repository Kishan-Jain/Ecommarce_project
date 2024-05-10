from django.db import models
from tinymce.models import HTMLField
from autoslug import AutoSlugField

# Create your models here.
class fashion(models.Model):
    product_title = models.CharField(max_length=100)
    product_brand = models.CharField(max_length=100, default="", null= True)
    product_MRP = models.IntegerField()
    discount = models.IntegerField()
    def price(self):
        return self.product_MRP * (self.discount /100)
    product_pic = models.FileField(upload_to="product/fashion", default=" ", null= True, )
    pro_disc = HTMLField()
    slug = AutoSlugField(default=None , populate_from ='product_title', unique=True, null=True)  
    
   
class buety_product(models.Model):
    product_title = models.CharField(max_length=100)
    product_brand = models.CharField(max_length=100, default="", null= True)
    product_MRP = models.IntegerField()
    discount = models.IntegerField()
    def price(self):
        return self.product_MRP * (self.discount /100)
    product_pic = models.FileField(upload_to="product/buety_product", default=" ", null= True, )
    pro_disc = HTMLField()
    slug = AutoSlugField(default=None , populate_from ='product_title', unique=True, null=True)
    
class divices(models.Model):
    product_title = models.CharField(max_length=100)
    product_brand = models.CharField(max_length=100, default="", null= True)
    product_MRP = models.IntegerField()
    discount = models.IntegerField()
    def price(self):
        return self.product_MRP * (self.discount /100)
    product_pic = models.FileField(upload_to="product/divices", default=" ", null= True, )
    pro_disc = HTMLField()
    slug = AutoSlugField(default=None , populate_from ='product_title', unique=True, null=True)
    
class mobiles(models.Model):
    product_title = models.CharField(max_length=100)
    product_brand = models.CharField(max_length=100, default="", null= True)
    product_MRP = models.IntegerField()
    discount = models.IntegerField()
    def price(self):
        return self.product_MRP * (self.discount /100)
    product_pic = models.FileField(upload_to="product/mobiles", default=" ", null= True, )
    pro_disc = HTMLField()
    slug = AutoSlugField(default=None , populate_from ='product_title', unique=True, null=True)
    
class leptop(models.Model):
    product_title = models.CharField(max_length=100)
    product_brand = models.CharField(max_length=100, default="", null= True)
    product_MRP = models.IntegerField()
    discount = models.IntegerField()
    def price(self):
        return self.product_MRP * (self.discount /100)
    product_pic = models.FileField(upload_to="product/leptop", default=" ", null= True, )
    pro_disc = HTMLField()
    slug = AutoSlugField(default=None , populate_from ='product_title', unique=True, null=True)
    
class daily_uses(models.Model):
    product_title = models.CharField(max_length=100)
    product_brand = models.CharField(max_length=100, default="", null= True)
    product_MRP = models.IntegerField()
    discount = models.IntegerField()
    def price(self):
        return self.product_MRP * (self.discount /100)
    product_pic = models.FileField(upload_to="product/daily_uses", default=" ", null= True, )
    pro_disc = HTMLField()
    slug = AutoSlugField(default=None , populate_from ='product_title', unique=True, null=True)
    
class gerociry(models.Model):
    product_title = models.CharField(max_length=100)
    product_brand = models.CharField(max_length=100, default="", null= True)
    product_MRP = models.IntegerField()
    discount = models.IntegerField()
    def price(self):
        return self.product_MRP * (self.discount /100)
    product_pic = models.FileField(upload_to="product/gerociry", default=" ", null= True, )
    pro_disc = HTMLField()
    slug = AutoSlugField(default=None , populate_from ='product_title', unique=True, null=True)
    
class stationary(models.Model):
    product_title = models.CharField(max_length=100)
    product_brand = models.CharField(max_length=100, default="", null= True)
    product_MRP = models.IntegerField()
    discount = models.IntegerField()
    def price(self):
        return self.product_MRP * (self.discount /100)
    product_pic = models.FileField(upload_to="product/stationary", default=" ", null= True, )
    pro_disc = HTMLField()
    slug = AutoSlugField(default=None , populate_from ='product_title', unique=True, null=True)
    
class kitchen_goods(models.Model):
    product_title = models.CharField(max_length=100)
    product_brand = models.CharField(max_length=100, default="", null= True)
    product_MRP = models.IntegerField()
    discount = models.IntegerField()
    def price(self):
        return self.product_MRP * (self.discount /100)
    product_pic = models.FileField(upload_to="product/kitchen_goods", default=" ", null= True, )
    pro_disc = HTMLField()
    slug = AutoSlugField(default=None , populate_from ='product_title', unique=True, null=True)
    
class luxury(models.Model):
    product_title = models.CharField(max_length=100)
    product_brand = models.CharField(max_length=100, default="", null= True)
    product_MRP = models.IntegerField()
    discount = models.IntegerField()
    def price(self):
        return self.product_MRP * (self.discount /100)
    product_pic = models.FileField(upload_to="product/luxury", default=" ", null= True, )
    pro_disc = HTMLField()
    slug = AutoSlugField(default=None , populate_from ='product_title', unique=True, null=True)
    
class antiqe(models.Model):
    product_title = models.CharField(max_length=100)
    product_brand = models.CharField(max_length=100, default="", null= True)
    product_MRP = models.IntegerField()
    discount = models.IntegerField()
    def price(self):
        return self.product_MRP * (self.discount /100)
    product_pic = models.FileField(upload_to="product/antiqe", default=" ", null= True, )
    pro_disc = HTMLField()
    slug = AutoSlugField(default=None , populate_from ='product_title', unique=True, null=True)
     