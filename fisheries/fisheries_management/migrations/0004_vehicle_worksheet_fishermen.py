# Generated by Django 4.2.2 on 2023-06-19 19:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fisheries_management', '0003_alter_marina_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('VId', models.AutoField(primary_key=True, serialize=False)),
                ('VName', models.CharField(max_length=20)),
                ('VOwner', models.CharField(max_length=30)),
                ('Ownerphone', models.IntegerField(default=False)),
                ('Password', models.CharField(max_length=16)),
                ('C_password', models.CharField(max_length=16)),
                ('MId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fisheries_management.marina')),
            ],
            options={
                'db_table': 'vehicle',
            },
        ),
        migrations.CreateModel(
            name='Worksheet',
            fields=[
                ('WId', models.AutoField(primary_key=True, serialize=False)),
                ('Fishspecie', models.CharField(max_length=20)),
                ('quantity', models.IntegerField(default=False)),
                ('Date', models.DateField()),
                ('price', models.IntegerField(default=False)),
                ('VId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fisheries_management.vehicle')),
            ],
            options={
                'db_table': 'worksheet',
            },
        ),
        migrations.CreateModel(
            name='Fishermen',
            fields=[
                ('FId', models.AutoField(primary_key=True, serialize=False)),
                ('FName', models.CharField(max_length=30)),
                ('Address', models.CharField(max_length=20)),
                ('Phonenumber', models.IntegerField(default=False)),
                ('VId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fisheries_management.vehicle')),
            ],
            options={
                'db_table': 'fishermen',
            },
        ),
    ]
