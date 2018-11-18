# Generated by Django 2.0.1 on 2018-11-18 07:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_auto_20181118_0703'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patient_detail',
            old_name='email',
            new_name='user_email',
        ),
        migrations.AlterField(
            model_name='patient_detail',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]