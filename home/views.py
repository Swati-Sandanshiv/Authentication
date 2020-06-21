from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login

# passward for test user is Swati$$$***000
# Create your views here.
def index(request):
    # if any 'anonymous' user ie.(the user who is not logged in) tries to open 'index.html',
    # then user will get redircted to 'login.html'.
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request, 'index.html')

def loginUser(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # if the method is "POST" check if user has entered correct credentials & Authenticating username and password of user.
        user = authenticate(username=username, password=password)
        
        if user is not None:
            # A backend authenticated the credentials ie. if username and password of user is correct,
            # user will redirect to home page ie 'index.html' else will remain on 'login.html'.
            login(request, user)
            return redirect("/") 
        
        else:
            # No backend authenticated the credentials
            return render(request, 'login.html')
    
    return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect("/login")