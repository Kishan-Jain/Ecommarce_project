from django.contrib import admin
from homepage.models import Offer_Nav
from homepage.models import Categories

# Register your models here.

class Offer_Nav_admin(admin.ModelAdmin):
    list_display=('offer_title','offer_disc')
    
class Categories_admin(admin.ModelAdmin):
    list_display=('title','disc','links')
    
admin.site.register(Offer_Nav, Offer_Nav_admin)
admin.site.register(Categories, Categories_admin)