# Generated by Django 4.1.2 on 2022-10-18 12:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0006_delete_login_employee_employee_code'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='supervisors',
            new_name='supervisor',
        ),
    ]
