# Generated by Django 3.2.9 on 2022-10-19 13:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('departments', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='employee',
            fields=[
                ('employee_id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('emmployee_name', models.CharField(max_length=100, unique=True)),
                ('date_of_birth', models.DateField()),
                ('employee_addr', models.TextField(blank=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('avatar', models.ImageField(default=None, upload_to='images')),
                ('cv', models.FileField(default=None, upload_to='files')),
                ('active', models.BooleanField(default=True)),
                ('department_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='departments.department')),
            ],
        ),
    ]
