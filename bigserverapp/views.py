from django.shortcuts import render, HttpResponse,redirect
from .models import User

def index(request):
    print(User.objects.all())
    context = {
        "allUsers": User.objects.all()
    }
    return render(request,"index.html", context)


def createUser(request):
    
    print(request.POST)
    
    newUser = User.objects.create(first_name=request.POST ['fname'],last_name=request.POST['lname'],email_address= request.POST['email'],age= request.POST['ageFromForm'])
    
    return redirect("/")