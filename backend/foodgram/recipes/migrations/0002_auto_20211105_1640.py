# Generated by Django 3.0.5 on 2021-11-05 16:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ingredient',
            old_name='measure',
            new_name='measurement_unit',
        ),
        migrations.RenameField(
            model_name='ingredient',
            old_name='title',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='recipe',
            old_name='title',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='tag',
            old_name='title',
            new_name='name',
        ),
    ]
