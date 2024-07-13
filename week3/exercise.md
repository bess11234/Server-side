# WEEK 3 Exercises - Django Model

1. สร้าง project ใหม่ชื่อ "myshop" (สร้าง vitual environment ใหม่ด้วย)
2. สร้าง app ชื่อ shop และทำการตั้งค่าใน `settings.py`
3. แก้ไขไฟล์ `models.py` สร้าง models ตาม ERD นี้

![ERD-E-COMMERCE](./images/WEEK3-ERD(e-commerce).png)

4. ทำการ makemigrations
5. ทำการ migrate เพื่อสร้างตาราง

### การให้คะแนน

- สร้าง models ที่มีความสัมพันธ์แบบ one-to-many ได้ครบถ้วนถูกต้อง (1 คะแนน)
- สร้าง models ที่มีความสัมพันธ์แบบ one-to-one ได้ครบถ้วนถูกต้อง (0.5 คะแนน)
- สร้าง models ที่มีความสัมพันธ์แบบ many-to-many ได้ครบถ้วนถูกต้อง (1 คะแนน)
- กำหนด ENUM method ใน model PaymentMethod ได้ถูกต้อง (0.5 คะแนน)