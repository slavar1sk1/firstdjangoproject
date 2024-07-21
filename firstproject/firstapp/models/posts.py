from django.db import models
from . import User, TimeControlModel


__all__ = ('Post', )


class Post(TimeControlModel):
    text = models.TextField()
    likes_count = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)