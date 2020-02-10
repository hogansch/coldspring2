# Generated by Django 2.2.9 on 2020-01-05 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='staffmember',
            name='staff_category',
            field=models.CharField(choices=[('teacher', 'Teacher'), ('specialist', 'Specialist'), ('office', 'Office Staff')], max_length=10, null=True),
        ),
    ]
