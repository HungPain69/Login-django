# Generated by Django 2.2.5 on 2019-09-21 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_auto_20190921_0338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='label',
            field=models.CharField(choices=[('N', 'New'), ('H', 'Hot'), ('D', 'Discount'), ('De', 'Default')], max_length=2),
        ),
    ]
