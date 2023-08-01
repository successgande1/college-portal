# Generated by Django 4.0 on 2023-07-31 23:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('academics', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Applicant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_status', models.BooleanField(default=False)),
                ('admitted', models.BooleanField(default=False)),
                ('added_date', models.DateField(auto_now_add=True)),
                ('applicant', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
                ('course_name', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='academics.courseofstudy')),
            ],
        ),
        migrations.CreateModel(
            name='SchoolsAttended',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school', models.CharField(blank=True, choices=[('PRIMARY SCHOOL ', 'PRIMARY SCHOOL'), ('SECONDARY SCHOOL', 'SECONDARY SCHOOL'), ('NCE', 'NCE'), ('ND', 'ND')], default=None, max_length=20, null=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admission.applicant')),
            ],
        ),
    ]
