# Generated by Django 3.2.16 on 2022-12-20 07:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0014_remove_college_details_fax'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alumni_details',
            name='reg_date',
        ),
    ]