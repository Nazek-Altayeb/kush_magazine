from django import forms
from .models import Article, Category, Comment


categories = Category.objects.all().values_list('name', 'name')
categories_list = []
for category in categories:
    categories_list.append(category)


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'author', 'category', 'body', )
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'required': 'True'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value': '',  'id': 'user-id', 'type': 'hidden'}),
            'category': forms.Select(choices=categories_list, attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'required': 'True'}),
        }


class EditArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'body',)
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name',)
        widget = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("date_and_time","body",)

