from email.policy import default
from pyexpat import model
from django.db import models
import uuid

from users.models import Profile
# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=200)
    owner = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.CASCADE)
    desc = models.TextField(null=True, blank=True) #null es para la BBDD, blank para el front
    featured_image = models.ImageField(null=True, blank=True, default='default.jpg')
    demoLink = models.CharField(max_length=200, null=True, blank=True)
    sourceLink = models.CharField(max_length=200, null=True, blank=True)
    tags = models.ManyToManyField('Tag', blank= True)
    vote_total = models.IntegerField(default= 0, null=True, blank=True)
    vote_ratio = models.IntegerField(default=0, null= True, blank=True)
    created = models.DateTimeField(auto_now_add=True) #crea TimeStamp automaticamente
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    def __str__(self):
        return self.title

class Review(models.Model):
    VOTE_TYPE = (
        ('up', 'Up Vote'), ('down', 'Down Vote')
    ) #Tupla para la votación
    #owner =
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    body =  models.TextField(null=True, blank=True) #null es para la BBDD, blank para el front
    value = models.CharField(max_length=200, choices=VOTE_TYPE)
    created = models.DateTimeField(auto_now_add=True) #crea TimeStamp automaticamente
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.value

class Tag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True) #crea TimeStamp automaticamente
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    def __str__(self):
        return self.name



