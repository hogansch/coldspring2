# Generated by Django 2.2.9 on 2020-01-05 06:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0041_group_collection_permissions_verbose_name_plural'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trustee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(help_text='First and last name', max_length=100)),
                ('position', models.CharField(help_text='Position', max_length=100)),
                ('term_start', models.CharField(help_text='Year that term started', max_length=4)),
                ('term_end', models.CharField(help_text='Year that term ends', max_length=4)),
            ],
            options={
                'verbose_name': 'Trustee',
                'verbose_name_plural': 'Trustees',
                'db_table': 'Trustee',
            },
        ),
        migrations.CreateModel(
            name='TrusteesPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('submenutitle', models.CharField(max_length=100, null=True, verbose_name='Submenu title')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]