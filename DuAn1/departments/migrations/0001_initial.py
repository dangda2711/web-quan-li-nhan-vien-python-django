# Generated by Django 3.2.9 on 2022-10-19 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='department',
            fields=[
                ('dempartment_id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('department_name', models.CharField(max_length=100, unique=True)),
                ('department_addr', models.CharField(max_length=100)),
                ('created_date_dp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
