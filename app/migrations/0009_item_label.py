# Generated by Django 2.2.5 on 2019-09-20 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20190920_1145'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='label',
            field=models.CharField(choices=[('N', 'New'), ('H', 'Hot'), ('D', 'Discount')], default=1, max_length=2),
            preserve_default=False,
        ),
    ]
