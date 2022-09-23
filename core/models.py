from datetime import datetime
from operator import mod
from tabnanny import verbose
from django.core.validators import RegexValidator
from django.db import models

# from django.contrib.auth import password_validation
# from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser

regex_mobile = r"^[6789]\d{9}$"
STATES = [
    ("Rajasthan", "Rajasthan"),
    ("Madhya Pradesh", "Madhya Pradesh"),
    ("Maharashtra", "Maharashtra"),
    ("Uttar Pradesh", "Uttar Pradesh"),
    ("Gujarat", "Gujarat"),
    ("Karnataka", "Karnataka"),
    ("Andhra Pradesh", "Andhra Pradesh"),
    ("Odisha", "Odisha"),
    ("Chhattisgarh", "Chhattisgarh"),
    ("Tamil Nadu", "Tamil Nadu"),
    ("Telangana", "Telangana"),
    ("Bihar", "Bihar"),
    ("West Bengal", "West Bengal"),
    ("Arunachal Pradesh", "Arunachal Pradesh"),
    ("Jharkhand", "Jharkhand"),
    ("Assam", "Assam"),
    ("Ladakh", "Ladakh"),
    ("Himachal Pradesh", "Himachal Pradesh"),
    ("Uttarakhand", "Uttarakhand"),
    ("Punjab", "Punjab"),
    ("Haryana", "Haryana"),
    ("Jammu and Kashmir", "Jammu and Kashmir"),
    ("Kerala", "Kerala"),
    ("Meghalaya", "Meghalaya"),
    ("Manipur", "Manipur"),
    ("Mizoram", "Mizoram"),
    ("Nagaland", "Nagaland"),
    ("Tripura", "Tripura"),
    ("Andaman and Nicobar Islands", "Andaman and Nicobar Islands"),
    ("Sikkim", "Sikkim"),
    ("Goa", "Goa"),
    ("Delhi", "Delhi"),
    (
        "Dadra and Nagar Haveli and Daman and Diu",
        "Dadra and Nagar Haveli and Daman and Diu",
    ),
    ("Puducherry", "Puducherry"),
    ("Chandigarh", "Chandigarh"),
    ("Lakshadweep", "Lakshadweep"),
]
BRANCHES = [
    ("Electrical Engineering", "Electrical Engineering"),
    (
        "Electronics and Communication Engineering",
        "Electronics and Communication Engineering",
    ),
    ("Civil Engineering", "Civil Engineering"),
    ("Material Science and Engineering", "Material Science and Engineering"),
    ("Computer Science and Engineering", "Computer Science and Engineering"),
    ("Chemical Engineering", "Chemical Engineering"),
    ("Mechanical Engineering", "Mechanical Engineering"),
    ("Architecture", "Architecture"),
]
DEGREES = [
    ("B.Tech.", "B.Tech."),
    ("Dual Degree (B.Tech. + M.Tech.)", "Dual Degree (B.Tech. + M.Tech.)"),
    ("B.Arch.", "B.Arch."),
]
# liitle_helpers


def capitalize_each_word(word: str) -> str:
    t = type(word).__name__
    if t != "str":
        raise TypeError(f"Expected str got {t}")
    word = word.strip()
    word = word.lower()
    word = word.split()
    result = ""
    for i in word:
        result += i.capitalize() + " "
    return result.strip()


def clean_email(email: str) -> str:
    t = type(email).__name__
    if t == "NoneType":
        return None
    if t != "str":
        raise TypeError(f"Expected str got {t}")
    try:
        email_name, domain_part = email.strip().rsplit("@", 1)
    except ValueError:
        pass
    else:
        email = email_name + "@" + domain_part.lower()
    return email


# Create your models here.


class StudentManager(models.Manager):
    def create_user(self, email=None, **extra_fields):
        email = email or ""
        email = email.strip()
        for key, value in extra_fields.items():
            if type(value).__name__ == "str":
                extra_fields[key] = value.strip()
        extra_fields["fname"] = capitalize_each_word(
            extra_fields.get("fname", "Jessie")
        )
        extra_fields["mname"] = capitalize_each_word(extra_fields.get("mname", ""))
        extra_fields["lname"] = capitalize_each_word(extra_fields.get("lname", ""))
        extra_fields["father_name"] = capitalize_each_word(
            extra_fields.get("father_name", "")
        )
        email = clean_email(email)
        extra_fields["student_email"] = clean_email(
            extra_fields.get("student_email", None)
        )
        extra_fields["domicile_district"] = extra_fields.get(
            "domicile_district", ""
        ).capitalize()
        user = self.model(email=email, **extra_fields)
        user.save(using=self._db)
        return user


class Student(models.Model):
    roll = models.CharField(
        verbose_name="Roll Number",
        primary_key=True,
        blank=False,
        null=False,
        max_length=10,
    )
    fname = models.CharField(
        verbose_name="First Name", blank=False, null=False, max_length=50
    )
    mname = models.CharField(
        verbose_name="Middle Name", blank=True, null=False, max_length=50
    )
    lname = models.CharField(
        verbose_name="Last Name", blank=True, null=False, max_length=50
    )
    father_name = models.CharField(
        verbose_name="Father's Name", blank=True, null=False, max_length=100
    )
    sex = models.CharField(
        verbose_name="Sex",
        max_length=6,
        blank=False,
        null=True,
        choices=[("Female", "Female"), ("Male", "Male"), ("Other", "Other")],
    )
    email = models.EmailField(verbose_name="Personal Email")
    phone_number1 = models.CharField(
        verbose_name="Phone Number (WhatsApp)",
        max_length=10,
        blank=True,
        null=False,
        validators=[RegexValidator(regex=regex_mobile)],
    )
    phone_number2 = models.CharField(
        verbose_name="Phone Number",
        max_length=10,
        blank=True,
        null=False,
        validators=[RegexValidator(regex=regex_mobile)],
    )
    student_email = models.EmailField(
        verbose_name="Student Email",
        null=True,
        blank=False,
        validators=[RegexValidator(regex=r"([A-Za-z0-9]+)@nith\.ac\.in")],
    )
    cgpi_bachelor = models.DecimalField(
        verbose_name="CGPI (U.G.)",
        max_digits=4,
        decimal_places=2,
        blank=False,
        null=False,
    )
    cgpi_master = models.DecimalField(
        verbose_name="CGPI (P.G.)",
        max_digits=4,
        decimal_places=2,
        blank=True,
        null=True,
        default=None,
    )
    dob = models.DateField(verbose_name="DOB", null=False, blank=False)
    active_backlog = models.DecimalField(
        verbose_name="Active Backlogs",
        max_digits=2,
        decimal_places=0,
        blank=False,
        null=False,
        default=0,
    )
    total_backlog = models.DecimalField(
        verbose_name="Total Backlogs",
        max_digits=2,
        decimal_places=0,
        blank=False,
        null=False,
    )
    twelveth_year = models.DecimalField(
        verbose_name="12 Year", max_digits=4, decimal_places=0, blank=False, null=False
    )
    twelveth_board = models.CharField(
        verbose_name="12 Education Board",
        max_length=100,
        blank=False,
        null=True,
        default=None,
    )
    twelveth_school = models.CharField(
        verbose_name="12 School Name", max_length=200, blank=False, null=True
    )
    twelveth_percent = models.DecimalField(
        verbose_name="12 Percentage",
        max_digits=5,
        decimal_places=2,
        blank=False,
        null=False,
    )
    tenth_year = models.DecimalField(
        verbose_name="10 Year", max_digits=4, decimal_places=0, blank=False, null=False
    )
    tenth_board = models.CharField(
        verbose_name="10 Education Board",
        max_length=100,
        blank=False,
        null=True,
        default=None,
    )
    tenth_school = models.CharField(
        verbose_name="10 School Name", max_length=200, blank=False, null=True
    )
    tenth_percent = models.DecimalField(
        verbose_name="10 Percentage",
        max_digits=5,
        decimal_places=2,
        blank=False,
        null=False,
    )
    domicile_state = models.CharField(
        verbose_name="Domicile State",
        max_length=500,
        blank=False,
        null=True,
        default=None,
        choices=STATES,
    )
    domicile_district = models.CharField(
        verbose_name="Domicile District",
        max_length=500,
        blank=False,
        null=True,
        default=None,
    )
    domicile_place = models.CharField(
        verbose_name="Domicile Place",
        max_length=500,
        blank=False,
        null=True,
        default=None,
    )
    cv = models.URLField(
        verbose_name="CV Drive URL", max_length=200, blank=False, null=True
    )
    grad_year = models.DecimalField(
        verbose_name="Graduation Year",
        max_digits=4,
        decimal_places=0,
        blank=False,
        null=False,
    )
    curr_batch = models.DecimalField(
        verbose_name="Admission Year",
        max_digits=4,
        decimal_places=0,
        blank=False,
        null=False,
    )
    pwd = models.BooleanField(
        verbose_name="PwD", null=False, blank=False, default=False
    )
    cluster = models.JSONField(verbose_name="Cluster Prefrences", null=True, blank=True)
    dept = models.CharField(
        verbose_name="Branch", blank=True, null=False, max_length=50, choices=BRANCHES
    )
    degree = models.CharField(
        verbose_name="Degree",
        blank=False,
        null=False,
        max_length=50,
        choices=DEGREES,
    )
    objects = StudentManager()

    def save(self, *args, **kwargs):
        if self.cgpi_master == "":
            self.cgpi_master = None
        if self.cluster == "" or self.cluster == "null":
            self.cluster = None
        super(Student, self).save(*args, **kwargs)


class MyUser(AbstractUser):
    is_student = models.BooleanField(
        verbose_name="Student Status",
        null=False,
        blank=False,
        default=True,
        help_text="Designates that this user is a student",
    )
    is_tpr = models.BooleanField(
        verbose_name="TPR Status",
        null=False,
        blank=False,
        default=False,
        help_text="Designates that this student has TPR level permissions",
    )
    is_core_tpr = models.BooleanField(
        verbose_name="Core TPR status",
        null=False,
        blank=False,
        default=False,
        help_text="Designates that this student has Core TPR level permissions",
    )
    is_jtpr = models.BooleanField(
        verbose_name="JTPR Status",
        null=False,
        blank=False,
        default=False,
        help_text="Designates that this student has JTPR level permissions",
    )
    nith_email = models.EmailField(
        verbose_name="NITH Email Address",
        null=True,
        blank=True,
        validators=[RegexValidator(regex=r"([A-Za-z0-9]+)@nith\.ac\.in")],
    )
    roll = models.OneToOneField(
        Student,
        verbose_name="Roll Number (If Student)",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        help_text="Student association if the user is a student.",
    )

    def save(self, *args, **kwargs):
        if self.roll == "":
            self.roll = None
        if self.nith_email == "":
            self.nith_email = None
        super(MyUser, self).save(*args, **kwargs)


class Company(models.Model):
    name = models.CharField(
        verbose_name="Company Name", blank=True, null=False, max_length=200
    )
    ctc_offered = models.DecimalField(
        verbose_name="CTC offered",
        max_digits=12,
        decimal_places=2,
        null=True,
        blank=True,
    )
    stipend_offered = models.DecimalField(
        verbose_name="Stipend offered",
        max_digits=12,
        decimal_places=2,
        null=True,
        blank=True,
    )
    total_candidates_place = models.DecimalField(
        verbose_name="Total Candidates Placed",
        null=True,
        blank=True,
        max_digits=2,
        decimal_places=0,
        default=0,
    )
    jnf_url = models.URLField(
        verbose_name="JNF URL", null=True, blank=True, default=None
    )
    on_campus = models.BooleanField(
        verbose_name="On Campus", null=False, blank=False, default=True
    )
    fte = models.BooleanField(verbose_name="FTE", null=False, blank=False, default=True)
    intern = models.BooleanField(
        verbose_name="Intern", null=False, blank=False, default=False
    )
    allowed_branches = models.JSONField(
        verbose_name="Allowed Branches", null=True, blank=True
    )
    fte_profile = models.CharField(
        verbose_name="FTE Profile", null=True, blank=True, max_length=400
    )
    intern_profile = models.CharField(
        verbose_name="Intern Profile", null=True, blank=True, max_length=400
    )
    drive_start_date = models.DateField(
        verbose_name="Drive Start Date", null=True, blank=True
    )
    drive_end_date = models.DateField(
        verbose_name="Drive End Date", null=True, blank=True
    )
    drive_engagement_date = models.DateField(
        verbose_name="Drive Engagement Date", null=True, blank=True
    )
    hr_details = models.JSONField(verbose_name="HR Details", null=True, blank=True)
    drive_status = models.CharField(
        null=True,
        blank=True,
        max_length=100,
        choices=[
            ("Upcomming", "Upcomming"),
            ("Complete", "Complete"),
            ("Ongoing", "Ongoing"),
        ],
    )
    drive_result = models.CharField(
        null=True,
        blank=True,
        max_length=100,
        choices=[
            ("Successful", "Successful"),
            ("Failed", "Failed"),
            ("Canceled", "Canceled"),
            ("Suspended", "Suspended"),
        ],
    )
    graduating_batch = models.DecimalField(
        null=False, blank=False, max_digits=4, decimal_places=0
    )
    spoc = models.ManyToManyField(MyUser)
    remarks = models.TextField(null=True, blank=True)

    def save(self, *args, **kwargs):
        field_names = [
            "ctc_offered",
            "candidates_placed",
            "jnf_url",
            "intern_details",
            "drive_start_date",
            "drive_end_date",
            "drive_engagement_date",
            "hr_details",
            "drive_result",
            "spoc",
            "stipend_offered",
            "drive_status",
        ]
        for f in field_names:
            value = getattr(self, f)
            if value == "" or value == "null":
                setattr(self, f, None)
        super(Company, self).save(*args, **kwargs)


class PlacementsAndInterns(models.Model):
    roll = models.ForeignKey(
        Student, on_delete=models.CASCADE, verbose_name="Roll Number"
    )
    company_intern = models.ForeignKey(
        Company,
        verbose_name="Intern Company",
        null=True,
        blank=True,
        on_delete=models.PROTECT,
        related_name="intern_company",
    )
    intern = models.BooleanField(
        verbose_name="Intern",
        default=False,
        null=True,
        blank=True,
    )
    job = models.BooleanField(verbose_name="Job", default=False, null=True, blank=True)
    first_company_placement = models.ForeignKey(
        Company,
        verbose_name="First Job Company",
        null=True,
        blank=True,
        on_delete=models.PROTECT,
        related_name="first_job_company",
    )
    second_company_placement = models.ForeignKey(
        Company,
        verbose_name="Second Job Company",
        null=True,
        blank=True,
        on_delete=models.PROTECT,
        related_name="second_job_company",
    )
    plus_placement = models.JSONField(
        verbose_name="Additional Placement JSON", null=True, blank=True
    )
    no_of_placements = models.DecimalField(
        verbose_name="Placement Count",
        max_digits=2,
        decimal_places=0,
        default=0,
        null=False,
        blank=False,
    )

    class Meta:
        constraints = [models.UniqueConstraint(fields=["roll"], name="unique_record")]

    def save(self, *args, **kwargs):
        fields = [
            "company_intern",
            "stipend",
            "intern_on_campus",
            "intern",
            "job",
            "first_ctc",
            "first_job_on_campus",
            "first_company_placement",
            "first_company_placement",
            "second_ctc",
            "second_job_on_campus",
            "second_company_placement",
            "plus_placement",
        ]
        for f in fields:
            value = getattr(self, f)
            if value == "" or value == "null":
                setattr(self, f, None)
        super(PlacementsAndInterns, self).save(*args, **kwargs)


class Subject(models.Model):
    sub_code = models.CharField(
        verbose_name="Subject Code",
        primary_key=True,
        blank=False,
        null=False,
        max_length=8,
    )
    sub_name = models.CharField(
        verbose_name="Subject Name", max_length=100, blank=False, null=False
    )
    dept = models.CharField(
        verbose_name="Subject Department",
        blank=False,
        null=False,
        max_length=50,
        choices=BRANCHES,
    )
    credits = models.PositiveSmallIntegerField(
        verbose_name="Credits", blank=False, null=False
    )


class Result(models.Model):
    roll = models.ForeignKey(
        Student, on_delete=models.CASCADE, verbose_name="Roll Number"
    )
    sub_code = models.ForeignKey(
        Subject, on_delete=models.PROTECT, verbose_name="Subject Code"
    )
    grade = models.PositiveSmallIntegerField(
        blank=False, null=False, verbose_name="Grade"
    )
    semester = models.PositiveSmallIntegerField(
        blank=False, null=False, verbose_name="Semester Number"
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["sub_code", "semester", "roll"], name="unique_result"
            )
        ]


class ResultSummary(models.Model):
    roll = models.ForeignKey(
        Student, on_delete=models.CASCADE, verbose_name="Roll Number"
    )
    semester = models.PositiveSmallIntegerField(
        blank=False, null=False, verbose_name="Semester Number"
    )
    cgpi = models.DecimalField(
        max_digits=4, decimal_places=2, blank=False, null=False, verbose_name="CGPI"
    )
    sgpi = models.DecimalField(
        max_digits=4, decimal_places=2, blank=True, null=True, verbose_name="SGPI"
    )
    sem_credits = models.PositiveSmallIntegerField(
        blank=False, null=False, verbose_name="Semester Credits"
    )
    total_credits = models.PositiveSmallIntegerField(
        blank=False, null=False, verbose_name="Cumalative Total Credits"
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["roll", "semester"], name="unique_summary")
        ]

    def save(self, *args, **kwargs):
        if self.sgpi == "":
            self.sgpi = None
        super(ResultSummary, self).save(*args, **kwargs)
