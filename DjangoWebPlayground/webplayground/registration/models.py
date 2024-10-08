from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.dispatch import receiver
from django.db.models.signals import post_save

def custom_upload_to(instance, filename):
    old_instance = Profile.objects.get(pk=instance.pk)
    old_instance.avatar.delete()
    return 'profile/' + filename

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Usuario")
    avatar = models.ImageField(upload_to=custom_upload_to, null=True, blank=True, verbose_name="Imagen del usuario")
    bio = RichTextField(null=True, blank=True, verbose_name="Biografia del usuario")
    link = models.URLField(max_length=200, null=True, blank=True, verbose_name="link del usuario")

    class Meta:
        verbose_name = "Perfil"
        verbose_name_plural = "Perfiles"
        ordering = ['user__username',]

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def ensure_profile_exists(sender, instance, **kwargs):
    if kwargs.get("created", False):
        Profile.objects.get_or_create(user=instance)