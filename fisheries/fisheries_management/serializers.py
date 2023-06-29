from rest_framework import serializers
from .models import Vehicle, Marina, Fishermen, Worksheet

class MarinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marina
        fields = ['MId','MName','location']

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ['VId','VName','VOwner','Ownerphone','MId','Password','C_password']

class FishermenSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Fishermen
        fields = ['FId','FName','Address','Phonenumber','VId']

class WorksheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worksheet
        fields = ['WId','VId','Fishspecie','quantity','Date','price']