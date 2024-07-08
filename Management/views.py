from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Request,RequestFunction


def top(request):
    template = loader.get_template("top.html")
    context = {'user': request.user}
    cliente = Request.objects.all()
    data = {'request': cliente }
    return HttpResponse(template.render(data, request))