# Generated by Django 4.1.2 on 2022-10-15 18:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='techstack',
            options={'ordering': ['-category']},
        ),
    ]
