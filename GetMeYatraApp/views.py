from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required 
from .models import Book, TripBooking
from datetime import datetime

# Create your views here.

def home(request):
    return render(request, 'homepage.html')


# def homePage(request):
#     return render(request, 'homepage.html')

def bookdetails(request):
    return render(request, 'bookingdetails.html')

def khatushyam(request):
    return render(request, 'khatushyamdetail.html')

def dodham(request):
    return render(request, 'dodhamdetail.html')

def ekdham(request):
    return render(request, 'ekdhamdetail.html')

def chardham(request):
    return render(request, 'chardhamdetail.html')

def vrindavan(request):
    return render(request, 'vrindavandetail.html')

def ujjain(request):
    return render(request, 'ujjaindetail.html')






def book_trip(request):
    if request.method == 'POST':
        from_location = request.POST.get('from')
        to_location = request.POST.get('to')
        date_str = request.POST.get('date')  
        pickup_point = request.POST.get('pickup')
        full_name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        alt_phone = request.POST.get('altPhone')
        persons = int(request.POST.get('persons'))
        price_per_person = float(request.POST.get('price'))
        total_price = persons * price_per_person

        # Convert date from DD-MM-YYYY to a Python date object
        if date_str:
            try:
                date = datetime.strptime(date_str, "%d-%m-%Y").date()
            except ValueError:
                # Handle invalid date format
                return render(request, 'book_trip.html', {
                    'error': 'Invalid date format. Please select a valid date.'
                })
        else:
            # No date selected
            return render(request, 'book_trip.html', {
                'error': 'Please select a date.'
            })

       
        TripBooking.objects.create(
            from_location=from_location,
            to_location=to_location,
            date=date,
            pickup_point=pickup_point,
            full_name=full_name,
            email=email,
            phone=phone,
            alt_phone=alt_phone,
            persons=persons,
            price_per_person=price_per_person,
            total_price=total_price
        )

        return redirect('booking_success')

    return render(request, 'bookingdetials.html')


def booking_success(request):
    return render(request, 'booking_success.html')


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
            return redirect('home')
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