from django.db import models
from django.contrib.auth.models import User

# Use signals for automatically created/updated a Profile
# when we create/update User instances
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    STUDENT = 1
    TEACHER = 2
    SUPERVISOR = 3
    ROLE_CHOICES = (
        (STUDENT, 'Student'),
        (TEACHER, 'Teacher'),
        (SUPERVISOR, 'Supervisor'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, null=True, blank=True)
    email_confirmed = models.BooleanField(default=False)

    def __str__(self):
    	return self.user.username

    def get_role_name(self, role):
        return dict(self.ROLE_CHOICES).get(role)
    

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()