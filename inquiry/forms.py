from django import forms
from django.core.mail import EmailMessage


class InquiryForm(forms.Form):
    name = forms.CharField(label='名前')
    email = forms.EmailField(label = 'メールアドレス')
    title = forms.CharField(label = '件名',max_length=40)
    message = forms.CharField(label='問い合わせ内容',widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.fields['name'].widget.attrs['placeholder'] = \
            'お名前を入力してください'
        self.fields['name'].widget.attrs['class'] = 'form-control'

        self.fields['email'].widget.attrs['placeholder'] = \
            'メールアドレスを入力してください'
        self.fields['email'].widget.attrs['class'] = 'form-control'

        self.fields['title'].widget.attrs['placeholder'] = \
            '件名を入力してください'
        self.fields['title'].widget.attrs['class'] = 'form-control'

        self.fields['message'].widget.attrs['placeholder'] = \
            '問い合わせる内容を入力してください'
        self.fields['message'].widget.attrs['class'] = 'form-control'

    def send_email(self):
        name = self.cleaned_data['name']
        email = self.changed_data['email']
        title = self.changed_data['title']
        message = self.changed_data['message']

        subject = 'お問い合わせ{}'.format(title)
        message = '送信者名: {0}\nメールアドレス: {1}\nメッセージ:\n{2}'.format(name,email,message)
        from_email = 'fko2347077@stu.o-hara.ac.jp'
        to_list = [
            'fko2347077@stu.o-hara.ac.jp'
        ]
        cc_list = [
            email
        ]
        message = EmailMessage(subject=subject,body=message, from_email=from_email, to=to_list, cc=cc_list)
        message.send()