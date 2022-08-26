from django.shortcuts import render, redirect
from django.contrib import messages
from jokesApp.models import *
import bcrypt

def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'GET':
        return redirect('/')
    errors = User.objects.validate(request.POST)
    if errors:
        for err in errors.values():
            messages.error(request, err)
        return redirect('/')
    hashedPw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
    newUser = User.objects.create(
        firstName = request.POST['firstName'],
        lastName = request.POST['lastName'],
        email = request.POST['email'],
        password = hashedPw
    )
    request.session['user_id'] = newUser.id
    return redirect('/dashboard/')

def login(request):
    emailUser = User.objects.filter(email = request.POST['email'])
    if emailUser:
        userLogin = emailUser[0]
        if bcrypt.checkpw(request.POST['password'].encode(), userLogin.password.encode()):
            request.session['user_id'] = userLogin.id
            return redirect('/dashboard/')
        messages.error(request, 'Invalid Credentials')
        return redirect('/')
    messages.error(request, 'That Username or Email is not in our system, please register for an account')
    return redirect('/')

def logout(request):
    request.session.clear()
    messages.error(request, 'You have been logged out')
    return redirect('/')

def dashboard(request):
    if 'user_id' not in request.session:
        return redirect('/')
    user = User.objects.get(id=request.session['user_id'])
    jokes = Joke.objects.all().values()
    context = {
        'user': user,
        'jokes': jokes
    }
    return render(request, 'dashboard.html', context)