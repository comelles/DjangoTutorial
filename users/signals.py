from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile

#Se pueden poner dentro de models.py, pero el codigo separado es mejor
#Para que django sepa triggerear estas signals hay q agregarlas en apps.py
# def ready(self):
#        import users.signals


#@receiver(post_save, sender=Profile)  #lo mismo q los signals de abajo.
def createProfile(sender, instance, created, **kwargs):
    print('funciona!')
    if created:
        user = instance
        profile = Profile.objects.create(user=user,
                                        username=user.username, 
                                        email=user.email,
                                        name=user.first_name)


#@receiver(post_delete, sender=Profile)  #lo mismo q los signals de abajo.
def deleteUser(sender, instance, **kwargs):
    user = instance.user
    user.delete()
    


post_save.connect(createProfile, sender=User)
post_delete.connect(deleteUser, sender=Profile)
#Signals, lo mismo q decorator + receiver
