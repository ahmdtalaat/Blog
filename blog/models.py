from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, unique=True)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        slug = slugify(self.title)
        if self.slug != slug:
            self.slug = slug
        super(Post, self).save(*args, **kwargs)

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('blog:post_detail', kwargs={'slug': self.slug})
