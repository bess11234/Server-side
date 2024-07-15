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

on_delete=
```bash
models.PROTECT
# เมื่อฝั่ง Foregin key จะถูกลบจะเกิดการป้องกันไม่ให้ฝั่งแม่ถูกลบได้ เพราะยังมีลูกอยู่
models.SET_NULL
# เมื่อฝั่ง Foregin key จะถูกลบจะใส่ค่า Null ให้
models.CASCADE
# เมื่อฝั่ง Foregin key จะถูกลบลูกทั้งหมดก็ถูกลบด้วย
models.DO_NOTHING
# เมื่อฝั่ง Foregin key จะถูกลบจะไม่มีการเปลี่ยนแปลงเกิดขึ้น
```

## Datetime
```python
import datetime as dt
>>> dt1 = dt.datetime(2024, 1, 12, 10, 30, 0)
>>> dt2 = dt.datetime.now()
>>> dt2-dt1
datetime.timedelta(days=185, seconds=12471, microseconds=779630)
```

```python
>>> dt1 + dt.timedelta(days=30) 
datetime.datetime(2024, 2, 11, 10, 30)
```
- **Naive datetime objects** หมายถึง datetime object ที่ไม่มีการกำหนดข้อมูล time zone (tzinfo เป็น None)
- **Aware datetime objects** คือ datetime object ทีมีข้อมูล time zone

```python
>>> from zoneinfo import ZoneInfo
dt2 = dt.datetime(2015, 12, 21, 12, 0, tzinfo = ZoneInfo(key='Asia/Bangkok'))
>>> print(dt2)
2015-12-21 12:00:00+07:00

>>> print("Naive Object :", dt1.tzname())
Naive Object : None
>>> print("Aware Object :", dt2.tzname())
Aware Object : +07
```

ใน settings.py
```python
TIME_ZONE = 'Asia/Bangkok'

USE_TZ=True
```
ช่วยให้ Convert เป็น UTC+0

เมื่อต้องการให้เวลาเป็นไปตาม TIME_ZONE ที่ได้ตั้งใน settings.py
timezone.localtime ทำให้จาก Aware เป็น Timezone ที่ตั้งไว้
timezone.make_aware ทำให้จาก Naive เป็น Aware ตาม Timezone ที่ตั้งไว้
```python
>>> from django.utils import timezone
>>> dt1 = datetime(2015, 12, 21, 12, 0, tzinfo=ZoneInfo(key='UTC')) 
>>> print(dt1)
2015-12-21 12:00:00+00:00
>>> dt1_local = timezone.localtime(dt1)
>>> print(dt1_local)
2015-12-21 19:00:00+07:00

>>> dt2 = datetime(2015, 5, 21, 12, 0) 
>>> print(dt2)
2015-12-21 12:00:00
>>> dt2_aware = timezone.make_aware(dt2)
>>> print(dt2_aware)
2015-05-21 12:00:00+07:00
```

เรื่อง Aware, Naive คือเมื่อเวลานั้นกำหนด Timezone จะเป็น Aware ถ้าไม่คือ Naive
Naive ไม่ดีเพราะเราจะไม่รู้เลยว่าเวลาที่ได้มาเป็นเวลาจาก Timezone ไหน
```python
>>> from django.utils import timezone
>>> timezone.is_aware(dt1)
True
>>> timezone.is_naive(dt1)
False
```

```python
>>> import datetime as dt
>>> dt.datetime.now() # สร้าง datetime ปัจจุบัน ที่ไม่มี timezone (Naive)
datetime.datetime(2024, 7, 15, 15, 21, 14, 597128)

>>> from django.utils import timezone
>>> timezone.localtime(dt.datetime.now()) # Error เพราะ localtime ใช้กับ Aware datetime
>>> timezone.make_aware(dt.datetime.now())
datetime.datetime(2024, 7, 15, 15, 22, 23, 461282, tzinfo=zoneinfo.ZoneInfo(key='Asia/Bangkok'))

>>> week500 = datenow + dt.timedelta(days=500)
>>> week500.weekday() # weekday() จะได้ 0-6 แทน Monday-Friday
3
```