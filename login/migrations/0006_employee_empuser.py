# Generated by Django 3.1.1 on 2020-11-04 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0005_remove_employee_empuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='empuser',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
