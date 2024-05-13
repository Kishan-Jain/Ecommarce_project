from django.contrib import admin
from .models import Antiqe, Buety_Product, Daily_Uses, Divices, Fashion, Gerociry, Kitchen_Goods, Leptop ,Luxury, Mobiles, Stationary


# Register your models here.

class Fashion_admin(admin.ModelAdmin):
    list_display=('product_title', 'product_brand', 'product_MRP', 'discount', 'price','slug')   

class Buety_Product_admin(admin.ModelAdmin):
    list_display=('product_title', 'product_brand', 'product_MRP', 'discount', 'price','slug')
    
class Divices_admin(admin.ModelAdmin):
    list_display=('product_title', 'product_brand', 'product_MRP', 'discount', 'price','slug')
    
class Leptop_admin(admin.ModelAdmin):
    list_display=('product_title', 'product_brand', 'product_MRP', 'discount', 'price','slug')
    
class Mobiles_admin(admin.ModelAdmin):
    list_display=('product_title', 'product_brand', 'product_MRP', 'discount', 'price','slug')
 
class Daily_Uses_admin(admin.ModelAdmin):
    list_display=('product_title', 'product_brand', 'product_MRP', 'discount', 'price','slug')
       
class Gerociry_admin(admin.ModelAdmin):
    list_display=('product_title', 'product_brand', 'product_MRP', 'discount', 'price','slug')

class Stationary_admin(admin.ModelAdmin):
    list_display=('product_title', 'product_brand', 'product_MRP', 'discount', 'price','slug')
       
class Kitchen_Goods_admin(admin.ModelAdmin):
    list_display=('product_title', 'product_brand', 'product_MRP', 'discount', 'price','slug')
    
class Luxury_admin (admin.ModelAdmin):
    list_display=('product_title', 'product_brand', 'product_MRP', 'discount', 'price','slug')
    
class Antiqe_admin(admin.ModelAdmin):
    list_display=('product_title', 'product_brand', 'product_MRP', 'discount', 'price','slug')
    
    

admin.site.register(Fashion, Fashion_admin )
admin.site.register(Buety_Product, Buety_Product_admin)
admin.site.register(Divices, Divices_admin )
admin.site.register(Mobiles, Mobiles_admin )
admin.site.register(Leptop, Leptop_admin )
admin.site.register(Daily_Uses, Daily_Uses_admin )
admin.site.register(Gerociry, Gerociry_admin )
admin.site.register(Kitchen_Goods, Kitchen_Goods_admin )
admin.site.register(Stationary, Stationary_admin )
admin.site.register(Luxury, Luxury_admin)
admin.site.register(Antiqe, Antiqe_admin)
