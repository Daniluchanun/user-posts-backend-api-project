from django.conf import settings
from django.db import models

from core.models import BaseModel


class PostModel(BaseModel):
    class Meta:
        db_table = 'user_posts'

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=100, blank=False)
    text = models.TextField(blank=False)
