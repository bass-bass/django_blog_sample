from django.db import models
from django.utils import timezone
from mdeditor.fields import MDTextField
# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self): 
        return self.name 

class Contact(models.Model):
    name = models.CharField(max_length=100)
    mail = models.EmailField()
    content = models.TextField()

    def __str__(self):
        return self.name

class Post(models.Model):
    tags = models.ManyToManyField(Tag, blank=True)
    title = models.CharField(max_length=150)
    content = MDTextField()
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='media/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True) 
    published_at = models.DateTimeField(blank=True, null=True) 
    is_public = models.BooleanField(default=False) 

    class Meta:
        ordering = ["-created_at"] #作成日時の降順で表示

    def save(self, *args, **kwargs):
        if self.is_public and not self.published_at:
            self.published_at = timezone.now()
        super().save(*args, **kwargs) #はじめて記事公開のとき現在の日時を保存

    def __str__(self):
        return self.title

class ContentImage(models.Model):
    post = models.ForeignKey(Post, on_delete=models.PROTECT)
    content_image = models.ImageField(upload_to='post_content_images/')

class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=50)
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['-timestamp']

    def approve(self):
        self.approved = True
        self.save()

    def __str__(self):
        return self.text

class Reply(models.Model):
    comment = models.ForeignKey(
        Comment, on_delete=models.CASCADE, related_name='replies')
    author = models.CharField(max_length=50)
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    def approve(self):
        self.approved = True
        self.save()

    def __str__(self):
        return self.text