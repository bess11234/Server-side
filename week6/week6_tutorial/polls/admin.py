from django.contrib import admin

# Register your models here.
from .models import Question, Choice

class ChoiceInline(admin.TabularInline): # admin.TabularInline อยู่ข้าง ๆ กัน # admin.StackedInline คนละบรรทัด
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    list_display = ["question_text", "pub_date"] # เปลี่ยนตัวแสดงผลในหน้าแต่ละ Table/Class
    
    list_filter = ["pub_date"]
    search_fields = ["question_text"]

    fieldsets = [
        ("Question text", {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin) # มันจะสลับ Field ตาม QuestionAdmin ใน หน้า admin

admin.site.register(Choice)