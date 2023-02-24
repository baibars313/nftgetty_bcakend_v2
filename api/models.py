from django.db import models
from ckeditor.fields import RichTextField


class Items(models.Model):
    uri=models.CharField(null=False, max_length=255)
    price=models.CharField(null=False,max_length=255)
    sold=models.BooleanField(default=False)
    itemId=models.IntegerField(default=0)
    category=models.CharField(null=False,max_length=255)
    chain=models.IntegerField(null=False, default=1)
    tokenId=models.IntegerField(null=False, default=1)
    owner=models.CharField(null=False,max_length=255,default="0x000000000000000000000000000000")
    auction=models.BooleanField(default=False)
    license=models.BooleanField(default=False)
    contract_address=models.CharField(null=False,max_length=255,default="0x000000000000000000000000000000")
    def __str__(self):
        return self.uri

class Userr(models.Model):
    name=models.CharField(null=False,max_length=255)
    address=models.CharField(null=False,max_length=255,default="0x000000000000000000000000000000", unique=True)
    email=models.CharField(null=False,max_length=255,default="examp@ex.com")
    date_joind=models.DateField(auto_now_add=True)
    usename=models.CharField(null=False,max_length=255)
    facebook=models.CharField(null=False,max_length=255,default="facebook.com")
    twiter=models.CharField(null=False,max_length=255,default="twitter.com")
    instagram=models.CharField(null=False,max_length=255,default="instagram.com")
    profile=models.CharField(null=False,max_length=255,default="https://i.imgur.com/KykRUCV.jpeg")
    cover=models.CharField(null=False,max_length=255,default="https://i.imgur.com/jxyuizJ.jpeg")
    def __str__(self):
        return self.name

class Bids(models.Model):
    name=models.CharField(null=False,max_length=255)
    address=models.CharField(null=False,max_length=255,default="0x000000000000000000000000000000")
    itemId=models.IntegerField(null=False, default=0)
    chainId=models.IntegerField(null=False, default=0)
    amount=models.CharField(null=False,max_length=255,default="examp@ex.com")
    date_joind=models.DateField(auto_now_add=True)
    def __str__(self):
        return self.name


class collection(models.Model):
    name=models.CharField(null=False,max_length=255)
    owner=models.CharField(null=False,max_length=255,default="0x000000000000000000000000000000")
    contract=models.CharField(null=False,max_length=255,default="0x000000000000000000000000000000")
    description=models.CharField(null=False,max_length=255,default="description")
    chainId=models.IntegerField(null=False, default=0)
    cover=models.CharField(null=False,max_length=255,default="not")
    avatr=models.CharField(null=False,max_length=255,default="not")
    date_joind=models.DateField(auto_now_add=True)
    def __str__(self):
        return self.name

class Question(models.Model):
    question=models.CharField(null=False,max_length=255)
    answere=RichTextField()



