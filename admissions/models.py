
from django.db import models

class Student(models.Model):

    stu_name = models.CharField(max_length=50)
    stu_fname = models.CharField(max_length=50)
    stu_age = models.IntegerField()
    stu_dob = models.DateField()
    stu_email = models.EmailField()
    stu_web_link = models.URLField()
    stu_profile_pic = models.ImageField(upload_to="images/")
    stu_fees = models.DecimalField(max_digits=10, decimal_places=2)
    stu_active = models.BooleanField(default=True)

    cr_date = models.DateField(auto_now_add=True)
    cr_time = models.TimeField(auto_now_add=True)
    cr_date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.stu_name