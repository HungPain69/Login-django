# Generated by Django 2.2.5 on 2019-09-21 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_auto_20190920_1434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='label',
            field=models.CharField(choices=[('success', 'New'), ('danger', 'Hot'), ('warning', 'Discount'), ('De', 'Default')], max_length=10),
        ),
    ]