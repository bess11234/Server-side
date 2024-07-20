from shop.models import *
books_category = ProductCategory.objects.get(pk=7)
it_category = ProductCategory.objects.get(pk=1)

product_1 = Product.objects.create(name="Philosopher's Stone (1997)", remaining_amount=20, description="By J. K. Rowling.", price=790)
product_1.categories.add(books_category)

product_2 = Product.objects.create(name="Me Before You", remaining_amount=40, description="A romance novel written by Jojo", price=390)
product_2.categories.add(books_category)

product_3 = Product.objects.create(name="Notebook HP Pavilion Silver", remaining_amount=10, description="Display Screen. 16.0", price=20000)
product_3.categories.add(it_category)