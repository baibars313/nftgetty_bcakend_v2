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



