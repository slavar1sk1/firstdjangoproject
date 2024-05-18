from django.db import models
from . import User, TimeControlModel


__all__ = ('Post', )


class Post(TimeControlModel):
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)