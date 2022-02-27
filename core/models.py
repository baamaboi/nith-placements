from django.db import models

# Create your models here.

class Student(models.Model):
    roll = models.CharField(primary_key=True, blank=False, null=False, max_length=10)
    fname = models.CharField(blank=True, null=False, max_length=50)
    mname = models.CharField(blank=True, null=False, max_length=50)
    lname = models.CharField(blank=True, null=False, max_length=50)
    father_name = models.CharField(blank=True, null=False, max_length=100)
    cgpi = models.DecimalField(max_digits=4, decimal_places=2, blank=False, null=False)
    sgpi = models.DecimalField(max_digits=4, decimal_places=2, blank=False, null=True)
    dept = models.CharField(blank=False, null=False, max_length=50 , choices=[
        ('CHE', 'Chemical Engineering'),
        ('CE', 'Civil Engineering'),
        ('CSE', 'Computer Science and Engineering'),
        ('ECE', 'Electronics and Communication Engineering'),
        ('EE', 'Electrical Engineering'),
        ('MSE', 'Material Science Engineering'),
        ('ME', 'Mechanical Engineering')
    ])
    degree = models.CharField(blank=False, null=False, max_length=50, choices=[
        ('B. Tech' , 'B. Tech'),
        ('B. Tech + M. Tech.' , 'B. Tech + M. Tech.')
    ])

class Subject(models.Model):
    sub_code = models.CharField(primary_key=True, blank=False, null=False, max_length=8)
    sub_name = models.CharField(max_length=100)
    dept = models.CharField(blank=False, null=False, max_length=50, choices=[
        ('CHE', 'Chemical Engineering'),
        ('CE', 'Civil Engineering'),
        ('CSE', 'Computer Science and Engineering'),
        ('ECE', 'Electronics and Communication Engineering'),
        ('EE', 'Electrical Engineering'),
        ('MSE', 'Material Science Engineering'),
        ('ME', 'Mechanical Engineering')
    ])
    credits = models.PositiveSmallIntegerField(blank=False, null=False)


class Result(models.Model):
    roll = models.ForeignKey(Student, on_delete=models.CASCADE)
    sub_code = models.ForeignKey(Subject, on_delete=models.PROTECT)
    grade = models.PositiveSmallIntegerField(blank=False, null=False)
    semester = models.PositiveSmallIntegerField(blanck=False, null=False)

    class Meta:
        constraints = [models.UniqueConstraint(fields=['sub_code', 'semester', 'roll'])]

class ResultSummary(models.Model):
    roll = models.ForeignKey(Student, on_delete=models.CASCADE)
    semester = models.PositiveSmallIntegerField(blank=False, null=False)
    cgpi = models.DecimalField(max_digits=4, decimal_places=2, blank=False, null=False)
    sgpi = models.DecimalField(max_digits=4, decimal_places=2, blank=False, null=True)
    sem_credits = models.PositiveSmallIntegerField(blank=False, null=False)
    total_credits = models.PositiveSmallIntegerField(blank=False, null=False)

    class Meta:
        constraints = [models.UniqueConstraint(fields=['roll', 'semester'])]
        