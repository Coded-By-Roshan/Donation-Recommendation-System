
from django.db import models


class EmailVerifications(models.Model):
    email = models.CharField(max_length=255)
    otp = models.IntegerField()
    created_at = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'email_verifications'


class Likes(models.Model):
    likes = models.IntegerField()
    postid = models.IntegerField()
    uid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'likes'


class Payments(models.Model):
    uid = models.IntegerField()
    postid = models.IntegerField()
    amount = models.CharField(max_length=255)
    paidtime = models.DateTimeField(blank=True, null=True)
    transictionid = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payments'


class Posts(models.Model):
    description = models.TextField(blank=True, null=True)
    relation = models.CharField(max_length=255)
    approvedstatus = models.IntegerField()
    pnumber = models.CharField(max_length=255)
    targetamount = models.IntegerField()
    targateddate = models.DateTimeField()
    catagory = models.CharField(max_length=255)
    collectedamount = models.IntegerField()
    uid = models.IntegerField()
    citizenship = models.TextField()
    fname = models.CharField(max_length=255)
    mname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    photos = models.TextField(blank=True, null=True)
    officialdocs = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'posts'


class Users(models.Model):
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    email_verified_at = models.DateTimeField()
    is_verified = models.IntegerField()
    password = models.CharField(max_length=255)
    role = models.IntegerField()
    pnumber = models.BigIntegerField(blank=True, null=True)
    mname = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'
