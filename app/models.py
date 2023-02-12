from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=90)
    created_at = models.DateTimeField(null=True)
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name


class App(models.Model):
    name = models.CharField('name', max_length=90)
    description = models.TextField('description')
    size = models.PositiveSmallIntegerField(null=False)
    installers = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(null=True)
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    url = models.SlugField(max_length=160, unique=True)
    poster = models.FileField(upload_to="app_poster/", null=True)
    # god creating
    # ganre
    # vozrast
    # country
    # author
    # deleted
    # version
    # programming languages
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("app_show", kwargs={"slug": self.url})


class AppImage(models.Model):
    app = models.ForeignKey(App, null=False, on_delete=models.CASCADE)
    image = models.FileField(upload_to='app_image/', null=False)
    created_at = models.DateTimeField(null=True)


class Rating(models.Model):
    app = models.ForeignKey(App, default=0, on_delete=models.CASCADE)
    star = models.PositiveSmallIntegerField(default=0)
    message = models.CharField(max_length=240, null=True, blank=True)
    author = models.CharField(max_length=180)


