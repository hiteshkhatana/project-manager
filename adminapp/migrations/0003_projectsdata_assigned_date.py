# Generated by Django 3.0.2 on 2021-08-20 12:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0002_employeesdata_projectsdata'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectsdata',
            name='assigned_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]