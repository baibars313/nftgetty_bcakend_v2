from django.urls import path
from .views import *
urlpatterns = [
 path('sales/',Sales,name="sales")
]