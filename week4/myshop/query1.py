from shop.models import *
order = Order.objects.filter(order_date__month=5)[:10]
for i in order:
    print("ORDER ID:%d, DATE: %s, "%(i.id, i.order_date), end="")
    
    orderItem = OrderItem.objects.filter(order=i)
    price = 0
    for j in orderItem:
        price += j.amount * j.product.price
    print("PRICE: %.2f"%price)