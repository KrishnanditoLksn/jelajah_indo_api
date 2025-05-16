from django.db import models


class Travel(models.Model):
    description = models.CharField(max_length=255)
