# Generated by Django 3.0.5 on 2021-11-07 09:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_auto_20211107_0921'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ingredient',
            name='amount',
        ),
    ]
