# Generated by Django 2.2.9 on 2020-01-12 20:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agendas', '0008_auto_20200112_0252'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agenda',
            name='assoc_minutes',
        ),
        migrations.DeleteModel(
            name='Minutes',
        ),
    ]