# Generated by Django 3.1.2 on 2020-10-27 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0016_merge_20201026_1859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='idProd',
            field=models.IntegerField(default=1, help_text='Id única del producto', primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]