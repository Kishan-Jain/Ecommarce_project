from django.contrib import admin
from homepage.models import offer_nav
from homepage.models import categories

# Register your models here.

class offer_nav_admin(admin.ModelAdmin):
    list_display=('offer_title','offer_disc')
    
class categories_admin(admin.ModelAdmin):
    list_display=('title','disc','image')
    
admin.site.register(offer_nav, offer_nav_admin)
admin.site.register(categories, categories_admin)