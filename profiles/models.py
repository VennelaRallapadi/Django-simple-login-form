from django.db import models

class ProfileDetails(models.Model):
    stu_name=models.CharField(max_length=100)
    stu_id = models.AutoField(primary_key=True)
    
    def __str__(self):
        return ProfileDetails
    class Meta:
        verbose_name="TProfileDetails"
        verbose_name_plural="ProfileDetails"



