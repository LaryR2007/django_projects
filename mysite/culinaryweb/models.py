from django.db import models

class Service(models.Model):
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.text

class Detail(models.Model):
    text = models.CharField(max_length=255)
    # item_id = models.ForeignKey(Item, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.text
# Create your models here.
