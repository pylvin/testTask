from django.contrib import admin
from django.urls import path

from app.views import index, status, update, active

urlpatterns = [
    path('', index,name="index"),
    path('status/<int:id>/', status,name="status"),
    path('update/<int:id>/<int:interval>/', update,name="update"),
    path('active/<int:id>/', active,name="active")
]