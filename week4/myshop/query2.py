from shop.models import *
products = Product.objects.filter(description__endswith="features.")
for i in products:
    print("PRODUCT ID:%d, DESCRIPTION: %s"%(i.id, i.description))