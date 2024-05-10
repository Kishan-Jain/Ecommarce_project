from django.contrib import admin
from .models import antiqe, buety_product, daily_uses, divices, fashion, gerociry, kitchen_goods, leptop ,luxury, mobiles, stationary

# Register your models here.

class fashion_admin(admin.ModelAdmin):
    list_display=('product_title', 'product_brand', 'product_MRP', 'discount', 'price','slug')   

class buety_product_admin(admin.ModelAdmin):
    list_display=('product_title', 'product_brand', 'product_MRP', 'discount', 'price','slug')
    
class divices_admin(admin.ModelAdmin):
    list_display=('product_title', 'product_brand', 'product_MRP', 'discount', 'price','slug')
    
class leptop_admin(admin.ModelAdmin):
    list_display=('product_title', 'product_brand', 'product_MRP', 'discount', 'price','slug')
    
class mobiles_admin(admin.ModelAdmin):
    list_display=('product_title', 'product_brand', 'product_MRP', 'discount', 'price','slug')
 
class daily_uses_admin(admin.ModelAdmin):
    list_display=('product_title', 'product_brand', 'product_MRP', 'discount', 'price','slug')
       
class gerociry_admin(admin.ModelAdmin):
    list_display=('product_title', 'product_brand', 'product_MRP', 'discount', 'price','slug')

class stationary_admin(admin.ModelAdmin):
    list_display=('product_title', 'product_brand', 'product_MRP', 'discount', 'price','slug')
       
class kitchen_goods_admin(admin.ModelAdmin):
    list_display=('product_title', 'product_brand', 'product_MRP', 'discount', 'price','slug')
    
class luxury_admin (admin.ModelAdmin):
    list_display=('product_title', 'product_brand', 'product_MRP', 'discount', 'price','slug')
    
class antiqe_admin(admin.ModelAdmin):
    list_display=('product_title', 'product_brand', 'product_MRP', 'discount', 'price','slug')
    
    

admin.site.register(fashion, fashion_admin )
admin.site.register(buety_product, buety_product_admin)
admin.site.register(divices, divices_admin )
admin.site.register(mobiles, mobiles_admin )
admin.site.register(leptop, leptop_admin )
admin.site.register(daily_uses, daily_uses_admin )
admin.site.register(gerociry, gerociry_admin )
admin.site.register(kitchen_goods, kitchen_goods_admin )
admin.site.register(stationary, stationary_admin )
admin.site.register(luxury, luxury_admin)
admin.site.register(antiqe, antiqe_admin)
