from portfolio.models import AboutMe, Education, Experience, Skills, Project, ProjectImage, YoutubeVideo
from django import forms
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox

class ResumeDownloadForm(forms.Form):
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox())



class AboutMeForm(forms.ModelForm):
    class Meta:
        model = AboutMe
        fields = '__all__'
        widgets = {
            'my_name': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Your Name', 'style': 'width:400px;'}),
            'about_me': forms.Textarea(
                attrs={'class': 'form-control', 'placeholder': 'About you', 'style': 'width:600px; height:150px;'}),
            'skills': forms.SelectMultiple(attrs={'class': 'form-control', 'style': 'width:400px; height:100px;'}),
            'social_media': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Social media JSON',
                                                  'style': 'width:600px; height:100px;'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control', 'style': 'width:400px;'}),
        }


class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = '__all__'
        widgets = {
            'start_year': forms.TextInput(attrs={'class': 'form-control', 'style': 'width:150px;'}),
            'end_year': forms.TextInput(attrs={'class': 'form-control', 'style': 'width:150px;'}),
            'degree': forms.TextInput(attrs={'class': 'form-control', 'style': 'width:400px;'}),
            'university': forms.TextInput(attrs={'class': 'form-control', 'style': 'width:400px;'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'style': 'width:600px; height:150px;'}),
        }


class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = '__all__'
        widgets = {
            'start_year': forms.TextInput(attrs={'class': 'form-control', 'style': 'width:150px;'}),
            'end_year': forms.TextInput(attrs={'class': 'form-control', 'style': 'width:150px;'}),
            'position': forms.TextInput(attrs={'class': 'form-control', 'style': 'width:400px;'}),
            'company': forms.TextInput(attrs={'class': 'form-control', 'style': 'width:400px;'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'style': 'width:600px; height:150px;'}),
            'about_me': forms.Select(attrs={'class': 'form-control', 'style': 'width:400px;'}),
        }


class SkillsForm(forms.ModelForm):
    class Meta:
        model = Skills
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Skill name', 'style': 'width:400px;'}),
        }


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'style': 'width:400px;'}),
            'year': forms.TextInput(attrs={'class': 'form-control', 'style': 'width:150px;'}),
            'clint': forms.TextInput(attrs={'class': 'form-control', 'style': 'width:400px;'}),
            'service': forms.TextInput(attrs={'class': 'form-control', 'style': 'width:400px;'}),
            'project_type': forms.TextInput(attrs={'class': 'form-control', 'style': 'width:400px;'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'style': 'width:600px; height:150px;'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class ProjectImageForm(forms.ModelForm):
    class Meta:
        model = ProjectImage
        fields = '__all__'
        widgets = {
            'project': forms.Select(attrs={'class': 'form-control', 'style': 'width:400px;'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control', 'style': 'width:400px;'}),
        }


class YoutubeVideoForm(forms.ModelForm):
    class Meta:
        model = YoutubeVideo
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'style': 'width:400px;'}),
            'link': forms.URLInput(attrs={'class': 'form-control', 'style': 'width:600px;'}),
            'thumbnail': forms.ClearableFileInput(attrs={'class': 'form-control', 'style': 'width:400px;'}),
        }