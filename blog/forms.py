
from django.forms import ModelForm, EmailInput, TextInput, Textarea

from blog.models import Comment, Reply, Contact

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'mail', 'content')
        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'お名前',
            }),
            'mail': EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'メールアドレス',
            }),
            'content': Textarea(attrs={
                'class': 'form-control',
                'placeholder': '内容',
            }),
        }
        labels = {
            'name': '',
            'mail': '',
            'content': '',
        }
        max_length = {
            'name': 100,
        }

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'text')
        widgets = {
            'author': TextInput(attrs={
                'class': 'form-control',
                'placeholder': '名前',
            }),
            'text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'コメント内容',
            }),
        }
        labels = {
            'author': '',
            'text': '',
        }


class ReplyForm(ModelForm):
    class Meta:
        model = Reply
        fields = ('author', 'text')
        widgets = {
            'author': TextInput(attrs={
                'class': 'form-control',
                'placeholder': '名前',
            }),
            'text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': '返信内容',
            }),
        }
        labels = {
            'author': '',
            'text': '',
        }