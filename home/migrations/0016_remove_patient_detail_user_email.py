# Generated by Django 2.0.1 on 2018-11-18 07:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_auto_20181118_0716'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient_detail',
            name='user_email',
        ),
    ]