from django import forms


class InquiryForm(forms.Form):
    name = forms.CharField(label='名前')
    email = forms.EmailField(label = 'メールアドレス')
    title = forms.CharField(label = 'タイトル',max_length=40)
    message = forms.CharField(label='メッセージ',widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.fields['name'].widget.attrs['placeholder'] = \
            'お名前を入力してください'
        self.fields['name'].widget.attrs['class'] = 'form-control'

        self.fields['email'].widget.attrs['placeholder'] = \
            'メールアドレスを入力してください'
        self.fields['email'].widget.attrs['class'] = 'form-control'

        self.fields['title'].widget.attrs['placeholder'] = \
            'タイトルを入力してください'
        self.fields['title'].widget.attrs['class'] = 'form-control'

        self.fields['message'].widget.attrs['placeholder'] = \
            '問い合わせる内容を入力してください'
        self.fields['message'].widget.attrs['class'] = 'form-control'