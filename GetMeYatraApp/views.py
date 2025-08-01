from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required 
from .models import Book

# Create your views here.

def home(request):
    return render(request, 'home.html')


def homePage(request):
    return render(request, 'homepage.html')


def book(request):
    if request.method=='POST':
        place = request.POST.get('place')
        total_person = request.POST.get('person')
        adate = request.POST.get('Adate')
        ldate = request.POST.get('Ldate')
        personaldata = request.POST.get('text')

        if place != '' and len(total_person) != 0 and adate != '' and ldate != 0 and personaldata != '':
            data = Book(Place=place, Total_person=total_person,
                             Adate=adate,Ldate=ldate,
                             Personaldata =personaldata)
            
            data.save()
    return render(request, 'book.html')


def package(request):
    return render(request, 'package.html')


def service(request):
    return render(request, 'service.html')


def gallery(request):
    return render(request, 'gallery.html')


def aboutUs(request):
    return render(request, 'about.html')


def loginpage(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request, username=username, password=pass1)
        if user is not None:
            login(request,user)
            return redirect('homePage')
        else:
            return HttpResponse("Username or Password in incorrect!!")
    return render(request, 'login.html')
 
def SignUp(request):
    if request.method == 'POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your password and confirm are not same!! ")
        
        else:
            my_user=User.objects.create_user(uname, email, pass1)
            my_user.save()
            return redirect('login')
    return render(request, 'signup.html')