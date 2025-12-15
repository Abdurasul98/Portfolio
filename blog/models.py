from django.contrib.auth import get_user_model
from django.db import models
from django.utils.text import slugify
from tinymce.models import HTMLField
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver


class Category(models.Model):
    name = models.CharField(max_length=100,unique=True,help_text='Category Name,e.g. , Technology')
    slug = models.SlugField(unique=True,blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100,unique=True,help_text='Tag Name,e.g. , Technology')
    slug = models.SlugField(unique=True,blank=True)


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


    def __str__(self):
        return self.name


class Blog(models.Model):

    STATUS_CHOICES = (
        ('draft','Draft'),
        ('published','Published'),
        ('disabled','Disabled')
    )


    title = models.CharField(max_length=200,help_text='Title of the blog post')
    content = HTMLField(help_text='Content of blog post')
    image = models.ImageField(upload_to='blog/images',blank=True,help_text='Blog post image')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True,blank=True)
    auther = models.ForeignKey(get_user_model(), on_delete= models.CASCADE,related_name='blog_auther',null=True,blank=True)

    categories = models.ManyToManyField(Category,related_name='blogs',blank=True)
    tag = models.ManyToManyField(Tag,related_name='blogs',blank=True)
    comments_count = models.PositiveIntegerField(default=0,editable=False,help_text='Number of comments')
    share_count = models.PositiveIntegerField(default=0,editable=False,help_text='Number of share')
    status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft',help_text='Status on the blog post')

    def update_comments_count(self):
        self.comments_count = self.comments.count()
        self.save()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


    def __str__(self):
        return self.title


class Comment(models.Model):
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=100,help_text='Name of the comment')
    email = models.EmailField(help_text='Email of the comment')
    message = HTMLField(help_text='Message of the comment')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.name} on {self.blog.title}"

@receiver(post_save, sender=Comment)
@receiver(post_delete, sender=Comment)
def update_blog_comments_count(sender, instance, **kwargs):
    blog = instance.blog
    blog.comments_count = blog.comments.count()
    blog.save()