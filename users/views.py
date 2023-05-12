from django.shortcuts import render

from .models import User
from .forms import UserLoginForm

# Create your views here.
def login(request):
    context = {'form': UserLoginForm}
    return render(request, 'users/login.html', context)

def registration(request):
    return render(request, 'users/register.html')