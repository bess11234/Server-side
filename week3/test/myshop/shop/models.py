from django.db import models

# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length=150, null=False)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=150)
    address = models.JSONField(null=True)
    
class Product(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(null=True)
    remaining_amount = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    categories = models.ManyToManyField('shop.ProductCategory')

class Cart(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=False)
    create_date = models.DateTimeField(auto_now_add=True)
    expired_In = models.IntegerField(default=60)
    cartItem = models.ManyToManyField("shop.Product", through="CartItem")

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    amount = models.IntegerField(default=1)

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_date = models.DateField(auto_now_add=True)
    remark = models.TextField(null=True)
    orderItem = models.ManyToManyField(Product, through="OrderItem")

class Payment(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    payment_date = models.DateField(auto_now_add=True)
    remark = models.TextField(null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=10, decimal_places=2, default=0)

class PaymentMethod(models.Model):
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE, null=True)
    methodPayment = {1: "QR", 2: "CREDIT"}
    method = models.IntegerField(choices=methodPayment)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def get_method(self):
        return self.methodPayment[self.method]

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.IntegerField(default=1)

class PaymentItem(models.Model):
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE)
    order_item = models.OneToOneField(OrderItem, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=10, decimal_places=2, default=0)

class ProductCategory(models.Model):
    name = models.CharField(max_length=150)