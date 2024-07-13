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

# **Importance**
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

# Week 3
