from django.db import models


class Module(models.Model):
    title = models.CharField(max_length=64)
