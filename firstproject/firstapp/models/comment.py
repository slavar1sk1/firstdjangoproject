from django.db import models
from . import User, TimeControlModel, Post


__all__ = ('Comment', )


class Comment(TimeControlModel):
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)


    def __str__(self):
        return f'{self.user.username} - {self.text[:20]}'