# Generated by Django 2.2.9 on 2020-01-12 20:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('agendas', '0009_auto_20200112_2008'),
        ('minutes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='minutes',
            name='assoc_agenda',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='agendas.Agenda', verbose_name='Associated Agenda'),
        ),
    ]
