from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import CustomUser
from django.urls import reverse
from django.contrib.auth import login,logout
from django.template import loader

def signin(request):
    template = loader.get_template("User/signin.html")
    return HttpResponse(template.render({}, request))

def signin_request(request):
    username = request.POST['username']
    password = request.POST['password']

    try:
        user = CustomUser.objects.get(username=username)
    except CustomUser.DoesNotExist:
        redirect_url = reverse('User:signin')
        return HttpResponseRedirect(redirect_url)

    if user.password == password:
        login(request, user)
        # return HttpResponseRedirect(reverse('Management:index'))
        return HttpResponseRedirect("/top")
    else:
        redirect_url = reverse('User:signin')
        return HttpResponseRedirect(redirect_url)

def signout(request):
    logout(request)
    return HttpResponseRedirect(reverse('User:signin'))