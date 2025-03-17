from django.db import models

class Candy(models.Model):
     name = models.CharField(max_length=255, unique=True)

     def __str__(self):
        return self.name
     
class Color(models.Model):
    name = models.CharField(max_length=50, unique=True)  # e.g., Red, Blue, Green

    def __str__(self):
        return self.name
     
class CandyDescription(models.Model):
    candy = models.ForeignKey(Candy, on_delete=models.CASCADE, related_name="descriptions")
    ingredients = models.TextField()
    flavor = models.CharField(max_length=255)
    colors = models.ManyToManyField(Color, related_name='candies')  # Many-to-Many Relationship

    def __str__(self):
        return f"{self.candy.name} - {self.flavor}"


# Create your models here.
