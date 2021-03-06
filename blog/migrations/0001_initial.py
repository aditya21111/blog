# Generated by Django 3.1.4 on 2021-01-08 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blogpost',
            fields=[
                ('post_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(default='', max_length=100)),
                ('pub_date', models.DateField(default=1)),
                ('writer', models.CharField(default='', max_length=60)),
                ('postimgdesc', models.CharField(default='', max_length=200)),
                ('para1', models.CharField(default='', max_length=3000)),
                ('head0', models.CharField(blank=True, default='', max_length=150)),
                ('head0para', models.CharField(default='', max_length=4000)),
                ('category', models.CharField(default='', max_length=15)),
                ('head1', models.CharField(blank=True, default='', max_length=150)),
                ('head1para', models.CharField(blank=True, default='', max_length=2000)),
                ('head2', models.CharField(blank=True, default='', max_length=150)),
                ('head2para', models.CharField(blank=True, default='', max_length=2000)),
                ('thumbnail', models.ImageField(default='', upload_to='media/blog/images')),
            ],
        ),
    ]
