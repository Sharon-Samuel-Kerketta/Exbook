# Generated by Django 2.2.5 on 2019-09-15 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isbn', models.CharField(max_length=13, null=True)),
                ('name', models.CharField(max_length=255)),
                ('publisher', models.CharField(max_length=255, null=True)),
                ('condition', models.IntegerField()),
                ('language', models.CharField(max_length=15)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
