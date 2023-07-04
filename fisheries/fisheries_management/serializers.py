from rest_framework import serializers
from .models import Vehicle, Marina, Fishermen, Worksheet

class MarinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marina
        fields = ['Mid','Mname','location']

class VehicleSerializer(serializers.ModelSerializer):
    marina = MarinaSerializer(source='MId', read_only=True)
    class Meta:
        model = Vehicle
        fields = ['VId','VName','VOwner','Ownerphone','MId','Password','C_password','marina']

class FishermenSerialzer(serializers.ModelSerializer):
    vehicle = VehicleSerializer(source ='VId', read_only=True)
    class Meta:
        model = Fishermen
        fields = ['FId','FName','Address','Phonenumber','VId','vehicle']

class WorksheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worksheet
        fields = ['WId','VId','Fishspecie','quantity','Date','price']