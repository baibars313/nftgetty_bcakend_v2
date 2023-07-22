from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Netuser(models.Model):
    user_id=models.CharField(max_length=255,unique=True,primary_key=True)
    level_1=models.CharField(max_length=255)
    level_2=models.CharField(max_length=255)
    level_3=models.CharField(max_length=255)
    level_4=models.CharField(max_length=255)
    my_refral=models.CharField(max_length=255)
    wallet=models.CharField(max_length=255,default='0x0000')



class Deposit(models.Model):
    user_id=models.ForeignKey(Netuser,on_delete=models.CASCADE)
    amount=models.FloatField()
    screen_shot=models.CharField(max_length=255,default="no ss")
    confirmed=models.BooleanField(default=False)
    creation_date=models.DateTimeField(auto_now_add=True)
    currency=models.CharField(max_length=100)
    tx_hash=models.CharField(max_length=255)


class Trade(models.Model):
    titel=models.CharField(max_length=255)
    max_amount=models.FloatField()
    min_amount=models.FloatField()
    time_span=models.FloatField(default=6)
    descrption=models.CharField(max_length=255)
    percentage=models.FloatField()
    disable=models.BooleanField(default=False)

class Link(models.Model):
    telegram=models.CharField(max_length=255)
    facebook=models.CharField(max_length=255)
    insta=models.CharField(max_length=255)
    twitter=models.CharField(max_length=255)
    youtube=models.CharField(max_length=255)



class Order(models.Model):
    user_id = models.ForeignKey(Netuser, on_delete=models.CASCADE)
    trade = models.ForeignKey(Trade, on_delete=models.CASCADE)
    amount = models.FloatField()
    commission = models.FloatField()
    starting_time = models.FloatField()
    ending_time = models.FloatField()
    personal_commision=models.FloatField(default=0)
    market_comission=models.FloatField(default=0)
    level_1=models.FloatField(default=0)
    level_2=models.FloatField(default=0)
    level_3=models.FloatField(default=0)
    level_4=models.FloatField(default=0)



class Withdrawl(models.Model):
    user_id=models.ForeignKey(Netuser,on_delete=models.CASCADE)
    amount=models.FloatField()
    confirmed=models.BooleanField(default=False)
    creation_date=models.DateTimeField(auto_now_add=True)






