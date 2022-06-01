from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.views import View
from django.contrib import messages
from django.views.generic import CreateView
from django.urls import reverse_lazy

from .forms import SignUpForm
from .models import CustomUser


class Login(View):
    def get(self, request):
        return render(request, 'accounts/login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, "username or password error")
            return redirect('login')

class SignUpView(CreateView):
    model = CustomUser
    form_class = SignUpForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('login')

def logout_page(request):
    logout(request)
    return redirect('login')