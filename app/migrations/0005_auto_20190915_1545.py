# Generated by Django 2.2.5 on 2019-09-15 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20190913_1719'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='child',
            options={'verbose_name_plural': 'children'},
        ),
        migrations.AlterField(
            model_name='child',
            name='weight',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]
