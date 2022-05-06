import logging

from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save

logger = logging.getLogger(__name__)


class Category(models.Model):
    name = models.CharField(max_length=200, null=True)
    image = models.CharField(max_length=200, null=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return f'{self.id} : {self.name}'


class Sale(models.Model):
    name = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=200, null=True)
    date = models.DateTimeField(null=True)
    image = models.CharField(max_length=200, null=True)

    def __str__(self):
        return f'{self.id} : {self.name}'


class Sub_category(models.Model):
    name = models.CharField(max_length=200, null=True)
    image = models.CharField(max_length=200, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.id} : {self.name}'

    class Meta:
        verbose_name = 'Subcategory'
        verbose_name_plural = 'Subcategories'


class Product(models.Model):
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField(max_length=200, null=True)
    description = models.CharField(max_length=200, null=True)
    image = models.CharField(max_length=200, null=True)
    rating = models.FloatField(max_length=200, null=True)
    sub_category = models.ForeignKey(Sub_category, related_name="products", on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.id} : {self.name}'


class AppealManager(models.Manager):
    def get_active(self):
        return self.filter(is_active=True)


class Appeal(models.Model):
    title = models.CharField(max_length=200, null=True)
    file = models.FileField(default=None)
    is_active = models.BooleanField(default=True)

    objects = AppealManager()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    first_name = models.CharField(max_length=200, blank=True, null=True)
    last_name = models.CharField(max_length=200, blank=True, null=True)
    phone = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.user.username


def create_profile(sender, instance, created, **kwargs):
    logger.warning('Created')
    if created:
        Profile.objects.create(user=instance)
        print('Profile created')


post_save.connect(create_profile, sender=User)


def updated_profile(sender, instance, created, **kwargs):
    logger.warning('Updated')
    if not created:
        instance.profile.save()


post_save.connect(updated_profile, sender=User)
