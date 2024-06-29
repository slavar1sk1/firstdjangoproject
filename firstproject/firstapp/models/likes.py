from django.db import models
from . import User, TimeControlModel, Post


__all__ = ('Like', )


class Like(TimeControlModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)