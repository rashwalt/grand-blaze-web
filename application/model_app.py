# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from django.db import models

class BazzerHistories(models.Model):
    id = models.IntegerField(primary_key=True)
    buyer_no = models.IntegerField()
    buyer_name = models.CharField(max_length=720, blank=True)
    seller_no = models.IntegerField()
    seller_name = models.CharField(max_length=720, blank=True)
    item_id = models.IntegerField()
    buy_count = models.IntegerField()
    price = models.IntegerField()
    created = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = u'bazzer_histories'

class BazzerItemBinds(models.Model):
    id = models.IntegerField(primary_key=True)
    item_id = models.IntegerField()
    class Meta:
        db_table = u'bazzer_item_binds'

class BazzerItems(models.Model):
    id = models.IntegerField(primary_key=True)
    seller_no = models.IntegerField(null=True, blank=True)
    have_no = models.IntegerField()
    price = models.IntegerField()
    it_id = models.IntegerField(null=True, blank=True)
    it_created = models.IntegerField(null=True, blank=True)
    item_id = models.IntegerField()
    set_count = models.IntegerField()
    sell_comp = models.IntegerField(null=True, blank=True)
    created = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = u'bazzer_items'

class ContinueBuyBazzers(models.Model):
    id = models.IntegerField(primary_key=True)
    entry_no = models.IntegerField()
    bazzer_item_id = models.IntegerField(null=True, blank=True)
    seller_no = models.IntegerField(null=True, blank=True)
    have_no = models.IntegerField(null=True, blank=True)
    it_id = models.IntegerField(null=True, blank=True)
    it_created = models.IntegerField(null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    set_count = models.IntegerField(null=True, blank=True)
    created = models.DateTimeField(null=True, blank=True)
    ip_address = models.CharField(max_length=765, blank=True)
    host_address = models.CharField(max_length=765, blank=True)
    agent = models.CharField(max_length=765, blank=True)
    class Meta:
        db_table = u'continue_buy_bazzers'

