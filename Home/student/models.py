from django.db import models
from django.utils.text import slugify
from django.utils.crypto import get_random_string

# Create your models here.

class Parent(models.Model):
    father_name = models.CharField(max_length=100)
    father_occupation = models.CharField(max_length=100)
    father_mobile = models.CharField(max_length=15)
    father_email = models.EmailField(max_length=100)
    mother_name = models.CharField(max_length=100)
    mother_occupation = models.CharField(max_length=100)
    mother_mobile = models.CharField(max_length=15)
    mother_email = models.EmailField(max_length=100)
    present_address = models.TextField(max_length=100)
    permanent_address = models.TextField(max_length=100)
    
    def __str__(self) -> str:
        return f"{self.father_name} & {self.mother_name}"
    
class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    student_id = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=[("Male", "Male"),("Female", "Female"),("others", "others")])
    date_of_birth = models.DateField()
    student_class = models.CharField(max_length=100)
    religion = models.CharField(max_length=10)
    joining_date = models.DateField(default=True)
    mobile_number = models.CharField(max_length=15)
    admission_number = models.CharField(max_length=100)
    section = models.CharField(max_length=15)
    student_image = models.ImageField(upload_to="student/",blank=True )
    parent = models.OneToOneField(Parent, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=225, unique=True, blank=True)
    
    
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.first_name}-{self.last_name}-{self.student_id}")
        super(Student, self).save(*args, **kwargs)
    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.student_id})"
    


    
    
