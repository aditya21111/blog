# Generated by Django 3.1.4 on 2021-01-08 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('msg_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=300)),
                ('phone', models.CharField(default='', max_length=50)),
                ('desc', models.CharField(default='', max_length=300)),
                ('time_stamp', models.DateTimeField(default="2021-01-24 04:12:52.268804"),
                )
            ],
        ),
    ]
