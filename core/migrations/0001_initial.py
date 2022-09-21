# Generated by Django 4.0.1 on 2022-09-10 20:28

import django.contrib.auth.models
import django.contrib.auth.validators
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, verbose_name='Company Name')),
                ('ctc_offered', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True, verbose_name='CTC offered')),
                ('candidates_placed', models.JSONField(blank=True, null=True, verbose_name='Placed candidates JSON')),
                ('total_candidates_place', models.DecimalField(blank=True, decimal_places=0, default=0, max_digits=2, null=True, verbose_name='Total Candidates Placed')),
                ('jnf_url', models.URLField(blank=True, default=None, null=True, verbose_name='JNF URL')),
                ('on_campus', models.BooleanField(default=True, verbose_name='On Campus')),
                ('fte', models.BooleanField(default=True, verbose_name='FTE')),
                ('intern', models.BooleanField(default=False, verbose_name='Intern')),
                ('intern_details', models.JSONField(blank=True, null=True, verbose_name='Intern Details')),
                ('fte_profile', models.CharField(blank=True, max_length=400, null=True, verbose_name='FTE Profile')),
                ('intern_profile', models.CharField(blank=True, max_length=400, null=True, verbose_name='Intern Profile')),
                ('drive_start_date', models.DateField(blank=True, null=True, verbose_name='Drive Start Date')),
                ('drive_end_date', models.DateField(blank=True, null=True, verbose_name='Drive End Date')),
                ('drive_engagement_date', models.DateField(blank=True, null=True, verbose_name='Drive Engagement Date')),
                ('hr_details', models.JSONField(blank=True, null=True, verbose_name='HR Details')),
                ('drive_result', models.CharField(blank=True, choices=[('Successful', 'Successful'), ('Failed', 'Failed'), ('Canceled', 'Canceled'), ('Suspended', 'Suspended')], max_length=100, null=True)),
                ('graduating_batch', models.DecimalField(decimal_places=0, max_digits=4)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('roll', models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='Roll Number')),
                ('fname', models.CharField(max_length=50, verbose_name='First Name')),
                ('mname', models.CharField(blank=True, max_length=50, verbose_name='Middle Name')),
                ('lname', models.CharField(blank=True, max_length=50, verbose_name='Last Name')),
                ('father_name', models.CharField(blank=True, max_length=100, verbose_name="Father's Name")),
                ('sex', models.CharField(choices=[('Female', 'Female'), ('Male', 'Male'), ('Other', 'Other')], max_length=6, null=True, verbose_name='Sex')),
                ('email', models.EmailField(max_length=254, verbose_name='Personal Email')),
                ('phone_number1', models.CharField(blank=True, max_length=10, validators=[django.core.validators.RegexValidator(regex='^[6789]\\d{9}$')], verbose_name='Phone Number (WhatsApp)')),
                ('phone_number2', models.CharField(blank=True, max_length=10, validators=[django.core.validators.RegexValidator(regex='^[6789]\\d{9}$')], verbose_name='Phone Number')),
                ('student_email', models.EmailField(max_length=254, null=True, validators=[django.core.validators.RegexValidator(regex='([A-Za-z0-9]+)@nith\\.ac\\.in')], verbose_name='Student Email')),
                ('cgpi_bachelor', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='CGPI (U.G.)')),
                ('cgpi_master', models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=4, null=True, verbose_name='CGPI (P.G.)')),
                ('dob', models.DateField(verbose_name='DOB')),
                ('active_backlog', models.DecimalField(decimal_places=0, default=0, max_digits=2, verbose_name='Active Backlogs')),
                ('total_backlog', models.DecimalField(decimal_places=0, max_digits=2, verbose_name='Total Backlogs')),
                ('twelveth_year', models.DecimalField(decimal_places=0, max_digits=4, verbose_name='12 Year')),
                ('twelveth_board', models.CharField(default=None, max_length=100, null=True, verbose_name='12 Education Board')),
                ('twelveth_school', models.CharField(max_length=200, null=True, verbose_name='12 School Name')),
                ('twelveth_percent', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='12 Percentage')),
                ('tenth_year', models.DecimalField(decimal_places=0, max_digits=4, verbose_name='10 Year')),
                ('tenth_board', models.CharField(default=None, max_length=100, null=True, verbose_name='10 Education Board')),
                ('tenth_school', models.CharField(max_length=200, null=True, verbose_name='10 School Name')),
                ('tenth_percent', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='10 Percentage')),
                ('domicile_state', models.CharField(choices=[('Rajasthan', 'Rajasthan'), ('Madhya Pradesh', 'Madhya Pradesh'), ('Maharashtra', 'Maharashtra'), ('Uttar Pradesh', 'Uttar Pradesh'), ('Gujarat', 'Gujarat'), ('Karnataka', 'Karnataka'), ('Andhra Pradesh', 'Andhra Pradesh'), ('Odisha', 'Odisha'), ('Chhattisgarh', 'Chhattisgarh'), ('Tamil Nadu', 'Tamil Nadu'), ('Telangana', 'Telangana'), ('Bihar', 'Bihar'), ('West Bengal', 'West Bengal'), ('Arunachal Pradesh', 'Arunachal Pradesh'), ('Jharkhand', 'Jharkhand'), ('Assam', 'Assam'), ('Ladakh', 'Ladakh'), ('Himachal Pradesh', 'Himachal Pradesh'), ('Uttarakhand', 'Uttarakhand'), ('Punjab', 'Punjab'), ('Haryana', 'Haryana'), ('Jammu and Kashmir', 'Jammu and Kashmir'), ('Kerala', 'Kerala'), ('Meghalaya', 'Meghalaya'), ('Manipur', 'Manipur'), ('Mizoram', 'Mizoram'), ('Nagaland', 'Nagaland'), ('Tripura', 'Tripura'), ('Andaman and Nicobar Islands', 'Andaman and Nicobar Islands'), ('Sikkim', 'Sikkim'), ('Goa', 'Goa'), ('Delhi', 'Delhi'), ('Dadra and Nagar Haveli and Daman and Diu', 'Dadra and Nagar Haveli and Daman and Diu'), ('Puducherry', 'Puducherry'), ('Chandigarh', 'Chandigarh'), ('Lakshadweep', 'Lakshadweep')], default=None, max_length=500, null=True, verbose_name='Domicile State')),
                ('domicile_district', models.CharField(default=None, max_length=500, null=True, verbose_name='Domicile District')),
                ('domicile_place', models.CharField(default=None, max_length=500, null=True, verbose_name='Domicile Place')),
                ('cv', models.URLField(null=True, verbose_name='CV Drive URL')),
                ('grad_year', models.DecimalField(decimal_places=0, max_digits=4, verbose_name='Graduation Year')),
                ('curr_batch', models.DecimalField(decimal_places=0, max_digits=4, verbose_name='Admission Year')),
                ('pwd', models.BooleanField(default=False, verbose_name='PwD')),
                ('cluster', models.JSONField(blank=True, null=True, verbose_name='Cluster Prefrences')),
                ('dept', models.CharField(blank=True, choices=[('Electrical Engineering', 'Electrical Engineering'), ('Electronics and Communication Engineering', 'Electronics and Communication Engineering'), ('Civil Engineering', 'Civil Engineering'), ('Material Science and Engineering', 'Material Science and Engineering'), ('Computer Science and Engineering', 'Computer Science and Engineering'), ('Chemical Engineering', 'Chemical Engineering'), ('Mechanical Engineering', 'Mechanical Engineering'), ('Architecture', 'Architecture')], max_length=50, verbose_name='Branch')),
                ('degree', models.CharField(choices=[('B.Tech.', 'B.Tech.'), ('Dual Degree (B.Tech. + M.Tech.)', 'Dual Degree (B.Tech. + M.Tech.)'), ('B.Arch.', 'B.Arch.')], max_length=50, verbose_name='Degree')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('sub_code', models.CharField(max_length=8, primary_key=True, serialize=False, verbose_name='Subject Code')),
                ('sub_name', models.CharField(max_length=100, verbose_name='Subject Name')),
                ('dept', models.CharField(choices=[('Electrical Engineering', 'Electrical Engineering'), ('Electronics and Communication Engineering', 'Electronics and Communication Engineering'), ('Civil Engineering', 'Civil Engineering'), ('Material Science and Engineering', 'Material Science and Engineering'), ('Computer Science and Engineering', 'Computer Science and Engineering'), ('Chemical Engineering', 'Chemical Engineering'), ('Mechanical Engineering', 'Mechanical Engineering'), ('Architecture', 'Architecture')], max_length=50, verbose_name='Subject Department')),
                ('credits', models.PositiveSmallIntegerField(verbose_name='Credits')),
            ],
        ),
        migrations.CreateModel(
            name='ResultSummary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester', models.PositiveSmallIntegerField(verbose_name='Semester Number')),
                ('cgpi', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='CGPI')),
                ('sgpi', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True, verbose_name='SGPI')),
                ('sem_credits', models.PositiveSmallIntegerField(verbose_name='Semester Credits')),
                ('total_credits', models.PositiveSmallIntegerField(verbose_name='Cumalative Total Credits')),
                ('roll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.student', verbose_name='Roll Number')),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.PositiveSmallIntegerField(verbose_name='Grade')),
                ('semester', models.PositiveSmallIntegerField(verbose_name='Semester Number')),
                ('roll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.student', verbose_name='Roll Number')),
                ('sub_code', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.subject', verbose_name='Subject Code')),
            ],
        ),
        migrations.CreateModel(
            name='PlacementsAndInterns',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stipend', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True, verbose_name='Intern Stipend')),
                ('intern_on_campus', models.BooleanField(blank=True, null=True, verbose_name='Intern on Campus')),
                ('intern', models.BooleanField(blank=True, default=False, null=True, verbose_name='Intern')),
                ('job', models.BooleanField(blank=True, default=False, null=True, verbose_name='Job')),
                ('first_ctc', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True, verbose_name='First CTC')),
                ('first_job_on_campus', models.BooleanField(blank=True, null=True, verbose_name='First Job on campus')),
                ('second_ctc', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True, verbose_name='Second CTC')),
                ('second_job_on_campus', models.BooleanField(blank=True, null=True, verbose_name='Second Job on campus')),
                ('plus_placement', models.JSONField(blank=True, null=True, verbose_name='Additional Placement JSON')),
                ('no_of_placements', models.DecimalField(decimal_places=0, default=0, max_digits=2, verbose_name='Placement Count')),
                ('company_intern', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='intern_company', to='core.company', verbose_name='Intern Company')),
                ('first_company_placement', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='first_job_company', to='core.company', verbose_name='First Job Company')),
                ('roll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.student', verbose_name='Roll Number')),
                ('second_company_placement', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='second_job_company', to='core.company', verbose_name='Second Job Company')),
            ],
        ),
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('is_student', models.BooleanField(default=True, help_text='Designates that this user is a student', verbose_name='Student Status')),
                ('is_tpr', models.BooleanField(default=False, help_text='Designates that this student has TPR level permissions', verbose_name='TPR Status')),
                ('is_core_tpr', models.BooleanField(default=False, help_text='Designates that this student has Core TPR level permissions', verbose_name='Core TPR status')),
                ('is_jtpr', models.BooleanField(default=False, help_text='Designates that this student has JTPR level permissions', verbose_name='JTPR Status')),
                ('nith_email', models.EmailField(blank=True, max_length=254, null=True, validators=[django.core.validators.RegexValidator(regex='([A-Za-z0-9]+)@nith\\.ac\\.in')], verbose_name='NITH Email Address')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('roll', models.OneToOneField(blank=True, help_text='Student association if the user is a student.', null=True, on_delete=django.db.models.deletion.CASCADE, to='core.student', verbose_name='Roll Number (If Student)')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AddConstraint(
            model_name='resultsummary',
            constraint=models.UniqueConstraint(fields=('roll', 'semester'), name='unique_summary'),
        ),
        migrations.AddConstraint(
            model_name='result',
            constraint=models.UniqueConstraint(fields=('sub_code', 'semester', 'roll'), name='unique_result'),
        ),
        migrations.AddConstraint(
            model_name='placementsandinterns',
            constraint=models.UniqueConstraint(fields=('roll',), name='unique_record'),
        ),
    ]
