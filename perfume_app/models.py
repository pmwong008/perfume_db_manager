from django.db import models

# Create your models here.
from django.db import models

from perfume_db_manager.models import Perfumes

'''
class Perfumes(models.Model):
    id = models.AutoField(primary_key=True)
    brand = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    launch_year = models.TextField(blank=True, null=True)
    main_accords = models.JSONField(blank=True, null=True)
    notes = models.JSONField(blank=True, null=True)
    longevity = models.JSONField(blank=True, null=True)
    sillage = models.JSONField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'perfumes'
        
'''