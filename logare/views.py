from django.shortcuts import render, redirect
from django.contrib import messages 
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User 

# Create your views here.
def paginaLogare(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Utilizatorul nu exista!')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Utilizatorul SAU parola nu exista!')

    return render(request, 'logare/logare_inregistrare.html')



def delogareUtilizator(request):
    logout(request)
    return redirect('home')
