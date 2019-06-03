from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import MinValueValidator,MaxValueValidator

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='profile')
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    bio = models.CharField(max_length=100)
    profile_pic = models.ImageField(upload_to='profile/')
    pub_date_created = models.DateTimeField(auto_now_add=True, null=True)
    neighbourhood = models.ForeignKey('Neighbourhood', blank=True, null=True)

    def __str__(self):
        return self.first_name

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    @classmethod
    def get_profiles(cls):
        profiles = cls.objects.all()
        return profiles


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class Neighbourhood(models.Model):
    name = models.CharField(max_length = 300)
    image = models.ImageField(upload_to='neighimage/', null=True)
    admin = models.ForeignKey(Profile, related_name='hoods', null=True)
    description = models.CharField(max_length = 300,default='My hood!!!')

class Business(models.Model):
    name = models.CharField(max_length=30)
    category = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=10)
    image = models.ImageField(upload_to='bsimage/')
    description = models.CharField(max_length = 300)
    neighbourhood = models.ForeignKey(Neighbourhood, related_name='businesses')
    profile = models.ForeignKey(Profile, related_name='profiles')

    @classmethod
    def search_by_name(cls,search_term):
        business = cls.objects.filter(title__icontains=search_term)
        return business

class Post(models.Model):
    user = models.ForeignKey(Profile, related_name='profile')
    post = models.CharField(max_length=30)
    neighbourhood = models.ForeignKey(Neighbourhood, related_name='posts')

class Location(models.Model):
    name = models.CharField(max_length=30)

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=30)

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

    def __str__(self):
        return self.name
