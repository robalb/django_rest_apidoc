from django.db import models


LANGUAGE_CHOICES = [
  ("python", "python"),
  ("not_python", "not python"),
  ("not_not_python", "not python (php)"),
]

class Guestnote(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    note = models.TextField()
    like_tiangolo = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)

    class Meta:
        ordering = ['created']
