import logging
from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from .forms import InquiryForm
# Create your views here.

logger = logging.getLogger(__name__)

class IndexView(generic.FormView):
    template_name = 'index.html'
    form_class = InquiryForm
    success_url = reverse_lazy('inquiry:inquirysuccess')
    def form_valid(self, form):
        form.send_email()
        logger.info('Inquiry sent by {}'.format(form.cleaned_data['name']))
        return super().form_valid(form)