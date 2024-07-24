from django import forms
from django.core.mail import EmailMessage
from Management.models import Request


class InquiryForm(forms.Form):
    name = forms.CharField(label='チーム名')
    title = forms.CharField(label = '件名',max_length=40)
    message = forms.CharField(label='問い合わせ内容',widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        request_id = kwargs.pop('request_id', None)
        print("Request ID in form init:", request_id)
        super().__init__(*args, **kwargs)

        # if request_id:
        #     try:
        #         request_instance = Request.objects.get(request_id=request_id)
        #         self.fields['name'].initial = request_instance.name
        #         self.fields['email'].initial = request_instance.mail
        #         print("Name:", request_instance.name)  # デバッグプリント
        #         print("Email:", request_instance.mail)  # デバッグプリント
        #     except Request.DoesNotExist:
        #         print("Request with id {} does not exist".format(request_id))

        # # self.fields['name'].widget.attrs['readonly'] = True
        # # self.fields['email'].widget.attrs['readonly'] = True

        self.fields['name'].widget.attrs['placeholder'] = 'チーム名を入力してください'
        self.fields['name'].widget.attrs['class'] = 'form-control'

        self.fields['title'].widget.attrs['placeholder'] = \
            '件名を入力してください'
        self.fields['title'].widget.attrs['class'] = 'form-control'

        self.fields['message'].widget.attrs['placeholder'] = \
            '問い合わせる内容を入力してください'
        self.fields['message'].widget.attrs['class'] = 'form-control'
