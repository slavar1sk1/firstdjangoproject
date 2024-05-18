from django.contrib.auth.models import AbstractUser
from .abstract import TimeControlModel


__all__ = ('User', )


class User(AbstractUser, TimeControlModel):
    pass