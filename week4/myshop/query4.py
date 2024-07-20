from shop.models import *
products = Product.objects.filter(price__lt=200, price__gt=100)
for i in products:
    print("PRODUCT ID:%d, NAME: %s, PRICE: %.2f"%(i.id, i.name, i.price))