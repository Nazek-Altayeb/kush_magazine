from django import forms
from .models import Article, Comment, Topic


if Topic.objects.all():
    topics = Topic.objects.all().values_list('name', 'name')
    topics_list = []
    for topic in topics:
        topics_list.append(topic)
    

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'author', 'topic', 'body', )
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'required': 'True'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value': '',  'id': 'user-id', 'type': 'hidden'}),       
            'topic': forms.Select(choices=topics_list, attrs={'class': 'form-control'}),
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


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
        widget = {
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ('name',)
        widget = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }
