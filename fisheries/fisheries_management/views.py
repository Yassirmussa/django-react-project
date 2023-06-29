from urllib import response
from django.shortcuts import render
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import VehicleSerializer, MarinaSerializer, FishermenSerialzer, WorksheetSerializer
from django.http import JsonResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
import json 
from .models import Marina, Vehicle,Fishermen, Worksheet

# Create your views here for marina
@api_view(['POST'])
def insertMarina(request):
    serializer = MarinaSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['GET'])
def getMarina(request):
    marina = Marina.objects.all()
    serializer = VehicleSerializer(marina, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getMarina_byId(request,Mid):
    marina = Vehicle.objects.get(Mid=Mid)
    serializer = VehicleSerializer(marina)
    return Response(serializer.data)

@api_view(['PUT'])
def updateMarina(request, Mid):
    marina = Marina.objects.get(Mid=Mid)
    serializer = VehicleSerializer(marina, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

    
@api_view(['DELETE'])
def deleteMarina(request, Mid):
    vehicle = Vehicle.objects.get(VId=VId)
    vehicle.delete()
    return Response(status=204)

# views for vehicle
@api_view(['POST'])
def insertVehicle(request):
    serializer = VehicleSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)
     
#normal get
@api_view(['GET'])
def getVehicle(request):
    vehicle = Vehicle.objects.all()
    serializer = VehicleSerializer(vehicle, many=True)
    return Response(serializer.data)

#get by id
@api_view(['GET'])
def getVehicle_byId(request,VId):
    vehicle = Vehicle.objects.get(VId=VId)
    serializer = VehicleSerializer(vehicle)
    return Response(serializer.data)

@api_view(['PUT'])
def updateVehicle(request, VId):
    vehicle = Vehicle.objects.get(VId=VId)
    serializer = VehicleSerializer(vehicle, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)


@api_view(['DELETE'])
def deleteVehicle(request, VId):
    vehicle = Vehicle.objects.get(VId=VId)
    vehicle.delete()
    return Response(status=204)
# @csrf_exempt
# def deleteVehicle(request, VId):
#     if request.method == 'DELETE':
#         vehicle = Vehicle.objects.get(VId = VId)
#         vehicle.delete()
#         return JsonResponse({'data':'deleted succesifully'})
    
@api_view(['POST'])
def insertFishermen(request):
    serializer = FishermenSerialzer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['GET'])
def getFishermen(request):
    fishermen = Fishermen.objects.all()
    serializer = FishermenSerialzer(fishermen, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getFishermen_byId(request,FId):
    fishermen = Fishermen.objects.get(FId=FId)
    serializer = FishermenSerialzer(fishermen)
    return Response(serializer.data)

@api_view(['PUT'])
def updateFishermen(request, FId):
    fishermen = Fishermen.objects.get(FId=FId)
    serializer = FishermenSerialzer(fishermen, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['DELETE'])
def deleteFishermen(request, FId):
    fishermen = Fishermen.objects.get(FId=FId)
    fishermen.delete()
    return Response(status=204)

@api_view(['POST'])
def insertWork(request):
    serializer = WorksheetSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['GET'])
def getWorksheet(request):
    worksheet = Worksheet.objects.all()
    serializer = WorksheetSerializer(worksheet, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getWorksheet_byId(request,WId):
    worksheet = Worksheet.objects.get(WId=WId)
    serializer = WorksheetSerializer(worksheet)
    return Response(serializer.data)

@api_view(['PUT'])
def updateWorksheet(request, WId):
    worksheet = Worksheet.objects.get(WId=WId)
    serializer = WorksheetSerializer(worksheet, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['DELETE'])
def deleteWorkshhet(request, WId):
    worksheet = Worksheet.objects.get(WId=WId)
    worksheet.delete()
    return Response(status=204)