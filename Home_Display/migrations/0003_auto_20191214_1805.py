# Generated by Django 3.0 on 2019-12-15 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home_Display', '0002_datetime_financialdata'),
    ]

    operations = [
        migrations.AddField(
            model_name='financialdata',
            name='networth',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='financialdata',
            name='total_assets',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='financialdata',
            name='total_liabilities',
            field=models.FloatField(default=0),
        ),
    ]
