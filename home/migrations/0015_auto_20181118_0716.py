# Generated by Django 2.0.1 on 2018-11-18 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_auto_20181118_0712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient_detail',
            name='user_email',
            field=models.CharField(max_length=40),
        ),
    ]
