# Generated by Django 3.1.4 on 2021-01-27 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0091_auto_20210126_0443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='pic',
            field=models.ImageField(blank=True, null=True, upload_to='home/images'),
        ),
    ]
