# Generated by Django 4.2.5 on 2023-09-15 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0003_alter_person_added'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='country',
            field=models.CharField(default='', max_length=50, unique=True),
        ),
        migrations.AddField(
            model_name='person',
            name='stack',
            field=models.CharField(default='', max_length=30),
        ),
    ]
