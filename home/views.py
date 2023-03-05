from django.shortcuts import render, HttpResponse, redirect

from django.contrib.auth.models import User
from django.contrib.auth import authenticate ,login
from django.contrib.auth import logout
from django.contrib import messages
from django.db import IntegrityError
import random
import string


# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request,'index.html')

def test(request):
    return render(request,'test.html')

def aptitude(request):
    return render(request,'aptitude.html')

def interview(request):
    return render(request,'interview.html')

def hrinter1(request):
    return render(request,'hrinter1.html')

def hrinter2(request):
    return render(request,'hrinter2.html')   

def placement1(request):
    return render(request,'placement1.html') 

def placement2(request):
    return render(request,'placement2.html') 

def geneknow(request):
    return render(request,'geneknow.html')

def courses(request):
    return render(request,'courses.html')

def course1(request):
    return render(request,'course1.html')

def coursematerial(request):
    return render(request,'coursematerial.html')

def about(request):
    return render(request,'about.html')

def logoutUser(request):
    logout(request)
    return redirect('login')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
    return render(request, 'login.html')



def register(request):
    
    if request.method=='POST':
        #get the post parameters
        username=request.POST['username']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        password=request.POST['password']
        confirmpassword=request.POST['confirmpassword']


        #create the user
        try:
            myuser = User.objects.create_user(username, email, password)
            myuser.first_name = fname
            myuser.last_name = lname
            myuser.save()
            return redirect('login')
        except IntegrityError:
            # If the username already exists, display an error message
            error_msg = "The username already exists. Please choose a different username."
            return render(request, 'register.html', {'error_msg': error_msg})
    if request.method=='GET':
        return render(request,'register.html')
    
        

def forget(request):
    return render(request,'forget.html')




# def register(request):
#     if request.method == "POST":
#             name = request.POST.get('name')
#             email = request.POST.get('email')
#             password = request.POST.get('password')
#             confirmpassword = request.POST.get('confirmpassword')

#             contact = Registerinfo(name = name, email = email, password = password, confirmpassword=confirmpassword,date = datetime.today())
#             contact.save()
#             messages.success(request, 'User Register Successfully!.')
#     return render(request,'register.html') 