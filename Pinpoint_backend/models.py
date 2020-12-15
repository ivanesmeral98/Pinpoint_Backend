# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=128, blank=True, null=True)
    personal_map = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'

class CollaborativeMap(models.Model):
    id = models.IntegerField(primary_key=True)
    map_id = models.IntegerField(blank=True, null=True)
    author = models.IntegerField(blank=True, null=True)
    collaborator = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'collaborative_map'

class Friendship(models.Model):
    id = models.IntegerField(primary_key=True)
    requestee = models.ForeignKey('UserProfile', models.DO_NOTHING, related_name='requestee', db_column='requestee', blank=True, null=True)
    acceptor = models.ForeignKey('UserProfile', models.DO_NOTHING, related_name='acceptor', db_column='acceptor', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'friendship'

class Map(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=128, blank=True, null=True)
    creator = models.CharField(max_length=128, blank=True, null=True)
    city = models.CharField(max_length=128, blank=True, null=True)
    state = models.CharField(max_length=128, blank=True, null=True)
    country = models.CharField(max_length=128, blank=True, null=True)
    is_collaborative = models.BooleanField(blank=True, null=True)
    is_preview_allowed = models.BooleanField(blank=True, null=True)
    is_public = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'maps'

class Notification(models.Model):
    id = models.IntegerField(primary_key=True)
    is_read = models.BooleanField(blank=True, null=True)
    content = models.CharField(max_length=128, blank=True, null=True)
    to_user = models.ForeignKey('UserProfile', models.DO_NOTHING, db_column='to_user', blank=True, null=True)
    caused_by = models.TextField(blank=True, null=True)  # This field type is a guess.
    notif_image = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'notifications'

class Pin(models.Model):
    id = models.IntegerField(primary_key=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    address = models.CharField(db_column='Address', max_length=128, blank=True, null=True)  # Field name made lowercase.
    rating = models.IntegerField(blank=True, null=True)
    map = models.ForeignKey(Map, models.DO_NOTHING, blank=True, null=True)
    type = models.TextField(blank=True, null=True)  # This field type is a guess.
    pin_image = models.IntegerField(blank=True, null=True)
    author = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pins'

class Request(models.Model):
    id = models.IntegerField(primary_key=True)
    is_accepted = models.BooleanField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    to_user = models.ForeignKey('UserProfile', models.DO_NOTHING, related_name='to_user', db_column='to_user', blank=True, null=True)
    from_user = models.ForeignKey('UserProfile', models.DO_NOTHING, related_name='from_user', db_column='from_user', blank=True, null=True)
    type = models.TextField(blank=True, null=True)  # This field type is a guess.
    request_image = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'requests'

class Review(models.Model):
    id = models.IntegerField(primary_key=True)
    author = models.ForeignKey('UserProfile', models.DO_NOTHING, db_column='author', blank=True, null=True)
    is_good = models.BooleanField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    for_pin = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reviews'

class Tag(models.Model):
    id = models.IntegerField(primary_key=True)
    type = models.CharField(max_length=128, blank=True, null=True)
    image = models.IntegerField(blank=True, null=True)
    text = models.CharField(max_length=128, blank=True, null=True)
    review = models.ForeignKey(Review, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tag'