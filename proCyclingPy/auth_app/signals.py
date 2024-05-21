from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from proCyclingPy.cyclist.models import Cyclist
from proCyclingPy.team_manager.models import TeamManager

UserModel = get_user_model()

@receiver(post_save, sender=UserModel)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.role == 'Cyclist':
            Cyclist.objects.create(user=instance)
        elif instance.role == 'Team Manager':
            TeamManager.objects.create(user=instance)
