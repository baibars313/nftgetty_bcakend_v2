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
    minting=models.IntegerField(null=False, default=1)
    expiring=models.IntegerField(null=False, default=0)
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
    banned=models.BooleanField(default=False)
    fee_discount=models.BooleanField(default=False)
    def __str__(self):
        return self.name

class Bids(models.Model):
    name=models.CharField(null=False,max_length=255)
    address=models.CharField(null=False,max_length=255,default="0x000000000000000000000000000000")
    itemId=models.IntegerField(null=False, default=0)
    chainId=models.IntegerField(null=False, default=0)
    amount=models.CharField(null=False,max_length=255,default="examp@ex.com")
    date_joind=models.DateField(auto_now_add=True)
    userAddress=models.CharField(null=False,max_length=255,default="0x000000000000000000000000000000")
    image=models.CharField(null=False,max_length=255,default="")
    link=models.CharField(null=False,max_length=255,default="")
    viewed=models.BooleanField(default=False)
    def __str__(self):
        return self.name


class Notifications(models.Model):
    name=models.CharField(null=False,max_length=255)
    description=models.CharField(null=False,max_length=255)
    viewed=models.BooleanField(default=False)
    image=models.CharField(max_length=255, default="https://cdn.pixabay.com/photo/2013/07/12/14/32/bell-148428_1280.png")
    userAddress=models.CharField(null=False,max_length=255,default="0x000000000000000000000000000000")
    amount=models.FloatField(default=0)
    link=models.CharField(null=False,max_length=255)

    def __str__(self):
        return self.name


class Fee(models.Model):
    address=models.CharField(null=False,max_length=255, unique=True)
    paid=models.BooleanField(default=False)
    amount=models.IntegerField(null=False, default=0)
    def __str__(self):
        return self.address

class BidUnlist(models.Model):
    address=models.CharField(null=False,max_length=255)
    closed=models.BooleanField(default=False)
    amount=models.FloatField(null=False, default=0)
    bidId=models.IntegerField(null=False, default=0,unique=True)
    tokenId=models.IntegerField(null=False, default=0)
    contract=models.CharField(null=False,max_length=255)
    userAddress=models.CharField(null=False,max_length=255,default="0x000000000000000000000000000000")
    image=models.CharField(null=False,max_length=255,default="")
    link=models.CharField(null=False,max_length=255,default="")
    viewed=models.BooleanField(default=False)
    def __str__(self):
        return self.address

class BaseFee(models.Model):
    apply=models.BooleanField(default=False)
    amount=models.IntegerField(null=False, default=0)
    def __str__(self):
        return str(self.amount)

class collection(models.Model):
    name=models.CharField(null=False,max_length=255)
    owner=models.CharField(null=False,max_length=255,default="0x000000000000000000000000000000")
    contract=models.CharField(null=False,max_length=255,default="0x000000000000000000000000000000")
    description=models.TextField(null=False,default="description")
    chainId=models.IntegerField(null=False, default=0)
    cover=models.CharField(null=False,max_length=255,default="not")
    avatr=models.CharField(null=False,max_length=255,default="not")
    date_joind=models.DateField(auto_now_add=True)
    banned=models.BooleanField(default=False)
    onsale=models.BooleanField(default=False)
    collectionId=models.IntegerField(null=False, default=0)
    price=models.IntegerField(null=False, default=1)
    def __str__(self):
        return self.name

class Reward(models.Model):
    name=models.CharField(null=False,max_length=255)
    owner=models.CharField(null=False,max_length=255,default="0x000000000000000000000000000000")
    contract=models.CharField(null=False,max_length=255,default="0x000000000000000000000000000000")
    description=models.CharField(null=False,max_length=255,default="description")
    chainId=models.IntegerField(null=False, default=0)
    claimed=models.BooleanField(default=False)
    rewardId=models.CharField(max_length=255,default=0)
    avatr=models.CharField(null=False,max_length=255,default="not")
    date_joind=models.DateField(auto_now_add=True)
    def __str__(self):
        return self.name


class Question(models.Model):
    question=models.CharField(null=False,max_length=255)
    imageLink=models.CharField(null=False,max_length=255)
    answere=RichTextField()

class Location(models.Model):
    lat=models.CharField(null=False,max_length=255)
    long=models.CharField(null=False,max_length=255)

class FeaturedCollection(models.Model):
    banner=models.CharField(null=False,max_length=255)
    link=models.CharField(null=False,max_length=255)



