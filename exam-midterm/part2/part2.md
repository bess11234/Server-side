# Mid-Term Exam PART 2

> คะแนนเต็ม 10 คะแนน

ต่อเนื่องจากระบบจองห้องใน PART 1 ผมได้ออกแบบว่ามีหน้าเวบทั้งหมด 3 หน้าดังนี้

- หน้าสำหรับแสดงรายการห้อง (`Room`) ทั้งหมด
- หน้าสำหรับกดเข้าไปเพื่อทำการจองห้อง
- หน้ารายการการจอง (`Booking`) ทั้งหมด

## Questions

1. เขียน view และ template สำหรับแสดงรายการห้องทั้งหมดโดยให้แสดงผลดังภาพ (ผมเตรียมไฟล์ room-list.html ไว้ให้แล้ว) (2 คะแนน)

![q1](images/q1-image.png)

**Hint: ลองทดสอบ unit test ของข้อ 1 ได้โดยใช้คำสั่ง:**

```
>>> python manage.py test bookings.tests.test_room_list
```

2. ต่อเนื่องจากข้อ 1 เมื่อกดปุ่ม "Book Room" จะเข้าสู่หน้าจองห้องซึ่งจะให้กรอกฟอร์มข้อมูลต่างๆ เพื่อทำการจอง ให้เขียน view และ template สำหรับสร้างการจอง (ผมเตรียมไฟล์ booking.html ไว้ให้แล้ว) (4 คะแนน)

    **Requirments:**

    - ห้ามเลือก end_time ก่อน start_date จะต้องแสดง error message "End time cannot be before start time"
    - ช่วงเวลาจองจะต้องจองอย่างน้อย 1 ชั่วโมง และจะต้องไม่เกิน 3 ชั่วโมง ถ้าเกินจะต้องแสดง error message "Invalid duration: min 1 hour and max 3 hours"
    - ก่อนบันทึกการจองให้ทำการตรวจสอบก่อนว่าห้องที่จองเข้ามา ในช่วงเวลาที่เลือกไม่ได้ถูกจองไว้แล้ว ถ้าถูกจองแล้วให้แสดง error message "This room has already been booked for the selected time"
    - เมื่อจองสำเร็จให้ redirect ไปที่หน้า `รายการการจองทั้งหมด`

![q2](images/q2-image.png)

**Hint: ลองทดสอบ unit test ของข้อ 2-3 ได้โดยใช้คำสั่ง:**

```
>>> python manage.py test bookings.tests.test_post_room
```

3. เขียน view และ template สำหรับแสดงรายการการจองทั้งหมด **ที่ยังมาไม่ถึง** และเรียงจากใกล้ถึงวันที่จองก่อนอยู่ด้านบน โดยให้แสดงผลดังภาพ (ผมเตรียมไฟล์ booking-list.html ไว้ให้แล้ว) (2 คะแนน)

![q3](images/q3-image.png)

**Hint: ลองทดสอบ unit test ของข้อ 2-3 ได้โดยใช้คำสั่ง:**

```
>>> python manage.py test bookings.tests.test_post_room
```

4. เขียน view สำหรับเมื่อกดปุ่ม "Cancel Booking" แล้วจะทำการลบการจอง (`Booking`) (1 คะแนน)

**Hint: ลองทดสอบ unit test ของข้อ 4 ได้โดยใช้คำสั่ง:**

```
>>> python manage.py test bookings.tests.test_cancel_booking
```

5. เขียน view สำหรับเมื่อกดปุ่ม "Search" ในหน้า `รายการการจองทั้งหมด` จะค้นหาการจองด้วยชื่อห้องที่ถูกจอง และ ชื่อพนักงานผู้จอง (1 คะแนน)

**Hint: ลองทดสอบ unit test ของข้อ 5 ได้โดยใช้คำสั่ง:**

```
>>> python manage.py test bookings.tests.test_booking_search
```
