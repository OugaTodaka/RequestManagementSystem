import logging
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.views.generic import FormView
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from .forms import InquiryForm
from Management.models import Request
from django.contrib import messages
from django.core.mail import EmailMessage
# Create your views here.

logger = logging.getLogger(__name__)

class IndexView(FormView):
    template_name = 'inquiry/index.html'
    form_class = InquiryForm
    success_url = reverse_lazy('inquiry:success')

    # def get_queryset(self):
    #     request_id = self.kwargs['id']
    #     requests = Request.objects.filter(
    #         request_id=request_id)
    #     return requests

    
    def form_valid(self, form):
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        title = form.cleaned_data['title']
        message = form.cleaned_data['message']
        subject = 'お問い合わせ: {}'.format(title)
        message = \
            '送信者名: {0}\nメールアドレス: {1}\n タイトル:{2}\n メッセージ:\n{3}' \
            .format(name, email, title, message)
        from_email = 'fko2347077@stu.o-hara.ac.jp'
        to_list = ['fko2347077@stu.o-hara.ac.jp']
        message = EmailMessage(subject=subject,
                                body=message,
                                from_email=from_email,
                                to=to_list,
                                )
        message.send()
        messages.success(
            self.request, 'お問い合わせは正常に送信されました。')
        return super().form_valid(form)
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['request_id'] = self.kwargs['id']
        print("Request ID in get_form_kwargs:", self.kwargs['id'])  
        return kwargs
    
class InquirysuccessView(TemplateView):
    template_name = 'inquiry/inquirysuccess.html'