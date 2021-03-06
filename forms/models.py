from django.db import models

# Create your models here.
class data_form(models.Model):
    first_name = models.CharField(null=True, blank=True, max_length=50)
    last_name = models.CharField(null=True, blank=True, max_length=50)
    father_name = models.CharField(null=True, blank=False, max_length=20)
    mother_name = models.CharField(null=True, blank=False, max_length=20)
    contact = models.CharField(null=True, blank=False, max_length=20)
    email = models.CharField(null=True, blank=True, max_length=50)
    father_contact = models.CharField(null=True, blank=True, max_length=10)
    mother_contact = models.CharField(null=True, blank=True, max_length=10)
    address = models.TextField(null=True, blank=True)
    city = models.CharField(null=True, blank=True, max_length=50)
    state = models.CharField(null=True, blank=True, max_length=50)
    pin = models.CharField(null=True, blank=True,max_length=10)
    country = models.CharField(null=True, blank=True, max_length=50)
    present_address = models.TextField(null=True, blank=True)
    present_city = models.CharField(null=True, blank=True, max_length=30)
    ppin = models.CharField(null=True, blank=True, max_length=10)
    pstate = models.CharField(null=True, blank=True, max_length=30)
    pcountry = models.CharField(null=True, blank=True, max_length=30)
    #work in experience
    org_name1 = models.CharField(null=True, blank=True, max_length=100)
    des1 = models.CharField(null=True, blank=True, max_length=100)
    peroid1 = models.CharField(null=True, blank=True, max_length=100)
    nature_work1 = models.CharField(null=True, blank=True, max_length=100)
    salary1 = models.CharField(null=True, blank=True, max_length=100)
    org_name2 = models.CharField(null=True, blank=True, max_length=100)
    des2 = models.CharField(null=True, blank=True, max_length=100)
    period2 = models.CharField(null=True, blank=True, max_length=100)
    nature_work2 = models.CharField(null=True, blank=True, max_length=100)
    salary2 = models.CharField(null=True, blank=True, max_length=100)
    total_exp = models.CharField(null=True, blank=True, max_length=100)
    #Awards and Honors
    year1 = models.CharField(null=True, blank=True, max_length=100)
    award_name1 = models.CharField(null=True, blank=True, max_length=100)
    institute1 = models.CharField(null=True, blank=True, max_length=100)
    level1 = models.CharField(null=True, blank=True, max_length=100)
    remark1 = models.CharField(null=True, blank=True, max_length=100)
    year2 = models.CharField(null=True, blank=True, max_length=100)
    award_name2 = models.CharField(null=True, blank=True, max_length=100)
    institute2 = models.CharField(null=True, blank=True, max_length=100)
    level2 = models.CharField(null=True, blank=True, max_length=100)
    remark2 = models.TextField(null=True, blank=True)

    #how do you come to know abt us
    how = models.CharField(null=True, blank=True, max_length=100)
    #personal perticular
    dob = models.CharField(null=True, blank=True, max_length=15)
    pob = models.CharField(null=True, blank=True, max_length=50)
    gender = models.CharField(null=True, blank=True, max_length=10)
    category = models.CharField(null=True, blank=True, max_length=50)
    aadhar = models.IntegerField(null=True, blank= True)
    blood_group = models.CharField(null=True, blank=True, max_length=10)
    maratial_status = models.CharField(null=True, blank=True, max_length=20)
    program = models.CharField(null=True, blank=True, max_length=100)
    # acedamic qualification
    secondary_year = models.CharField(null=True, blank=True, max_length=100)
    nos1 = models.CharField(null=True, blank=True, max_length=100)
    board1 = models.CharField(null=True, blank=True, max_length=100)
    max_marks1 = models.CharField(null=True, blank=True, max_length=100)
    marks1 = models.CharField(null=True, blank=True, max_length=100) 
    percent1 = models.CharField(null=True, blank=True, max_length=100)
    sr_secondary_year = models.CharField(null=True, blank=True, max_length=100)
    nos2 = models.CharField(null=True, blank=True, max_length=100)
    board2 = models.CharField(null=True, blank=True, max_length=100)
    max_marks2 = models.CharField(null=True, blank=True, max_length=100)
    marks2 = models.CharField(null=True, blank=True, max_length=100) 
    percent2 = models.CharField(null=True, blank=True, max_length=100)

    # Graduation
    name_of_degree = models.CharField(null=True, blank=True, max_length=100)
    graduation_year1 = models.CharField(null=True, blank=True, max_length=100)
    college1 = models.CharField(null=True, blank=True, max_length=100)
    uni1 = models.CharField(null=True, blank=True, max_length=100)
    mmarks1 = models.CharField(null=True, blank=True, max_length=100)
    mo1 = models.CharField(null=True, blank=True, max_length=100)
    cgpa1 = models.CharField(null=True, blank=True, max_length=100)
    photograph = models.FileField(null=True, blank=True)
    

    def __str__(self):
        return self.first_name + " " + self.last_name