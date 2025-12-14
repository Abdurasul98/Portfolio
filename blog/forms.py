from blog.models import *
from django import forms


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Category name',
                'style': 'width: 400px;'
            }),
            'slug': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Slug (auto fill if blank)',
                'style': 'width: 400px;'
            }),
        }


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Tag name',
                'style': 'width: 400px;'
            }),
            'slug': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Slug (auto fill if blank)',
                'style': 'width: 400px;'
            }),
        }


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Blog title',
                'style': 'width: 600px;'
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Write your blog content here',
                'style': 'width: 600px; height: 200px;'
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'style': 'width: 400px;'
            }),
            'status': forms.Select(attrs={
                'class': 'form-control',
                'style': 'width: 200px;'
            }),
            'categories': forms.SelectMultiple(attrs={
                'class': 'form-control',
                'style': 'width: 400px; height: 100px;'
            }),
            'tag': forms.SelectMultiple(attrs={
                'class': 'form-control',
                'style': 'width: 400px; height: 100px;'
            }),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your name',
                'style': 'width: 400px;'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your email',
                'style': 'width: 400px;'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Your comment here',
                'style': 'width: 600px; height: 150px;'
            }),
            'blog': forms.Select(attrs={
                'class': 'form-control',
                'style': 'width: 400px;'
            }),
        }