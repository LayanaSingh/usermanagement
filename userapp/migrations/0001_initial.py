# Generated by Django 5.0.6 on 2024-06-14 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('DOB', models.DateField()),
                ('Contact', models.IntegerField()),
                ('Nationality', models.CharField(max_length=200, null=True)),
                ('Education', models.CharField(max_length=200, null=True)),
                ('Skills', models.CharField(max_length=400, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Education_1', models.CharField(max_length=200, null=True)),
                ('College', models.CharField(max_length=200, null=True)),
                ('Education_2', models.CharField(blank=True, max_length=200, null=True)),
                ('College_2', models.CharField(blank=True, max_length=200, null=True)),
                ('Work_1', models.CharField(max_length=500, null=True)),
                ('Work_2', models.CharField(blank=True, max_length=500, null=True)),
                ('Work_3', models.CharField(blank=True, max_length=500, null=True)),
                ('Project_1', models.CharField(max_length=500, null=True)),
                ('Project_2', models.CharField(blank=True, max_length=500, null=True)),
                ('Project_3', models.CharField(blank=True, max_length=500, null=True)),
                ('Project_4', models.CharField(blank=True, max_length=500, null=True)),
                ('Project_5', models.CharField(blank=True, max_length=500, null=True)),
                ('Project_6', models.CharField(blank=True, max_length=500, null=True)),
                ('Certification_1', models.CharField(max_length=400, null=True)),
                ('Certification_2', models.CharField(blank=True, max_length=400, null=True)),
                ('Certification_3', models.CharField(blank=True, max_length=400, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='media/')),
                ('Description', models.TextField(max_length=2000)),
                ('Link', models.CharField(max_length=200)),
                ('Project_Name', models.CharField(default='Unnamed_project', max_length=500, null=True)),
            ],
        ),
    ]
