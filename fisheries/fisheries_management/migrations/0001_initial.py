# Generated by Django 4.2.2 on 2023-06-18 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Marina',
            fields=[
                ('Mid', models.AutoField(primary_key=True, serialize=False)),
                ('Mname', models.CharField(max_length=20)),
                ('location', models.CharField(max_length=20)),
            ],
        ),
    ]
