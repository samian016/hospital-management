from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import auth,User
# Create your views here.


def signup(request):
    if request.method == 'GET':
        return render(request, 'login/signup.html')
    elif request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username already taken...")
                return redirect('/signup')

            elif User.objects.filter(email=email):
                messages.info(request, "Already exist...")
                return redirect('/signup')

            else:
                user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password1)

                messages.info(request, "User Created...")
                return redirect('/login')


        else:
            messages.info(request, "Password not matching...")
            return redirect('/signup')

        #return redirect('/')


def home(request):
    return render(request, 'login/home.html')


def login(request):

    if request.method == 'POST':
        username = request.POST['Username']
        password = request.POST['Password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/medical/m')
        else:
            messages.info(request, "Invalid credentials")
            return redirect('/login')
    else:
        return render(request, 'login/login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


