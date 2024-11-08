from django.urls import path
from . import views

urlpatterns = [
    path('', views.mainproject, name='mainproject'),
    path('<int:rohan_id>/',views.nextproject, name='nextproject'),
]
