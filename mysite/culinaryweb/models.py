from django.db import models

class Service(models.Model):
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.text

class Detail(models.Model):
    service_id = models.ForeignKey(Service, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    
    def __str__(self):
        return self.text
# Create your models here.ç
