from django.db import models

# Create your models here.
class StudentData(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    section_name = models.CharField(max_length=30)
    class_name = models.CharField(max_length=10)
    school_name = models.CharField(max_length=50)
    telugu_marks = models.IntegerField()
    hindi_marks = models.IntegerField()
    english_marks = models.IntegerField()
    maths_marks = models.IntegerField()
    science_marks = models.IntegerField()
    social_marks = models.IntegerField()