# Generated by Django 2.2.18 on 2021-05-14 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0002_auto_20210514_2221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='fecha_accidente',
            field=models.DateField(blank=True, default=None, null=True),
        ),
    ]
