# Generated by Django 4.1.2 on 2022-10-16 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutmecontent',
            name='description',
            field=models.CharField(max_length=1200),
        ),
    ]
