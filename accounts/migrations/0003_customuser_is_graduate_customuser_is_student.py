# Generated by Django 4.0 on 2023-08-01 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_customuser_alter_profile_user_alter_usercontact_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='is_graduate',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='customuser',
            name='is_student',
            field=models.BooleanField(default=False),
        ),
    ]