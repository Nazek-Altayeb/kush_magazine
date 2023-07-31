from django import forms
from .models import Article, Comment, Topic


topics = Topic.objects.all().values_list('name', 'name')
topics_list = []
for topic in topics:
    topics_list.append(topic)


class ArticleForm(forms.ModelForm):
    """
    Form model that allows moderators to
    create and save articles
    """
    class Meta:
        model = Article
        fields = ('title', 'author', 'topic', 'body', )
        widgets = {
            'title': forms.TextInput(
                attrs={'class': 'form-control', 'required': 'True'}),
            'author': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'value': '',
                    'id': 'user-id',
                    'type': 'hidden'}),
            'topic': forms.Select(
                choices=topics_list, attrs={'class': 'form-control'}),
            'body': forms.Textarea(
                attrs={'class': 'form-control', 'required': 'True'}),
        }


class EditArticleForm(forms.ModelForm):
    """
    Form model that allows a moderator to
    change articles content,only those that are written by him/her 
    """
    class Meta:
        model = Article
        fields = ('title', 'body',)
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }


class CommentForm(forms.ModelForm):
    """
    Form model that allows authenticated users to
    comment on articles
    """
    class Meta:
        model = Comment
        fields = ('body',)
        widget = {
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }


class TopicForm(forms.ModelForm):
    """
    Form model that allows moderators to
    create and save topics
    """
    class Meta:
        model = Topic
        fields = ('name',)
        widget = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }
