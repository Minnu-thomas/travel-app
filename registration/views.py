from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login_fn(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid credentials")
            return redirect('login_fn')
    return render(request,"login.html")


def register_fn(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        password_conf = request.POST['password_conf']
        if password == password_conf:
            if User.objects.filter(username=username).exists():
                messages.info(request,"USERNAME ALREADY EXISTS!")
                return redirect('register_fn')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "EMAIL ALREADY EXISTS!")
                return redirect('register_fn')
            else:
                user = User.objects.create_user(username=username, password=password, first_name=first_name,
                                        last_name=last_name, email=email)
                user.save();
                return redirect('login_fn')
        else:
            print("Password mismatch!!")
            return redirect('register_fn')
        return redirect('/')

    return render(request, "register.html")

def logout_fn(request):
    auth.logout(request)
    return redirect('/')