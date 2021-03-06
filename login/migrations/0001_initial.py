# Generated by Django 3.1.1 on 2020-11-04 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(max_length=100)),
                ('designation', models.CharField(max_length=200)),
                ('profileimage', models.ImageField(blank=True, default='defaultimage', null=True, upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='profileimage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='defaultname', max_length=50)),
                ('profile_image', models.ImageField(default='defaultimage', upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='UserReportModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=800)),
                ('feedback', models.CharField(max_length=500)),
                ('date', models.DateField(max_length=500)),
                ('time', models.TimeField()),
            ],
        ),
    ]
