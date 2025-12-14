import requests
from django.contrib import messages
from django.conf import settings
from django.http import Http404
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, DetailView
from django.views import View
from portfolio.models import *


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

    def getqueryset(self):
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



