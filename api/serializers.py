from rest_framework import serializers
from .models import *


class Itemserializer(serializers.ModelSerializer):
    class Meta:
        model = Items
        fields = '__all__'



class Useserilizer(serializers.ModelSerializer):
    class Meta:
        model=Userr
        fields='__all__'

class Bidserializer(serializers.ModelSerializer):
    class Meta:
        model=Bids
        fields='__all__'

class collectionserializer(serializers.ModelSerializer):
    class Meta:
        model=collection
        fields='__all__'

class Questionserializer(serializers.ModelSerializer):
    class Meta:
        model=Question
        fields='__all__'



class Rewardserializer(serializers.ModelSerializer):
    class Meta:
        model=Reward
        fields='__all__'

class Locationserializer(serializers.ModelSerializer):
    class Meta:
        model=Location
        fields='__all__'

class Feeserializer(serializers.ModelSerializer):
    class Meta:
        model=Fee
        fields='__all__'

class BaseFeeserializer(serializers.ModelSerializer):
    class Meta:
        model=BaseFee
        fields='__all__'
# BidUnlist

class BidUnlistserializer(serializers.ModelSerializer):
    class Meta:
        model= BidUnlist
        fields='__all__'

class FeaturedCollectionserializer(serializers.ModelSerializer):
    class Meta:
        model= FeaturedCollection
        fields='__all__'

class Notificationserializer(serializers.ModelSerializer):
    class Meta:
        model= Notifications
        fields='__all__'




