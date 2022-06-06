from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name = 'home'),
    path('questions/<int:pk>', quiz_test, name = 'quiz_test'),
]