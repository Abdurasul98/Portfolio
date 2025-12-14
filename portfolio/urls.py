from django.urls import path
from portfolio.views import *

urlpatterns = [
    path('',index,name='index'),
    path('about/',AboutView.as_view(),name='about'),
    path('credentials/',CredentialsView.as_view(),name='credentials'),
    path('works/',WorkView.as_view(),name='works'),
    path('work/<slug:slug>/',WorkDetailView.as_view(),name='work_detail'),
    path('contact/',ContactView.as_view(),name='contact'),

]
