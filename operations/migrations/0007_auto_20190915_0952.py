# Generated by Django 2.2.5 on 2019-09-15 09:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('operations', '0006_auto_20190915_0951'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'verbose_name_plural': 'Author'},
        ),
        migrations.AlterModelOptions(
            name='book',
            options={'verbose_name_plural': 'Book'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Category'},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name_plural': 'User'},
        ),
    ]
