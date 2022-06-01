from django.urls import path
from .views import *

urlpatterns = [
    path('login', Login.as_view(), name = 'login'),
    path('signup', SignUpView.as_view(), name = 'signup'),
    path('logout', logout_page, name = 'logout')
]