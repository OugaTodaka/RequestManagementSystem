from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Request
from django.contrib.auth.decorators import login_required

@login_required
def top(request):
    template = loader.get_template("Management/top.html")
    data_list = Request.objects.all()
    context = {
        "data_list":data_list,
        "user":request.user,
    }
    return HttpResponse(template.render(context, request))

@login_required
def detail(request,id):
    template = loader.get_template("Management/detail.html")
    data = Request.objects.get(request_id=id)
    context = {
        "data":data,
        "user":request.user,
    }
    return HttpResponse(template.render(context, request))

@login_required
def portfolio(request):
    template = loader.get_template("Management/portfolio.html")
    data_list = Request.objects.all()
    context = {
        "data_list":data_list,
        "user":request.user,
    }
    return HttpResponse(template.render(context, request))