from django.db import models
from django.contrib.auth.models import User

class MyUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(name='Фото профиля',width_field=100, height_field=100)
    bio = models.CharField(name='Описание')


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        MyUser.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()