# Generated by Django 4.1.2 on 2022-10-11 13:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_remove_employee_position_employee_positio'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='positio',
            new_name='position',
        ),
    ]
