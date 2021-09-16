from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username = request.POST['username'], password = request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'account/login.html', {'error': 'Username or password is incorrect'})   
    else:
        return render(request, 'account/login.html')    

def register(request):
    if request.method == 'POST':
        if request.POST['password'] == request.POST['confirm']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'account/register.html', {'error': 'This username is already taken'})
            except User.DoesNotExist:
                user = User.objects.create_user(username = request.POST['username'], password = request.POST['password'])
                auth.login(request, user)
                return redirect('home')
        
        else:
            return render(request, 'account/register.html', {'error': 'Passwords must match'})


    else:
        return render(request, 'account/register.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
    
    