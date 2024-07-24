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
    model = Request
    template_name = 'inquiry/index.html'
    form_class = InquiryForm
    success_url = reverse_lazy('inquiry:success')

    # def get_initial(self):
    #     initial = super().get_initial()
    #     pk = self.kwargs.get('pk')
    #     my_model_instance = MyModel.objects.get(pk=pk)
    #     initial['readonly_field'] = my_model_instance.some_field
    #     return initial

    # def get_form_kwargs(self):
    #     kwargs = super().get_form_kwargs()
    #     pk = self.kwargs.get('pk')
    #     my_model_instance = MyModel.objects.get(pk=pk)
    #     kwargs['readonly_value'] = my_model_instance.some_field
    #     return kwargs

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['request_id'] = self.kwargs['id']
        print("Request ID in get_form_kwargs:", self.kwargs['id'])  
        return kwargs
    
    
    
    def form_valid(self, form):
        name = form.cleaned_data['name']
        title = form.cleaned_data['title']
        message = form.cleaned_data['message']
        subject = 'お問い合わせ: {}'.format(title)
        message = \
            '送信者名: {0}\n タイトル:{1}\n メッセージ:\n{2}' \
            .format(name,title, message)
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
    
class InquirysuccessView(TemplateView):
    template_name = 'inquiry/inquirysuccess.html'