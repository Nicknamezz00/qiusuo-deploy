# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or
# field names.
from django.db import models


class School(models.Model):
    id = models.IntegerField(primary_key=True)
    school_id = models.CharField(max_length=20, blank=True, null=True)
    school_name = models.CharField(max_length=255, blank=True, null=True)
    province_id = models.CharField(max_length=20, blank=True, null=True)
    province_name = models.CharField(max_length=255, blank=True, null=True)
    city_id = models.CharField(max_length=20, blank=True, null=True)
    city_name = models.CharField(max_length=255, blank=True, null=True)
    level = models.CharField(max_length=255, blank=True, null=True)
    department = models.CharField(max_length=255, blank=True, null=True)
    other = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.school_name

    class Meta:
        managed = False
        db_table = 'school'
        verbose_name = 'school'
        verbose_name_plural = verbose_name + 's'
