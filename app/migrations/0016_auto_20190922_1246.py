# Generated by Django 2.2.5 on 2019-09-22 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_auto_20190921_1223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('Clock', 'Clock'), ('Cabinet', 'Cabinet')], max_length=5),
        ),
    ]
