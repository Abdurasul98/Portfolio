from portfolio.models import AboutMe, Education, Experience, Skills, Project, ProjectImage, YoutubeVideo
from django import forms

class AboutMeForm(forms.ModelForm):
    class Meta:
        model = AboutMe
        fields = '__all__'


class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = '__all__'


class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = '__all__'


class SkillsForm(forms.ModelForm):
    class Meta:
        model = Skills
        fields = '__all__'


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'


class ProjectImageForm(forms.ModelForm):
    class Meta:
        model = ProjectImage
        fields = '__all__'


class YoutubeVideoForm(forms.ModelForm):
    class Meta:
        model = YoutubeVideo
        fields = '__all__'