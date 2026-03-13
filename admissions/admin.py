from django.contrib import admin
from .models import Student   # ← change 'Admissions' to 'Student'

admin.site.register(Student)
    