from django.shortcuts import redirect, render, HttpResponse
import requests
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User, AnonymousUser
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, "website/index.html")

def domain_search(request):

    if request.user.is_anonymous:
        return redirect("/")

    context = {}
    if request.method=="POST":
        try:
            domain=request.POST['domain']
            r=requests.get(f"http://localhost:8000/email/{domain}")
            data=r.json()[f"{domain}"]
            context = {
                'email': data
            }
        except Exception as e:

            context = {
                'email': "Not found"
            }

    return render(request, "website/domain_search.html", context)

def email_finder(request):

    if request.user.is_anonymous:
        return redirect("/")    

    return render(request, "website/email_finder.html")


def email_verifier(request):

    if request.user.is_anonymous:
        return redirect("/")

    return render(request, "website/email_verifier.html")

def resources(request):

    if request.user.is_anonymous:
        return redirect("/")
        
    return render(request, "website/resources.html")

def about_us(request):

    if request.user.is_anonymous:
        return redirect("/")

    return render(request, "website/about_us.html")

def our_data(request):

    if request.user.is_anonymous:
        return redirect("/")

    return render(request, "website/our_data.html")


def loginuser(request):

    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "successfully logged in")
            return redirect("/")
        else:
            messages.warning(request, "Invalide username or password")
            return redirect("/loginuser") 
        
    return redirect("/")


def signupuser(request):

    if request.method=="POST":
        username=request.POST['username']
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        myuser=User.objects.create_user(username, email, password1)
        myuser.fname=firstname
        myuser.lname=lastname
        myuser.save()
        messages.success(request, f"Successfully created username : {username} ")
        return redirect("/")

    return redirect("/")

def logoutuser(request):
    logout(request)
    messages.success(request, "successfully logged out")
    return redirect("/")



