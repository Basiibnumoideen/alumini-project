# Generated by Django 3.2.13 on 2022-06-14 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20220614_1513'),
    ]

    operations = [
        migrations.AddField(
            model_name='college_details',
            name='fax',
            field=models.CharField(default=2, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='college_details',
            name='contact',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='college_details',
            name='pin',
            field=models.CharField(max_length=100),
        ),
    ]
