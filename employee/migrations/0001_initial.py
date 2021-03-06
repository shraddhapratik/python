# Generated by Django 2.1.5 on 2019-02-13 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('eid', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('ename', models.CharField(max_length=100)),
                ('eemail', models.EmailField(max_length=254)),
                ('econtact', models.CharField(max_length=15)),
                ('eage', models.IntegerField()),
                ('esalary', models.IntegerField()),
                ('eaddress', models.CharField(max_length=300)),
            ],
            options={
                'db_table': 'emp_info',
            },
        ),
    ]
