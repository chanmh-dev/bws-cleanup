from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    path('api/', views.view_api, name='view_api'),
    path('plastic-counters/', views.view_plastic_counters,
         name='view_plastic_counters'),
]
