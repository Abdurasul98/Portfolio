from blog.models import *
from django import forms


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = '__all__'


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'