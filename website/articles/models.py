from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import uuid

# Define the Article model
class Article(models.Model):
    title = models.CharField(max_length=255)  # Field for article title
    content = models.TextField()  # Field for article content
    image = models.ImageField(upload_to='articles/article_images/', null=True, blank=True)  # Field for uploading an image
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # Author of the article
    created_at = models.DateTimeField(default=timezone.now)  # Automatically add timestamp for creation
    updated_at = models.DateTimeField(auto_now=True)  # Automatically add timestamp for updates
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)


    def __str__(self):
        return self.title

