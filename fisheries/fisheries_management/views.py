from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json 
from .models import Marina, Vehicle

# Create your views here for marina
@csrf_exempt
def insertMarina(request):
    if request.method =='POST':
        data = json.loads(request.body)
        Mid = data.get('Mid')
        Mname = data.get('Mname')
        location = data.get('location')
        
        marina = Marina(Mid=Mid,Mname=Mname,location=location)
        marina.save()
        origin = request.META.get('HTTP_ORIGIN')
        return JsonResponse({'Mid':marina.Mid,'Mname':marina.Mname,'messsage':'data inserted succesiful '})

@csrf_exempt
def getMarina(request):
    if request.method=='GET':
        marina = Marina.objects.all()
        origin = request.META.get('HTTP_ORIGIN')
        data = []
        for marina in marina:
            data.append({
                'Mid': marina.Mid,
                'Mname':marina.Mname,
                'Location': marina.location
            })
        return JsonResponse(data, safe=False)

@csrf_exempt
def updateMarina(request, Mid):
    if request.method =='PUT':
        marina = Marina.objects.get(Mid=Mid)
        data = json.loads(request.body)
        Mname = data.get('Mname')
        location = data.get('location')
        # Update the instance fields
        # marina.Mname = request.POST.get('Mname', marina.Mname)
        # marina.location = request.POST.get('location', marina.location)
        
        marina.Mname = Mname
        marina.location = location
        marina.save()

        return JsonResponse({'Mid':marina.Mid,'Mname':marina.Mname,'location':marina.location,'message':'data updated successiful'})
    
@csrf_exempt
def deleteMarina(request, Mid):
    if request.method == 'DELETE':
        marina = Marina.objects.get(Mid=Mid)
        marina.delete()

        return JsonResponse({'data':'deleted successifully'})

# views for vehicle
@csrf_exempt
def insertVehicle(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            VId = data.get('VId')
            VName = data.get('VName')
            VOwner = data.get('VOwner')
            Ownerphone = data.get('Ownerphone')
            MId = data.get('MId')
            Password = data.get('Password')
            C_password = data.get('C_password')
            # to retrieve id direct 
            marin = Marina.objects.get(Mid=MId)


            vehicle = Vehicle(VId=VId, 
                              VName=VName, 
                              VOwner=VOwner, 
                              Ownerphone=Ownerphone,
                              MId=marin,
                              Password=Password,
                              C_password=C_password)
            vehicle.save()
            return JsonResponse({vehicle.VId:'inserted'})
        
        except json.JSONDecodeError:
            response = {'error':'Invalid json data'}
            return JsonResponse(response, status=400)

# @csrf_exempt
# def getVehicle (request, VId):
#     try:
#         vehicle = Vehicle.objects.get(VId=VId)
            
#         if request.method =='GET':
#             getvehicle = {
#                 'VId':vehicle.VId,
#                 'VName':vehicle.VName,
#                 'VOwner':vehicle.VOwner,
#                 'Ownerphone':vehicle.Ownerphone,
#                 'Password':vehicle.Password,
#                 'C_password':vehicle.C_password,
#                 'MId':vehicle.MId
#             }
#             return JsonResponse(getvehicle)
#     except Vehicle.DoesNotExist:
#         reponse = {'error':'vehicle not found'}
#         return JsonResponse(reponse, status=404)    

@csrf_exempt
def getVehicle(request):
    if request.method=='GET':
        vehicle = Vehicle.objects.all()
        origin = request.META.get('HTTP_ORIGIN')
        data = []
        for vehicle in vehicle:
            data.append({
                'VId':vehicle.VId,
                'VName':vehicle.VName,
                'VOwner':vehicle.VOwner,
                'Ownerphone':vehicle.Ownerphone,
                'Password':vehicle.Password,
                'C_password':vehicle.C_password,
                'MId':vehicle.MId
                })
            return JsonResponse(data, safe=False)