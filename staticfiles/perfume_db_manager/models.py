# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Perfumes(models.Model):
    id = models.BigIntegerField(primary_key=True)
    brand = models.TextField()
    name = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    launch_year = models.TextField(blank=True, null=True)
    main_accords = models.JSONField(blank=True, null=True)
    notes = models.JSONField(blank=True, null=True)
    longevity = models.JSONField(blank=True, null=True)
    sillage = models.JSONField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'perfume_test'
        db_table_comment = 'testing supabase creat table'
