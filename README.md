https://github.com/it-web-pro/django-week2
# รหัส: password

# Week 2
## WINDOW Install virtualenv
```bash
pip install virtualenv
```

Create a virtual environment
```bash
py -m venv myvenv
```

Activate virtual environment
```bash
myvenv\Scripts\activate.bat
```
---
## MacOS Install virtualenv
```bash
pip install virtualenv
```

Create a virtual environment
```bash
python -m venv myvenv
```

Activate virtual environment
```bash
source myvenv/bin/activate
```

```
> django-admin startproject mysite
mysite/
    manage.py
    mysite/
        __init__.py
        settings.py # สำหรับตั้งค่า project
        urls.py # สำหรับกำหนด path url
        asgi.py
        wsgi.py
```
## คำสั่งในการเข้า Shell ใน Postgres
```sh
psql -U postgres
```
## คำสั่งในการแก้ไข Database
คำสั่งต้องทำคู่กันเมื่อมีการแก้ไข models.py
```bash
python manage.py makemigrations
```
ใช้เมื่อมีการแก้ไขไฟล์ models.py

```bash
python manage.py migrate
```

ใช้เพื่อให้ระบบนำไปอัพเดทข้อมูลในฐานข้อมูล ถ้ามีการแก้ไข Models

## คำสั่งภายใน Shell Django
```bash
<Table>.objects.all()
```
```bash
<Table>.objects.first()
```
```bash
<Table>.objects.get(pk=)
# pk คือ ID
```
```bash
.save()
# ใช้เมื่อต้องการบันทึกข้อมูลลงฐานข้อมูล
```

```bash
.<Table>_set.count()
# ใช้เมื่อ Tables นั้นมีความสัมพันธ์ 1 -M โดย Table เป็น 1 (เช่น choice_set)
```
```bash
<Table>.objects.filter(question_text__icontains="llo")
```
```bash
<Table>.objects.filter(question_text__startswith="What")
# แสดงข้อมูลที่มีการกำหนดประโยคภายใน
```
```bash
<Table>.objects.filter(<Table>_id=1, ...)
# แสดงข้อมูลตาม ID โดยมี _id โดยต้องมี Foreign Key
```
```bash
print(<คำสั่งที่เรียกข้อมูล>.query)
# แสดง SQL Query ที่คำสั่งใช้ใน Database
```
```bash
<Table>.objects.all().delete()
# ลบข้อมูลทั้งหมดใน Table
```
`{% <command> %}` command เป็นโค้ด Python

ถ้าเพิ่ม Template แล้วเข้าไปไม่ได้ให้รัน python manage.py runserver ใหม่

# Week 3
## **Importance**
เมื่อมีการใช้งาน ForeignKey Field อย่างเช่น
```bash
created_by_id = models.ForeignKey(Author, on_delete=models.PROTECT)
# เมื่อ Migrate จะทำการสร้าง Column ที่มีชื่อตามตัวแปร + _id ต่อท้ายให้ทำให้เป็น
# created_by_id_id
```

เมื่อมีการใช้งาน ManyToMany Field อย่างเช่น
```bash
categories = models.ManyToManyField("blogs.Category")
# จะสร้าง Table ที่่มีชื่อที่ขึ้นต้นด้วย Table ที่สร้าง Column นี้โดยอันนี้คือ blog ตามด้วย _<ตัวแปร>
# blog_categories
# และจะสร้าง ForeignKey ที่มีชื่อของ ทั้ง Table ที่ใช้สร้าง Column นี้กับ Table ที่เชื่อมไปคือ blog กับ Category และทั้งสองจะมี _id ต่อท้าย
# blog_id กับ category_id

cartItem = models.ManyToManyField("shop.Product", through="CartItem")
# ถ้ามี Column มากกว่า FK
```

เมื่อมีการใช้งาน Decimal Field อย่างเช่น
```bash
models.DecimalField(..., max_digits=5, decimal_places=2)
# ตัวเลขที่ใส่ได้มากที่สุดคือ 999.99 มาจากการเอา max_digits - decimal_places = 3 ก็คือจะต้องใส่ 9 สามตัว และ decimal_places คือจะต้องใส่ 9 สองตัว หลัง . หรือก็คือมีทศนิยมได้ 2 ตำแหน่ง
# 999.99

models.DecimalField(..., max_digits=19, decimal_places=10)
# 999999999.9999999999 ประมาณคือใส่ได้เยอะสุดเกือบ 1 พันล้าน
```

# Week 4

## Insert Data
วิธีสร้าง row หรือเพิ่มข้อมูลเข้าไปใน Table
```python
from blog.models import Blog, Author, Entry
b = Blog(name="Beatles Blog", tagline="All the latest Beatles news.")
b.save()
```
อีกโดยวิธีนี้ไม่ต้อง
`save()` ก็จะเพิ่มข้อมูลเข้าไปใน Database ทันที
```python
b = Blog.objects.create(name="Beatles Blog", tagline="All the latest Beatles news.")
```

ในความสัมพันธ์ ManyToMany ให้ใช้ `add()` กับ Table ที่สร้างขึ้นมาโดยสามารถเพิ่มได้ในหลายข้อมูลพร้อมกัน เพิ่มข้อมูลเข้าไปใน Database ทันที
```python
john = Author.objects.create(name="John")
paul = Author.objects.create(name="Paul")
george = Author.objects.create(name="George")
ringo = Author.objects.create(name="Ringo")
entry.authors.add(john, paul, george, ringo)

entry.authors.remove(john, paul, george, ringo) # เป็นการลบข้อมูลออกจาก Table ManaToMany
entry.authors.clear() # ลบทุกความสัมพันธ์ออกจาก Entry ใน Authors ที่เป็น Table ManaToMany
```

## Select Data
ข้อมูลที่จะได้มาจะเป็น Instance ของ Class **QuerySet**

```Python
Entry.objects.all() # SELECT * FROM entry;

Table.objects.filter().dictinct() # จะได้แบบ Unique Row
```

```python
Entry.objects.filter(pub_date__year=2010) # SELECT * FROM entry WHERE pub_date=2010;
```

สามารถใช้ Lookup __type ตามด้วยความหมายที่ต้องการดึง
```python
__exact=""|0|None # field="", field=0, field is NULL
__iexact=""|0|None # เหมือนกับ exact แต่เป็น case-insensitive ILIKE "" | ILIKE 0 | IS NULL
__contains="K" # LIKE %K%
__icontains="K" # ILIKE %K% เป็น case-insensitive
__startswith="K" # LIKE K%
__istartswith="K" # ILIKE K%
__endswith="K" # LIKE %K
__iendswith="K" # ILIKE %K
__in = [1, 2, 3]|"abc" # IN (1, 2, 3) | IN ("a", "b", "c")
__gte=1 # >= 1
__gt=1 # > 1
__lte=1 # <= 1
__te=1 # < 1
__range=(1, 2)|(date, date) # BETWEEN data AND date
__date=datetime # หมายความว่าที่ใส่ไปคือ type date || __date__gt || __date__gte ใช้ น้อยกว่า มากกว่า เพิ่มเติมได้
__year=2005 # แปลงเป็น BETWEEN '2005-01-01' AND '2005-12-31'
__year__gt=2005 # แปลงเป็น > "2005-01-01"
<field>__avg
<field>__count
<field>__max
<field>__min
<field>__sum
<field>__isnull=True
```
```python
Entry.objects.filter(headline__startswith="What").exclude(
    pub_date__gte=datetime.date.today()
).filter(pub_date__gte=datetime.date(2005, 1, 30))
```
`values(field1, field2, ..)` สามารถนำมาใช้กับการดึงข้อมูลแค่ Column ที่ต้องการได้
```python
>>> a = Author.objects.all().values("name")
<QuerySet [{'name': 'John'}, {'name': 'Joe'}, {'name': 'Paul'}, {'name': 'George'}, {'name': 'Ringo'}, {'name': 'John2'}, {'name': 'Test'}, {'name': 'Test'}]>
```
สามารถเอาไปประยุกต์กับการใช้ Lookup ได้ด้วยการ
```python
authors = Entry.objects.filter(pk=1).values("authors")
for i in Author.objects.filter(id__in=authors):
    print(i)
```

เลือกข้อมูลจากใน Table สามารถกำหนดเงื่อนไขผ่าน arguments ที่ Model มี
`<Table>.objects.get(column1="", column2="", ...)`
```python
entry = Entry.objects.get(pk=1)
cheese_blog = Blog.objects.get(name="Cheddar Talk")
```

### ข้อแตกต่างของ `get()` กับ `filter()`

- get() สามารถดึงข้อมูลเพียงแค่ตัวเดียว แล้วสามารถใช้ข้อมูลได้เลย แต่นั้นก็ทำให้ต้อง ***กำหนดเงื่อนไขให้ได้แค่ข้อมูลเดียว***
- filter() สามารถดึงข้อมูลได้ >= 1 ตัว แต่ต้องเข้าไปในแต่ละตัวเพื่อใช้งาน โดยจะได้เป็น `QuerySet`

```python
one_entry = Entry.objects.get(pk=1)
one_entry = Entry.objects.filter(pk=1).first()
one_entry = Entry.objects.filter(pk=1)[0]
# ทั้ง 3 บรรทัดนี้ให้ผลเหมือนกัน
```

### Limit ข้อมูลที่ต้องการ Query
การทำ Query อย่าง `SELECT * FROM table LIMIT 5` เพื่อประหยัดเวลาในการประมวลผลดึงข้อมูล

```python
Entry.objects.all()[:5] # LIMIT 5
Entry.objects.all()[5:11] # OFFSET 5 LIMIT 5
Entry.objects.all()[1:5] # OFFSET 1 LIMIT 4
Entry.objects.all()[:-1] # ! ERROR ValueError: Negative indexing is not supported.
```

### Compare ข้อมูล
เช็คข้อมูลว่าเป็นตัวเดียวกันหรือป่าวใช้ `==`

```python
author_1 = Author.objects.get(pk=1)
author_j = Author.objects.get(name="John")
author_1 == author_j # True
author_1.id == author_j.id # True
```

### Delete ข้อมูล
ลบข้อมูลออกจาก Database จากการใช้ `delete()`

```python
Author.objects.filter(name__startswith="T").delete() # ลบ Author ที่มีชื่อขึ้นต้นด้วย T
>>> (2, {'blog.Author': 2})
Author.objects.get(name="John").delete() # ลบ Author ที่ชื่อว่า John
>>> (1, {'blog.Author': 1})
Author.objects.all().delete() # ลบข้อมูลทั้งหมดใน Author
>>> (10, {'blog.Author': 10})
```

### Copy ข้อมูล

คัดลอกข้อมูลที่มีรายละเอียดเหมือนกัน โดยจะทำการลบ pk แล้วให้ใช้ `_state_adding = True` เป็นการเพิ่ม pk ใหม่อัตโนมัติ ต้องมีการ `save()` ด้วยเพื่อเพิ่มข้อมูลลงไป
```python
test = Author.objects.create(name="Test") # Author.objects.get(pk=1) || Author.objects.get(name="John")
test.pk = None
test._state_adding = True
test.save()
```

### Raw (query) ข้อมูล

การเขียน SQL Query ที่ต้องการโดยไม่ใช้ API จาก Django

### One to One Field Retrive Data

การดึงข้อมูลจากการใช้ความสัมพันธ์แบบ OneToOne ยกตัวอย่าง Order และ Payment มีความสัมพันธ์แบบ OneToOne โดยมีข้อมูลโครงสร้างดังนี้

```python
class Order(models.Model):
    customer = models.ForeignKey(Customer, models.CASCADE)
    order_date = models.DateField(auto_now_add=True)
    remark = models.TextField(null=True)
    orderItem = models.ManyToManyField(Product, through='shop.OrderItem')

class Payment(models.Model):
    order = models.OneToOneField(Order, models.CASCADE)
    payment_date = models.DateField(auto_now_add=True)
    remark = models.TextField(null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
```

จะเห็นว่า Payment มี field order อยู่ทำให้เวลาเรามี object ของ Payment เราจะสามารถดึงข้อมูลจาก Order ที่เชื่อมได้เลยอย่าง

```python
payment = Payment.objects.get(pk=1)
payment.order.order_date # Payment นี้ให้ดึงว่า Order เวลาไหน

order = Order.objects.get(pk=1)
order.payment.price # Order นี้ให้ดึงว่า payment ราคาเท่าไร
```

### Many to Many Field Retrive Data

การดึงข้อมูลโดยมีความสัมพันธ์แบบ ManyToMany จะแตกต่างกันโดยจะได้ข้อมูลมา
```python
class Order(models.Model):
    customer = models.ForeignKey(Customer, models.CASCADE)
    order_date = models.DateField(auto_now_add=True)
    remark = models.TextField(null=True)
    orderItem = models.ManyToManyField(Product, through='shop.OrderItem')

class OrderItem(models.Model):
    order = models.ForeignKey(Order, models.CASCADE)
    product = models.ForeignKey(Product, models.CASCADE)
    amount = models.IntegerField(default=1)
```

เราสามารถดึงข้อมูล OrderItem ผ่าน Order ได้เลยโดยวิธีดึงให้ใช้
```python
order = Order.objects.get(pk=1)
order.orderItem.all() # ดึงข้อมูล orderItem ทั้งหมด และจะสามารถดึงข้อมูลจาก field ที่ต้องการได้
```

ในกรณีที่อยากได้ amount ใน OrderItem ให้
```python
order = Order.objects.filter(order_date__month=5)[:10]
for i in order:
    for j in i.orderitem_set.all():
        print(j.amount, j.product.name, j.product.price)
```

**! ระวัง**
* `order.OrderItem.all()` อันนี้ดึงข้อมูลจาก Field ใน Order ที่ลิงค์ไปหา Product ทันทีเพราะงั้นคำสั่งนี้จะได้แค่ Product
* `order.orderitem_set.all()` อันนี้ดึงข้อมูลผ่าน Table OrderItem ทำให้ได้ Field ทั้งหมดใน OrderItem และดึงข้อมูล amount ได้

### Playground

เมื่อต้องการ filter ข้อมูลที่เป็น field แบบ ManyToMany สามารถใช้ __ แล้วตามด้วย field ของ Table ที่เชื่อมเช่น
```python
class ProductCategory(models.Model):
    name = models.CharField(max_length=150)
    
class Product(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(null=True)
    remaining_amount = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    categories = models.ManyToManyField(ProductCategory)
```

เราต้องการได้ Product แต่งื่อนไขคือต้องเป็นประเภท "Technologies" ซึ่งต้องดึงข้อมูลจาก categories ที่เป็น name มาโดยสามารถใช้
```python
product = Product.objects.filter(categories__name="Technologies") # ดึงข้อมูลสินค้าที่มีประเภท "Technologies"
```
ก็จะได้ข้อมูลที่ต้องการมา

## ! IMPORTANT `dir(<object>)` เพื่อ Function และ Attribute ของ Object มาดู