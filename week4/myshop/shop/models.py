from django.db import models

# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=150)
    address = models.JSONField(null=True)

class ProductCategory(models.Model):
    name = models.CharField(max_length=150)
    
class Product(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(null=True)
    remaining_amount = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    categories = models.ManyToManyField(ProductCategory)

class Cart(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True)
    expired_in = models.IntegerField(default=60)
    cartItem = models.ManyToManyField("shop.Product", through="CartItem")
    
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.IntegerField(default=1)

class Order(models.Model):
    customer = models.ForeignKey(Customer, models.CASCADE)
    order_date = models.DateField(auto_now_add=True)
    remark = models.TextField(null=True)
    orderItem = models.ManyToManyField(Product, through='shop.OrderItem')

class OrderItem(models.Model):
    order = models.ForeignKey(Order, models.CASCADE)
    product = models.ForeignKey(Product, models.CASCADE)
    amount = models.IntegerField(default=1)

class Payment(models.Model):
    order = models.OneToOneField(Order, models.CASCADE)
    payment_date = models.DateField(auto_now_add=True)
    remark = models.TextField(null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=10, decimal_places=2, default=0)

# Weird
class PaymentMethod(models.Model):
    payment = models.ForeignKey(Payment, models.CASCADE)
    
    # ที่ต้องทำแบบนี้เพื่อให้เวลาใช้งาน ใช้งานได้ง่าย
    QR = 1
    CREDIT = 2
    methodPayment = {QR: "QR", CREDIT: "CREDIT"}
    method = models.IntegerField(choices=methodPayment)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def getMethod(self):
        return self.methodPayment[self.method]
    
class PaymentItem(models.Model):
    payment = models.ForeignKey(Payment, models.CASCADE)
    order_item = models.OneToOneField(OrderItem, models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    