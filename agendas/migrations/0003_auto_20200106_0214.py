# Generated by Django 2.2.9 on 2020-01-06 02:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtaildocs', '0010_document_file_hash'),
        ('agendas', '0002_auto_20200105_1623'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agenda',
            name='agenda_or_minutes',
        ),
        migrations.CreateModel(
            name='Minutes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Date of Meeting')),
                ('general_or_special', models.CharField(choices=[('general', 'General'), ('special', 'Special')], default='general', max_length=10, null=True)),
                ('assoc_agenda', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtaildocs.Document', verbose_name='Associated Agenda')),
                ('document', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtaildocs.Document', verbose_name='Minutes PDF')),
            ],
        ),
    ]