from django.urls import path, include
from . import views

urlpatterns = [
    #marina
    path('api/v1/marina', views.insertMarina),
    path('api/v1/getmarina', views.getMarina),
    path('api/v1/getMarina/<Mid>/', views.getMarina_byId),
    path('api/v1/marina2/<Mid>/', views.updateMarina),
    path('api/v1/deleteMarina/<Mid>/', views.deleteMarina),

    #vehicle
    path('api/v1/vehicle', views.insertVehicle),
    path('api/v1/getvehicle', views.getVehicle),
    path('api/v1/getvehicle/<VId>/', views.getVehicle_byId),
    path('api/v1/updateVehicle/<VId>/', views.updateVehicle),
    path('api/v1/deleteVehicle/<VId>/', views.deleteVehicle),

    #fishermen
    path('api/v1/insertFishermen', views.insertFishermen),
    path('api/v1/getFishermen', views.getFishermen),
    path('api/v1/getFishermen/<FId>/', views.getFishermen_byId),
    path('api/v1/updateFishermen/<FId>/', views.updateFishermen),
    path('api/v1/deleteFishermen/<FId>/', views.deleteFishermen),

    #Worksheet
    path('api/v1/insertWorksheet', views.insertWork),
    path('api/v1/getWorksheet', views.getWorksheet),
    path('api/v1/getWorksheet/<WId>/', views.getWorksheet_byId),
    path('api/v1/updateWorksheet/<WId>/', views.updateWorksheet),
    path('api/v1/deleteWorksheet/<WId>/', views.deleteWorkshhet),
    
]