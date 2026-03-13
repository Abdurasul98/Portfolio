from django.urls import path
from blog.views import *

urlpatterns = [
    path('blog/',BlogListView.as_view(),name='blog_list'),
    
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('admin_index/', admin_index_view, name='admin_index'),

    path('category/',CategoryListView.as_view(),name='blog_category_list_form'),
    path('category/add/',CategoryCreateView.as_view(),name='blog_category_create_form'),
    path('category/<int:pk>/delete/',CategoryDeleteView.as_view(),name='blog_category_delete_form'),
    path('category/<int:pk>/update/',CategoryUpdateView.as_view(),name='blog_category_update_form'),

    path('tag/', TagListView.as_view(), name='blog_tag_list_form'),
    path('tag/add/', TagCreateView.as_view(), name='blog_tag_create_form'),
    path('tag/<int:pk>/delete/', TagDeleteView.as_view(), name='blog_tag_delete_form'),
    path('tag/<int:pk>/update/', TagUpdateView.as_view(), name='blog_tag_update_form'),

    path('manage-blog/', BlogListsView.as_view(), name='blog_blog_list_form'),
    path('manage-blog/add/', BlogCreateView.as_view(), name='blog_blog_create_form'),
    path('manage-blog/<int:pk>/delete/', BlogDeleteView.as_view(), name='blog_blog_delete_form'),
    path('manage-blog/<int:pk>/update/', BlogUpdateView.as_view(), name='blog_blog_update_form'),

    path('blog/<slug:slug>/',BlogDetailView.as_view(),name='blog_detail'),

    path('comment/', CommentListView.as_view(), name='blog_comment_list_form'),
    path('comment/add/', CommentCreateView.as_view(), name='blog_comment_create_form'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='blog_comment_delete_form'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='blog_comment_update_form'),

]