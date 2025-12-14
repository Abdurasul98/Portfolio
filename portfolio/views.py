import textwrap

import requests
from django.contrib import messages
from django.conf import settings
from django.http import Http404, FileResponse, HttpResponse
from django.shortcuts import render, redirect
from django.utils.html import strip_tags
from django.views.generic import *
from django.views import View
from reportlab.lib.pagesizes import A4
from portfolio.forms import *
from django.urls import reverse_lazy
from reportlab.pdfgen import canvas
from io import BytesIO

from portfolio.models import (
    AboutMe, Education, Experience, Skills, Project
)

def index(request):
    return render(request, 'index.html')


class AboutView(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['about_me'] = AboutMe.objects.select_related('user').first()
        context['experiences'] = Experience.objects.filter(about_me=context['about_me'])
        context['educations'] = Education.objects.filter(about_me=context['about_me'])
        return context


class CredentialsView(TemplateView):
    template_name = 'credentials.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        about_me = AboutMe.objects.select_related('user').first()

        context['about_me'] = about_me
        context['experiences'] = Experience.objects.filter(about_me=about_me) if about_me else []
        context['educations'] = Education.objects.filter(about_me=about_me) if about_me else []
        context['social_media'] = about_me.social_media if about_me else []
        context['skills'] = about_me.skills.all() if about_me else []
        return context

class WorkView(ListView):
    model = Project
    template_name = 'works.html'
    context_object_name = 'projects'


    def get_queryset(self):
        return Project.objects.prefetch_related('images').order_by('year')


class WorkDetailView(DetailView):
    model = Project
    template_name = 'work_detail.html'
    context_object_name = 'project'

    def get_queryset(self):
        return Project.objects.prefetch_related('images').order_by('year')

    def get_object(self, queryset=None):
        slug = self.kwargs.get('slug')
        try:
            return Project.objects.prefetch_related('images').get(slug=slug)
        except Project.DoesNotExist:
            raise Http404('Project does not exist')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        projects = list(Project.objects.order_by('id'))
        current_index = projects.index(self.object)
        next_project = projects[current_index + 1] if current_index + 1 < len(projects) else None
        context['next_project'] = next_project
        return context



class ContactView(View):
    template_name = 'contact.html'

    def get(self, request):
        return render(request, self.template_name)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        about_me = AboutMe.objects.select_related('user').first()

        context['about_me'] = about_me
        context['social_media'] = about_me.social_media if about_me else {}

        return context

    def post(self, request):
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        bot_token = settings.BOT_TOKEN
        chat_id = settings.TELEGRAM_CHAT_ID

        telegram_message = (
            f"**New Contact Message\n\n"
            f"Name: {full_name}\n\n"
            f"Email: {email}\n\n"
            f"Message: {message}\n\n"
        )

        url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
        payload = {
            "chat_id": chat_id,
            "text": telegram_message,
            "parse_mode": "Markdown",
        }

        response = requests.post(url, data=payload)

        if response.status_code == 200:
            messages.success(request,f"Message sent successfully")
        else:
            messages.error(request,f"Error sending message")
        return redirect('/')





class AboutMeListView(ListView):
    model = AboutMe
    template_name = 'portfolio_aboutme_list_form.html'
    context_object_name = 'aboutmes'


class AboutMeCreateView(CreateView):
    model = AboutMe
    form_class = AboutMeForm
    template_name = 'portfolio_aboutme_create_form.html'
    success_url = reverse_lazy('admin_index')


class AboutMeUpdateView(UpdateView):
    model = AboutMe
    form_class = AboutMeForm
    template_name = 'portfolio_aboutme_update_form.html'
    success_url = reverse_lazy('admin_index')


class AboutMeDeleteView(DeleteView):
    model = AboutMe
    template_name = 'portfolio_aboutme_delete_form.html'
    success_url = reverse_lazy('admin_index')



class EducationListView(ListView):
    model = Education
    template_name = 'portfolio_education_list_form.html'
    context_object_name = 'educations'


class EducationCreateView(CreateView):
    model = Education
    form_class = EducationForm
    template_name = 'portfolio_education_create_form.html'
    success_url = reverse_lazy('admin_index')


class EducationUpdateView(UpdateView):
    model = Education
    form_class = EducationForm
    template_name = 'portfolio_education_update_form.html'
    success_url = reverse_lazy('admin_index')


class EducationDeleteView(DeleteView):
    model = Education
    template_name = 'portfolio_education_delete_form.html'
    success_url = reverse_lazy('admin_index')



class ExperienceListView(ListView):
    model = Experience
    template_name = 'portfolio_experience_list_form.html'
    context_object_name = 'experiences'


class ExperienceCreateView(CreateView):
    model = Experience
    form_class = ExperienceForm
    template_name = 'portfolio_experience_create_form.html'
    success_url = reverse_lazy('admin_index')


class ExperienceUpdateView(UpdateView):
    model = Education
    form_class = ExperienceForm
    template_name = 'portfolio_experience_update_form.html'
    success_url = reverse_lazy('admin_index')


class ExperienceDeleteView(DeleteView):
    model = Experience
    template_name = 'portfolio_experience_delete_form.html'
    success_url = reverse_lazy('admin_index')



class SkillsListView(ListView):
    model = Skills
    template_name = 'portfolio_skills_list_form.html'
    context_object_name = 'skills'


class SkillsCreateView(CreateView):
    model = Skills
    form_class = SkillsForm
    template_name = 'portfolio_skills_create_form.html'
    success_url = reverse_lazy('admin_index')


class SkillsUpdateView(UpdateView):
    model = Skills
    form_class = SkillsForm
    template_name = 'portfolio_skills_update_form.html'
    success_url = reverse_lazy('admin_index')


class SkillsDeleteView(DeleteView):
    model = Skills
    template_name = 'portfolio_skills_delete_form.html'
    success_url = reverse_lazy('admin_index')



class ProjectListView(ListView):
    model = Project
    template_name = 'portfolio_project_list_form.html'
    context_object_name = 'projects'


class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectForm
    template_name = 'portfolio_project_create_form.html'
    success_url = reverse_lazy('admin_index')


class ProjectUpdateView(UpdateView):
    model = Project
    form_class = ProjectForm
    template_name = 'portfolio_project_update_form.html'
    success_url = reverse_lazy('admin_index')


class ProjectDeleteView(DeleteView):
    model = Project
    template_name = 'portfolio_project_delete_form.html'
    success_url = reverse_lazy('admin_index')



class ProjectImageListView(ListView):
    model = ProjectImage
    template_name = 'portfolio_projectimage_list_form.html'
    context_object_name = 'images'


class ProjectImageCreateView(CreateView):
    model = ProjectImage
    form_class = ProjectImageForm
    template_name = 'portfolio_projectimage_create_form.html'
    success_url = reverse_lazy('admin_index')


class ProjectImageUpdateView(UpdateView):
    model = ProjectImage
    form_class = ProjectImageForm
    template_name = 'portfolio_projectimage_update_form.html'
    success_url = reverse_lazy('admin_index')


class ProjectImageDeleteView(DeleteView):
    model = ProjectImage
    template_name = 'portfolio_projectimage_delete_form.html'
    success_url = reverse_lazy('admin_index')



class YoutubeVideoListView(ListView):
    model = YoutubeVideo
    template_name = 'portfolio_youtubevideo_list_form.html'
    context_object_name = 'videos'


class YoutubeVideoCreateView(CreateView):
    model = YoutubeVideo
    form_class = YoutubeVideoForm
    template_name = 'portfolio_youtubevideo_create_form.html'
    success_url = reverse_lazy('admin_index')


class YoutubeVideoUpdateView(UpdateView):
    model = YoutubeVideo
    form_class = YoutubeVideoForm
    template_name = 'portfolio_youtubevideo_update_form.html'
    success_url = reverse_lazy('admin_index')


class YoutubeVideoDeleteView(DeleteView):
    model = YoutubeVideo
    template_name = 'portfolio_youtubevideo_delete_form.html'
    success_url = reverse_lazy('admin_index')





def resume_download_view(request):
    if request.method == "POST":
        recaptcha_response = request.POST.get('g-recaptcha-response')

        data = {
            'secret': settings.RECAPTCHA_SECRET_KEY,
            'response': recaptcha_response
        }

        r = requests.post(
            'https://www.google.com/recaptcha/api/siteverify',
            data=data
        )
        result = r.json()

        if not result.get('success'):
            return render(request, 'portfolio_resume_download.html', {
                'error': 'Captcha tasdiqlanmadi',
                'RECAPTCHA_SITE_KEY': settings.RECAPTCHA_SITE_KEY
            })

        pdf_buffer = generate_resume_pdf()
        response = HttpResponse(pdf_buffer, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="Resume.pdf"'
        return response

    return render(request, 'portfolio_resume_download.html', {
        'RECAPTCHA_SITE_KEY': settings.RECAPTCHA_SITE_KEY
    })

def generate_resume_pdf():
    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=A4)
    width, height = A4
    y = height - 50

    about = AboutMe.objects.first()

    if about:
        p.setFont("Helvetica-Bold", 16)
        p.drawString(50, y, about.my_name)
        y -= 30

        p.setFont("Helvetica", 12)
        text = p.beginText(50, y)

        if about.about_me:
            clean_about_me = strip_tags(about.about_me)
            lines = textwrap.wrap(clean_about_me, width=80)  # width – qator uzunligi (tahrirlash mumkin)
            for line in lines:
                text.textLine(line)
        p.drawText(text)
        y -= 80

        skills = ", ".join([s.name for s in about.skills.all()])
        if skills:
            p.drawString(50, y, f"Skills: {skills}")
            y -= 30

        p.setFont("Helvetica-Bold", 14)
        p.drawString(50, y, "Education")
        y -= 20
        p.setFont("Helvetica", 12)
        for edu in Education.objects.filter(about_me=about):
            p.drawString(60, y, f"{edu.degree} - {edu.university}")
            y -= 15

        y -= 20
        p.setFont("Helvetica-Bold", 14)
        p.drawString(50, y, "Experience")
        y -= 20
        p.setFont("Helvetica", 12)
        for exp in Experience.objects.filter(about_me=about):
            p.drawString(60, y, f"{exp.position} - {exp.company}")
            y -= 15

    p.showPage()
    p.save()
    buffer.seek(0)
    return buffer