from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Patient_Detail(models.Model):
    # MALE = 'male'
    # FEMALE = 'female'
    # UNDEFINED = 'undefined'
    #
    # GENDER_CHOICES = (
    #     (MALE, 'Male'),
    #     (FEMALE, 'Female'),
    #     (UNDEFINED, 'Undefined')
    # )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=40)
    IP=models.CharField(max_length=30)
    gender=models.CharField(max_length=10)
    user_email=models.CharField(max_length=40)
    balance_due=models.IntegerField(default=0)
    total=models.IntegerField(default=0)

    @receiver(post_save, sender=User)
    def update_user_profile(sender, instance, created, **kwargs):
        try:
            if created:
                Patient_Detail.objects.create(user=instance)
            instance.profile.save()
        except Exception as e:
            pass

    def __str__(self):
        return self.name

class Hospital(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name
