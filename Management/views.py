from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Request


def top(request):
    template = loader.get_template("Management/top.html")
    data_list = Request.objects.all()
    context = {
        "data_list":data_list,
        "user":request.user,
    }
    return HttpResponse(template.render(context, request))

def detail(request,id):
    template = loader.get_template("Management/detail.html")
    data = Request.objects.get(request_id=id)
    context = {
        "data":data,
        "user":request.user,
    }
    return HttpResponse(template.render(context, request))