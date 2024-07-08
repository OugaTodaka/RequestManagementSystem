from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Request,RequestFunction


def top(request):
    template = loader.get_template("Management/top.html")
    data_list = Request.objects.all()
    context = {
        "data_list":data_list,
        "user":request.user,
    }
    return HttpResponse(template.render(context, request))