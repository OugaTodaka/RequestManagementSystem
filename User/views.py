from django.http import HttpResponse, HttpResponseRedirect
from Management.models import User
from django.urls import reverse
from django.contrib.auth import login, logout
from django.contrib.auth.hashers import check_password
from django.template import loader


def signin(request):
    template = loader.get_template("User/signin.html")
    return HttpResponse(template.render({}, request))


def signin_request(request):
    username = request.POST['username']
    password = request.POST['password']

    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        redirect_url = reverse('User:signin')
        return HttpResponseRedirect(redirect_url)

    if check_password(password, user.password):
        login(request, user)
        # return HttpResponseRedirect(reverse('Management:index'))
        return HttpResponseRedirect("/")
    else:
        redirect_url = reverse('User:signin')
        return HttpResponseRedirect(redirect_url)


def signout(request):
    logout(request)
    return HttpResponseRedirect(reverse('User:signin'))
