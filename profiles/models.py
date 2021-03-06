from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from django_countries.fields import CountryField


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_full_name = models.CharField(
        max_length=70, null=True, blank=True)
    default_email = models.CharField(
        max_length=50, null=True, blank=True)
    default_phone_number = models.CharField(
        max_length=13, null=True, blank=True)
    default_street_address = models.CharField(
        max_length=80, null=True, blank=True)
    default_house_number = models.CharField(
        max_length=10, null=True, blank=True)
    default_addition = models.CharField(max_length=5, null=True, blank=True)
    default_postcode = models.CharField(max_length=6, null=True, blank=True)
    default_city = models.CharField(max_length=40, null=True, blank=True)
    default_country = CountryField(null=True, blank=True)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
        instance.userprofile.save()
