# Generated by Django 2.2.5 on 2019-09-18 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operations', '0013_auto_20190915_1918'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='discounted_price',
            field=models.IntegerField(default=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='original_price',
            field=models.IntegerField(default=150),
            preserve_default=False,
        ),
    ]
