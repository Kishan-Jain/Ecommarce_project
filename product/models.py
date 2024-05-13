from django.db import models
from tinymce.models import HTMLField
from autoslug import AutoSlugField

# Create your models here.
class Fashion(models.Model):
    product_title = models.CharField(max_length=100)
    product_brand = models.CharField(max_length=100, default="", null= True)
    product_MRP = models.IntegerField()
    discount = models.IntegerField()
    def price(self):
        totalPrice = str(self.product_MRP * (1-(self.discount /100))).split(".")
        prices = float(totalPrice[0] +"." + totalPrice[1][:2])
        
        return prices
    product_pic = models.FileField(upload_to="product/fashion", default=" ", null= True, )
    pro_disc = HTMLField()
    slug = AutoSlugField(default=None , populate_from ='product_title', unique=True, null=True)  
    
   
class Buety_Product(models.Model):
    product_title = models.CharField(max_length=100)
    product_brand = models.CharField(max_length=100, default="", null= True)
    product_MRP = models.IntegerField()
    discount = models.IntegerField()
    def price(self):
        return self.product_MRP * (self.discount /100)
    product_pic = models.FileField(upload_to="product/buety_product", default=" ", null= True, )
    pro_disc = HTMLField()
    slug = AutoSlugField(default=None , populate_from ='product_title', unique=True, null=True)
    
class Divices(models.Model):
    product_title = models.CharField(max_length=100)
    product_brand = models.CharField(max_length=100, default="", null= True)
    product_MRP = models.IntegerField()
    discount = models.IntegerField()
    def price(self):
        return self.product_MRP * (self.discount /100)
    product_pic = models.FileField(upload_to="product/divices", default=" ", null= True, )
    pro_disc = HTMLField()
    slug = AutoSlugField(default=None , populate_from ='product_title', unique=True, null=True)
    
class Mobiles(models.Model):
    product_title = models.CharField(max_length=100)
    product_brand = models.CharField(max_length=100, default="", null= True)
    product_MRP = models.IntegerField()
    discount = models.IntegerField()
    def price(self):
        return self.product_MRP * (self.discount /100)
    product_pic = models.FileField(upload_to="product/mobiles", default=" ", null= True, )
    pro_disc = HTMLField()
    slug = AutoSlugField(default=None , populate_from ='product_title', unique=True, null=True)
    
class Leptop(models.Model):
    product_title = models.CharField(max_length=100)
    product_brand = models.CharField(max_length=100, default="", null= True)
    product_MRP = models.IntegerField()
    discount = models.IntegerField()
    def price(self):
        return self.product_MRP * (self.discount /100)
    product_pic = models.FileField(upload_to="product/leptop", default=" ", null= True, )
    pro_disc = HTMLField()
    slug = AutoSlugField(default=None , populate_from ='product_title', unique=True, null=True)
    
class Daily_Uses(models.Model):
    product_title = models.CharField(max_length=100)
    product_brand = models.CharField(max_length=100, default="", null= True)
    product_MRP = models.IntegerField()
    discount = models.IntegerField()
    def price(self):
        return self.product_MRP * (self.discount /100)
    product_pic = models.FileField(upload_to="product/daily_uses", default=" ", null= True, )
    pro_disc = HTMLField()
    slug = AutoSlugField(default=None , populate_from ='product_title', unique=True, null=True)
    
class Gerociry(models.Model):
    product_title = models.CharField(max_length=100)
    product_brand = models.CharField(max_length=100, default="", null= True)
    product_MRP = models.IntegerField()
    discount = models.IntegerField()
    def price(self):
        return self.product_MRP * (self.discount /100)
    product_pic = models.FileField(upload_to="product/gerociry", default=" ", null= True, )
    pro_disc = HTMLField()
    slug = AutoSlugField(default=None , populate_from ='product_title', unique=True, null=True)
    
class Stationary(models.Model):
    product_title = models.CharField(max_length=100)
    product_brand = models.CharField(max_length=100, default="", null= True)
    product_MRP = models.IntegerField()
    discount = models.IntegerField()
    def price(self):
        return self.product_MRP * (self.discount /100)
    product_pic = models.FileField(upload_to="product/stationary", default=" ", null= True, )
    pro_disc = HTMLField()
    slug = AutoSlugField(default=None , populate_from ='product_title', unique=True, null=True)
    
class Kitchen_Goods(models.Model):
    product_title = models.CharField(max_length=100)
    product_brand = models.CharField(max_length=100, default="", null= True)
    product_MRP = models.IntegerField()
    discount = models.IntegerField()
    def price(self):
        return self.product_MRP * (self.discount /100)
    product_pic = models.FileField(upload_to="product/kitchen_goods", default=" ", null= True, )
    pro_disc = HTMLField()
    slug = AutoSlugField(default=None , populate_from ='product_title', unique=True, null=True)
    
class Luxury(models.Model):
    product_title = models.CharField(max_length=100)
    product_brand = models.CharField(max_length=100, default="", null= True)
    product_MRP = models.IntegerField()
    discount = models.IntegerField()
    def price(self):
        return self.product_MRP * (self.discount /100)
    product_pic = models.FileField(upload_to="product/luxury", default=" ", null= True, )
    pro_disc = HTMLField()
    slug = AutoSlugField(default=None , populate_from ='product_title', unique=True, null=True)
    
class Antiqe(models.Model):
    product_title = models.CharField(max_length=100)
    product_brand = models.CharField(max_length=100, default="", null= True)
    product_MRP = models.IntegerField()
    discount = models.IntegerField()
    def price(self):
        return self.product_MRP * (self.discount /100)
    product_pic = models.FileField(upload_to="product/antiqe", default=" ", null= True, )
    pro_disc = HTMLField()
    slug = AutoSlugField(default=None , populate_from ='product_title', unique=True, null=True)
     