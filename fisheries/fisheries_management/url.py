from django.urls import path, include
from . import views

urlpatterns = [
    #marina
    path('api/v1/marina', views.insertMarina),
    path('api/v1/getmarina', views.getMarina),
    path('api/v1/marina2/<Mid>/', views.updateMarina),
    path('api/v1/deleteMarina/<Mid>/', views.deleteMarina),

    #vehicle
    path('api/v1/vehicle', views.insertVehicle),
    path('api/v1/getvehicle', views.getVehicle)
]