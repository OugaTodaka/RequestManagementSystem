from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Request
from django.urls import reverse
from django.contrib.auth.decorators import login_required

@login_required
def top(request):
    template = loader.get_template("requestForm/top.html")
    data_list = Request.objects.all()
    context = {
        "data_list":data_list,
        "user":request.user,
    }
    return HttpResponse(template.render(context, request))

@login_required
def detail(request,id):
    template = loader.get_template("requestForm/detail.html")
    data = Request.objects.get(request_id=id)
    context = {
        "data":data,
        "user":request.user,
    }
    return HttpResponse(template.render(context, request))

@login_required
def detail_update(request,id):
    data = Request.objects.get(request_id=id)
    data.system_name = request.POST.get("system_name")
    data.system_overview = request.POST.get("system_overview")
    data.status = request.POST.get("status")
    data.save()
    return HttpResponseRedirect(reverse("requestForm:detail",args=[id]))

@login_required
def portfolio(request):
    template = loader.get_template("requestForm/portfolio.html")
    data_list = Request.objects.all()
    context = {
        "data_list":data_list,
        "user":request.user,
    }
    return HttpResponse(template.render(context, request))