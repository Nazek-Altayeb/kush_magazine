from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'body', 'author',)
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'required': 'True'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'required': 'True'}),
            # 'author': forms.Select(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value': '',  'id': 'user-id', 'type': 'hidden'}),
        }


class EditArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'body',)
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }
