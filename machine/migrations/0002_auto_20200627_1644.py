# Generated by Django 3.0.6 on 2020-06-27 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('machine', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='breastcancerchecker',
            name='mean_area',
            field=models.FloatField(default=1001.0, null=True),
        ),
        migrations.AlterField(
            model_name='breastcancerchecker',
            name='mean_perimeter',
            field=models.FloatField(default=122.8, null=True),
        ),
        migrations.AlterField(
            model_name='breastcancerchecker',
            name='mean_radius',
            field=models.FloatField(default=17.99, null=True),
        ),
        migrations.AlterField(
            model_name='breastcancerchecker',
            name='mean_smoothness',
            field=models.FloatField(default=0.1184, null=True),
        ),
        migrations.AlterField(
            model_name='breastcancerchecker',
            name='mean_texture',
            field=models.FloatField(default=10.38, null=True),
        ),
    ]
