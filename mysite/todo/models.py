from django.db import models

class ToDo(models.Model):
    description = models.CharField(max_length=80)
    due = models.DateField()

    def get_absolute_url(self):
        return "/todo/items"

    # Create your models here.
