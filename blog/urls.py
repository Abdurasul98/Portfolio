from django.urls import path
from blog.views import *

urlpatterns = [
    path('blog/',BlogListView.as_view(),name='blog_list'),
    path('blog/<slug:slug>/',BlogDetailView.as_view(),name='blog_detail'),


    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('admin_index/', admin_index_view, name='admin_index'),

]