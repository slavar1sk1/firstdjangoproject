from django.db import models


__all__ = ('TimeControlModel', )


class TimeControlModel(models.Model):
    create_at = models.DateTimeField(auto_now_add=True)
    modifided_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True