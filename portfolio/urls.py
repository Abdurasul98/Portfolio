from django.urls import path
from portfolio.views import *

urlpatterns = [
    path('',index,name='index'),
    path('about/',AboutView.as_view(),name='about'),
    path('credentials/',CredentialsView.as_view(),name='credentials'),
    path('works/',WorkView.as_view(),name='works'),
    path('work/<slug:slug>/',WorkDetailView.as_view(),name='work_detail'),
    path('contact/',ContactView.as_view(),name='contact'),
    path('resume/download/', resume_download_view, name='resume_download'),


    # AboutMe
    path('aboutme/', AboutMeListView.as_view(), name='portfolio_aboutme_list_form'),
    path('aboutme/add/', AboutMeCreateView.as_view(), name='portfolio_aboutme_create_form'),
    path('aboutme/<int:pk>/update/', AboutMeUpdateView.as_view(), name='portfolio_aboutme_update_form'),
    path('aboutme/<int:pk>/delete/', AboutMeDeleteView.as_view(), name='portfolio_aboutme_delete_form'),

    # Education
    path('education/', EducationListView.as_view(), name='portfolio_education_list_form'),
    path('education/add/', EducationCreateView.as_view(), name='portfolio_education_create_form'),
    path('education/<int:pk>/update/', EducationUpdateView.as_view(), name='portfolio_education_update_form'),
    path('education/<int:pk>/delete/', EducationDeleteView.as_view(), name='portfolio_education_delete_form'),

    # Experience
    path('experience/', ExperienceListView.as_view(), name='portfolio_experience_list_form'),
    path('experience/add/', ExperienceCreateView.as_view(), name='portfolio_experience_create_form'),
    path('experience/<int:pk>/update/', ExperienceUpdateView.as_view(), name='portfolio_experience_update_form'),
    path('experience/<int:pk>/delete/', ExperienceDeleteView.as_view(), name='portfolio_experience_delete_form'),

    # Skills
    path('skills/', SkillsListView.as_view(), name='portfolio_skills_list_form'),
    path('skills/add/', SkillsCreateView.as_view(), name='portfolio_skills_create_form'),
    path('skills/<int:pk>/update/', SkillsUpdateView.as_view(), name='portfolio_skills_update_form'),
    path('skills/<int:pk>/delete/', SkillsDeleteView.as_view(), name='portfolio_skills_delete_form'),

    # Project
    path('project/', ProjectListView.as_view(), name='portfolio_project_list_form'),
    path('project/add/', ProjectCreateView.as_view(), name='portfolio_project_create_form'),
    path('project/<int:pk>/update/', ProjectUpdateView.as_view(), name='portfolio_project_update_form'),
    path('project/<int:pk>/delete/', ProjectDeleteView.as_view(), name='portfolio_project_delete_form'),

    # ProjectImage
    path('projectimage/', ProjectImageListView.as_view(), name='portfolio_projectimage_list_form'),
    path('projectimage/add/', ProjectImageCreateView.as_view(), name='portfolio_projectimage_create_form'),
    path('projectimage/<int:pk>/update/', ProjectImageUpdateView.as_view(), name='portfolio_projectimage_update_form'),
    path('projectimage/<int:pk>/delete/', ProjectImageDeleteView.as_view(), name='portfolio_projectimage_delete_form'),

    # YoutubeVideo
    path('youtubevideo/', YoutubeVideoListView.as_view(), name='portfolio_youtubevideo_list_form'),
    path('youtubevideo/add/', YoutubeVideoCreateView.as_view(), name='portfolio_youtubevideo_create_form'),
    path('youtubevideo/<int:pk>/update/', YoutubeVideoUpdateView.as_view(), name='portfolio_youtubevideo_update_form'),
    path('youtubevideo/<int:pk>/delete/', YoutubeVideoDeleteView.as_view(), name='portfolio_youtubevideo_delete_form'),

]
