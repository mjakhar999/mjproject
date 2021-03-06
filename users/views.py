from django.db.models.query import QuerySet
from django.http import response
from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from datetime import date
from django.views.generic import ListView,DetailView
from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse
import secrets
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json
from .form import UserRegisterForm
from .models import Token
# Create your views here.



def genrate_code():
    code = secrets.token_urlsafe(nbytes=4)
    return code

def register_page(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user_name = form.cleaned_data['username']
            messages.success(request,f"account created for {user_name}")
            return HttpResponseRedirect("home")
        return HttpResponseRedirect(reverse)        
    else:
        form = UserRegisterForm()
    return render(request, "blog/register.html",{"form":form})

@method_decorator(csrf_exempt , name='dispatch')    
def login_user(request):
    
    if request.method =="POST":
        
        if request.body:
            data = json.loads(request.body)
            username = data["username"]
            passw = data['password']
            print("ii",type(username),passw)

            # user = User.objects.filter(username =username).first()
            user = authenticate(request,username= username, password = passw)
            print("user",user)
            if user is not None:
                code = genrate_code()
                Token.objects.create(token=code, user= user).save()
                # request.session['id'] = user.id
                login(request,user)
                response = HttpResponseRedirect('blog/')
                response.set_cookie(key='token',value=code)
                return response
            else:
                return HttpResponse("user not found")

def logout_page(request):
    print('up')
    if request.COOKIES.get("token"):
        print('us')
        # id_s = request.session["id"]
        us = request.user

        print("user",type(us.id))
        tok = Token.objects.get(user__id = us.id)
        print(tok)
        tok.delete()
        print('deleted')
        logout(request)

        response = HttpResponseRedirect('home')
        # response.delete_cookie("token")
        # del request.session['id']
        # request.session.flush()
        print('redirect')
        return response
    else:
        return HttpResponse('error')