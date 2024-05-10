from django.shortcuts import render
from product.models import antiqe, buety_product, daily_uses, divices, fashion, gerociry, kitchen_goods, leptop ,luxury, mobiles, stationary

# Create your views here.

# def cat_base_page(request):
#     antiqeitem =antiqe.objects.all()
#     buety_productitem = buety_product.objects.all()
#     daily_usesitem = daily_uses.objects.all()
#     divicesitem = divices.objects.all()
#     fashionitem = fashion.objects.all()
#     gerociryitem = gerociry.objects.all()
#     kitchen_goodsitem = kitchen_goods.objects.all()
#     leptopitem = leptop.objects.all() 
#     luxuryitem = luxury.objects.all()
#     mobilesitem = mobiles.objects.all()
#     stationaryitem = stationary.objects.all()

#     data = {
#         'antiqeitem' : antiqeitem,
#         'buety_productitem' : buety_productitem,
#         'daily_usesitem' : daily_usesitem,
#         'divicesitem' : divicesitem,
#         'fashionitem' : fashionitem,
#         'gerociryitem' : gerociryitem,
#         'kitchen_goodsitem': kitchen_goodsitem,
#         'leptopitem' : leptopitem,
#         'luxuryitem' : luxuryitem,
#         'mobilesitem' : mobilesitem,
#         'stationaryitem' : stationaryitem,

#     }
     
#     return render(request, "cat_base_page.html", data)

