# Generated by Django 4.1.3 on 2022-11-30 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentTable',
            fields=[
                ('StudentID', models.AutoField(primary_key=True, serialize=False)),
                ('StudentName', models.CharField(max_length=500)),
                ('Age', models.IntegerField()),
                ('DOB', models.DateField()),
                ('Grade', models.CharField(max_length=500)),
            ],
        ),
    ]