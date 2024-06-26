from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def top(request):
    template = loader.get_template("top.html")
    context = {'user': request.user}
    return HttpResponse(template.render({}, request))