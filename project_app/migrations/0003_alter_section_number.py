# Generated by Django 4.1.7 on 2023-05-18 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_app', '0002_remove_section_tas_section_ta_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='section',
            name='number',
            field=models.CharField(max_length=3),
        ),
    ]
