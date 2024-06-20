from django.shortcuts import render
from django.views import generic
from django.views.generic.base import TemplateView
# Create your views here.

class IndexView(generic.FormView):
    template_name = 'index.html'
    form_class = InquiryForm
