# Mid-Term Exam PART 1

> คะแนนเต็ม 10 คะแนน

## Instructions:

1. สร้าง virtualenv และติดตั้ง django และ psycopg2
2. สร้าง project `room_booking`
3. สร้าง app `bookings`
4. เพิ่ม code ด้านล่างใน `bookings/models.py`

```python
from django.db import models

class Staff(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    position = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class RoomType(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Room(models.Model):
    number = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    capacity = models.IntegerField()
    description = models.TextField(blank=True)
    room_types = models.ManyToManyField(RoomType, related_name='rooms', blank=True)

    def __str__(self):
        return f'Room {self.number}: {self.name}'


class Booking(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    purpose = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f'Booking by {self.staff} for {self.room} from {self.start_time} to {self.end_time}'

```

5. สร้าง DB ชื่อ `bookings` และทำการ import ข้อมูลจากไฟล์ `bookings.sql`
6. ติดตั้งเพื่อใช้งาน Jupyter Notebook ตามขั้นตอนใน `django-notebook.md`

**จากนั้นเริ่มทำโจทย์ในไฟล์ `part1.ipynb`**
