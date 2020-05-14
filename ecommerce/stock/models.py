from django.db import models

# Create your models here.
class Stock(models.Model):
    category = models.CharField(max_length=50, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    cnt = models.IntegerField(blank=True, null=True)
    img = models.CharField(max_length=255, blank=True, null=True)
    createdat = models.DateTimeField(db_column='createdAt', blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'stock'