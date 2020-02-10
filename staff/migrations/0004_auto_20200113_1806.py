# Generated by Django 2.2.9 on 2020-01-13 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0003_auto_20200105_0702'),
    ]

    operations = [
        migrations.AddField(
            model_name='staffmember',
            name='ext',
            field=models.IntegerField(blank=True, max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='staffmember',
            name='staff_category',
            field=models.CharField(choices=[('teacher', 'Teacher'), ('specialist', 'Specialist'), ('admini', 'Administrative Staff'), ('other', 'Other')], default='teacher', max_length=100, null=True),
        ),
    ]