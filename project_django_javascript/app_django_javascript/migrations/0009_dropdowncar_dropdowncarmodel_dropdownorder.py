# Generated by Django 3.1.7 on 2021-02-28 10:37

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_django_javascript', '0008_delete_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='DropdownCar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='DropdownCarModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_django_javascript.dropdowncar')),
            ],
        ),
        migrations.CreateModel(
            name='DropdownOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_nr', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('description', models.CharField(default='...', max_length=50)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_django_javascript.dropdowncar')),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_django_javascript.dropdowncarmodel')),
            ],
        ),
    ]