# Generated by Django 2.2.5 on 2019-09-20 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20190920_1336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='label',
            field=models.CharField(choices=[('New', 'success'), ('Hot', 'danger'), ('Discount', 'warning'), ('De', 'Default')], max_length=2),
        ),
    ]
