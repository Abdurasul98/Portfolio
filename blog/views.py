from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from rest_framework.reverse import reverse_lazy
from blog.forms import CategoryForm, TagForm, BlogForm, CommentForm
from blog.models import Blog, Category,Tag,Comment
import bleach
from django.contrib.auth import authenticate, login, logout





def truncate_html(context, length):
    allow_tags = ['p','b','i','u','a','br', 'strong', 'em', 'code', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6']

    truncated_context = bleach.clean(context, tags=allow_tags, strip=True)

    if len(truncated_context) > length:
        truncated_context = truncated_context[:length]
    return truncated_context


class BlogListView(ListView):
    model = Blog
    template_name = 'blog_list.html'
    context_object_name = 'blogs'

    def get_queryset(self):
        blogs = Blog.objects.filter(status='published').order_by('-created_at')
        category_slug = self.request.GET.get('category')

        if category_slug:
            blogs = blogs.filter(categories__slug=category_slug)

        for blog in blogs:
            blog.truncate_content = truncate_html(blog.content,150)
        return blogs


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recent_posts'] = Blog.objects.filter(status='published').order_by('-created_at')[:5]
        context['categories'] = Category.objects.order_by('name')
        context['tegs'] = Tag.objects.order_by('name')
        return context


class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog_detail.html'
    context_object_name = 'blog'

    def post(self,request,*args,**kwargs):
        blog = self.get_object()
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        if name and email and message:
            Comment.objects.create(blog=blog,name=name,email=email,message=message)
            return redirect('blog_detail',slug=blog.slug)

    def get_queryset(self):
        return Blog.objects.filter(status='published')

    def get_object(self,queryset=None):
        slug = self.kwargs.get('slug')
        return self.get_queryset().get(slug=slug)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recent_posts'] = Blog.objects.filter(status='published').order_by('-created_at')[:5]
        context['categories'] = Category.objects.order_by('name')
        context['tegs'] = Tag.objects.order_by('name')
        context['comments'] = Comment.objects.filter(blog=self.object).order_by('-created_at')

        return context



class CategoryListView(ListView):
    model = Category
    template_name = 'blog_category_list_form.html'
    context_object_name = 'categories'


class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'blog_category_create_form.html'
    success_url = reverse_lazy('admin_index')


class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'blog_category_update_form.html'
    success_url = reverse_lazy('admin_index')


class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'blog_category_delete_form.html'
    success_url = reverse_lazy('admin_index')



class TagListView(ListView):
    model = Tag
    template_name = 'blog_tag_list_form.html'
    context_object_name = 'tags'


class TagCreateView(CreateView):
    model = Tag
    form_class = TagForm
    template_name = 'blog_tag_create_form.html'
    success_url = reverse_lazy('admin_index')


class TagUpdateView(UpdateView):
    model = Tag
    form_class = TagForm
    template_name = 'blog_tag_update_form.html'
    success_url = reverse_lazy('admin_index')


class TagDeleteView(DeleteView):
    model = Tag
    template_name = 'blog_tag_delete_form.html'
    success_url = reverse_lazy('admin_index')



class BlogListView(ListView):
    model = Blog
    template_name = 'blog_blog_list_form.html'
    context_object_name = 'blogs'


class BlogCreateView(CreateView):
    model = Blog
    form_class = BlogForm
    template_name = 'blog_blog_create_form.html'
    success_url = reverse_lazy('admin_index')


class BlogUpdateView(UpdateView):
    model = Blog
    form_class = BlogForm
    template_name = 'blog_blog_update_form.html'
    success_url = reverse_lazy('admin_index')


class BlogDeleteView(DeleteView):
    model = Blog
    template_name = 'blog_blog_delete_form.html'
    success_url = reverse_lazy('admin_index')



class CommentListView(ListView):
    model = Comment
    template_name = 'blog_comment_list_form.html'
    context_object_name = 'comments'


class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog_comment_create_form.html'
    success_url = reverse_lazy('admin_index')


class CommentUpdateView(UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog_comment_update_form.html'
    success_url = reverse_lazy('admin_index')


class CommentDeleteView(DeleteView):
    model = Comment
    template_name = 'blog_comment_delete_form.html'
    success_url = reverse_lazy('admin_index')






@login_required
@user_passes_test(lambda u: u.is_superuser)
def admin_index_view(request):
    categories = Category.objects.all()
    return render(request, 'admin_index.html',{'categories': categories})


def logout_view(request):
    logout(request)
    return redirect('index')

def login_view(request):
    logout(request)


    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        print("Login attempt:", email, password)
        user = authenticate(request, email=email, password=password)
        print("authenticate returned:", user)

        if user is not None and user.is_superuser:
            login(request, user)
            return redirect('admin_index')
        else:
            return render(request, 'login.html', {'error': 'Login yoki parol xato!'})

    return render(request, 'login.html')