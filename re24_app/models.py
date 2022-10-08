from django.db import models


class Student(models.Model):
    
    Name = models.CharField(max_length = 50)
    Age = models.IntegerField(null = True)
    City = models.CharField(max_length = 100,null = True)
    DOB = models.DateField() 
    Img = models.ImageField(upload_to='Pictures/', null = True)       
    #def __str__(self):
        #return self.Name

class Mark(models.Model):
    student = models.ForeignKey(Student,null = True, on_delete=models.CASCADE)
    sub = models.CharField(max_length = 50)
    mrk = models.IntegerField(null = True)
    created_at = models.DateTimeField(auto_now_add=True, null = True)
    updated_at = models.DateTimeField(auto_now=True, null = True)
    creator = models.CharField(max_length = 50)
    updator = models.CharField(max_length = 50)
    def __int__(self):
        return self.student
     
