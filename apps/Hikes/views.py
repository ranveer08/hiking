
from django.http import JsonResponse
from django.shortcuts import render, HttpResponse, redirect, HttpResponse
from django.contrib import messages
from .models import *
import bcrypt
import json


def index(request):
    if 'user_id' not in request.session:
        # messages.error(request,'You must be logged in')
        return render(request, "Hikes/index.html")
        
    user_id = request.session['user_id']
    current_user = User.objects.get(id=user_id)
    context = {
        'user': current_user
    }
    return render(request, "Hikes/index.html", context)

def weather(request):

    return render(request, "Hikes/weather.html" )

def gallery(request):
    if 'user_id' not in request.session:
        # messages.error(request,'You must be logged in')
        return render(request, "Hikes/gallery.html")
        
    user_id = request.session['user_id']
    current_user = User.objects.get(id=user_id)
    context = {
        'user': current_user
    }
    return render(request, "Hikes/gallery.html", context)

def video(request):
    if 'user_id' not in request.session:
        # messages.error(request,'You must be logged in')
        return render(request, "Hikes/video.html")
        
    user_id = request.session['user_id']
    current_user = User.objects.get(id=user_id)
    context = {
        'user': current_user
    }
    return render(request, "Hikes/video.html", context)

def _map(request):
    mapKey = "KEY"
    return render(request, "Hikes/map.html", {'mapKey': mapKey})

def get_data(request):
    user_id = request.session['user_id']
    current_user = User.objects.get(id=user_id)
    print(current_user.name)
    
    data = {
  "cols": [
        {"id":"","label":"Topping","pattern":"","type":"string"},
        {"id":"","label":"Slices","pattern":"","type":"number"}
      ],
  "rows": [
        {"c":[{"v":"Mushrooms","f":'Mushrooms'},{"v":3,"f":3}]},
        {"c":[{"v":"Onions","f":'null'},{"v":1,"f":'null'}]},
        {"c":[{"v":"Olives","f":'null'},{"v":1,"f":'null'}]},
        {"c":[{"v":"Zucchini","f":'null'},{"v":1,"f":'null'}]},
        {"c":[{"v":"Pepperoni","f":'null'},{"v":2,"f":'null'}]}
      ]
}
    return JsonResponse(data)


def about(request):
    if 'user_id' not in request.session:
        # messages.error(request,'You must be logged in')
        return render(request, "Hikes/about.html")
        
    user_id = request.session['user_id']
    current_user = User.objects.get(id=user_id)
    context = {
        'user': current_user
    }
    return render(request, "Hikes/about.html", context)

def register(request):
    return render(request, "Hikes/register.html")

def login(request):
    return render(request, "Hikes/login.html")

def registerProcess(request):
    errors = User.objects.registration_validator(request.POST)
    if(len(errors))>0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/register')
    else:
        firstName = request.POST.get('firstName')
        print(firstName)
        lastName = request.POST.get('lastName')
        email = request.POST.get('email')
        request.session['firstName'] = firstName
        request.session['email'] = email
        hashed_password = bcrypt.hashpw(request.POST.get('password').encode('utf-8'),bcrypt.gensalt())
        user = User.objects.create(firstName = firstName, lastName = lastName, email = email, password = hashed_password)
        print(hashed_password)
        request.session['user_id'] = user.id 

        return redirect('/')

def loginProcess(request):
    if request.method == "POST":
        errors = User.objects.loginValidator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect("/login")
        else:
            em = request.POST["email"]
            pw = request.POST["password"]
            user = User.objects.filter(email=em)
            if not user: 
                print("failed email")
                messages.error(request, 'Incorrect Login Info') 
                return redirect("/login")
            else:
                user = User.objects.get(email=em)
                if bcrypt.checkpw(pw.encode('utf-8'), user.password.encode('utf-8')):
                    print("password match")
                    
                    request.session["user_id"] = user.id
                    messages.success(request, 'You have succefully logged in')
                    return redirect("/")
                else:
                    print("failed password")
                    messages.error(request, 'Incorrect Login Info') 
                    return redirect("/login")
    # errors = {}
    # email = request.POST.get('email')
    # pw = request.POST.get('password')
    # if len(email) < 1:
    #     errors['email'] = "Email field cannot be blank"
    # if len(pw) < 1:
    #     errors['password'] = 'Password field cannot be blank'
    # else:
    #     user = User.objects.filter(email = email)
    #     if user: 
    #         user = User.objects.get(email = email)
    #         if not bcrypt.checkpw(pw.encode(), user.password.encode()):
                
    #             errors['password'] = "Could not be logged in"
    # if(len(errors)):
    #     for key, value in errors.items():
    #         messages.error(request, value)

    #         return redirect('/login')
    # else:
    #     return redirect ('/')
def logout(request):
    request.session.clear()
    return redirect('/')

def rattle(request):
    # if 'user_id' not in request.session:
    #     # messages.error(request,'You must be logged in')
    #     return render(request, "Hikes/survey.html")

    rattle = int(request.POST.get('rattleSnake'))
    print(rattle)
    user = User.objects.get(rattleSnake = rattle)
    user.rattleSnake += 1
    user.save()
    print(user.rattleSnake)

    return redirect('/survey')

def little(request):
    # if 'user_id' not in request.session:
    #     # messages.error(request,'You must be logged in')
    #     return render(request, "Hikes/survey.html")

    little = int(request.POST.get('littleSi'))
    print(little)
    user = User.objects.get(littleSi = little)
    user.littleSi += 1
    user.save()
    print(user.littleSi)
    # user_id = request.session['user_id']
    # user.add(user_id)
    return redirect('/survey')