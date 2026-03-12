from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify
from tinymce.models import HTMLField

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(unique=True, max_length=100)

    REQUIRED_FIELDS = ['username']
    USERNAME_FIELD = 'email'

class AboutMe(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    about_me = HTMLField(null=True, blank=True, help_text='Write something about yourself')
    image = models.ImageField(upload_to='about_me/image', null=True, blank=True)
    skills = models.ManyToManyField('Skills', blank=True,help_text='Add your skills')
    my_name = models.CharField(max_length=100,help_text='Enter your name')
    social_media = models.JSONField(null=True, blank=True, help_text='Add your social media links')

    def __str__(self):
        return self.my_name

class Education(models.Model):
    about_me = models.ForeignKey(AboutMe, on_delete=models.CASCADE)
    start_year = models.CharField(max_length = 4 , help_text='Start year, e.g , 2024')
    end_year = models.CharField(max_length = 4 , help_text='End year, e.g , 2025')
    degree = models.CharField(max_length = 100 , help_text='Degree, Bachelor of Science')
    university = models.CharField(max_length = 100, help_text='University of Edinburgh')
    description = HTMLField(help_text='Write something about yourself')

    def __str__(self):
        return f"{self.degree} - {self.university} ({self.start_year} - {self.end_year})"

class Experience(models.Model):
    about_me = models.ForeignKey(AboutMe, on_delete=models.CASCADE)
    start_year = models.CharField(max_length = 4 , help_text='Start year, e.g , 2024')
    end_year = models.CharField(max_length = 4 , help_text='End year, e.g , 2025')
    position = models.CharField(max_length = 100 , help_text='Position, e.g , Bachelor')
    company = models.CharField(max_length = 100 , help_text='Company')
    description = HTMLField(help_text='Write something about yourself')

    def __str__(self):
        return f"{self.position} - {self.company} ({self.start_year} - {self.end_year})"

class Skills(models.Model):
    name = models.CharField(max_length = 100, unique = True, help_text='Enter your skills')

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length = 100, help_text='Enter your project title')
    year = models.CharField(max_length = 4, help_text='Enter your project year')
    clint = models.CharField(max_length = 100, help_text='Enter your project clint')
    service = models.CharField(max_length = 100, help_text='Enter your project service')
    project_type = models.CharField(max_length = 100, help_text='Enter your project type')
    description = HTMLField(null=True,blank= True, help_text='Write something about yourself')
    slug = models.SlugField(unique=True,blank = True)
    is_active = models.BooleanField(default=False)
    create_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-id']
        verbose_name = "Project item"
        verbose_name_plural = "Project items"

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1
            while Project.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} {str(self.year)}"

class ProjectImage(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE,related_name='images')
    image = models.ImageField(upload_to = 'project/image', null=True, blank=True,help_text='upload your project image')

    def __str__(self):
        return f'Image for {self.project.title}'

class YoutubeVideo(models.Model):
    title = models.CharField(max_length = 100, help_text='Enter your video title')
    link = models.URLField(help_text='Enter your video link')
    thumbnail = models.ImageField(upload_to = 'image/youtube_thumbnail', null=True, blank=True,help_text='upload your project thumbnail')
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Resume(models.Model):
    file = models.FileField(upload_to='resume/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Resume {self.id}"