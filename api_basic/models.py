from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_lenght = 100)
    author = models.CharField(max_lenght=100)
    email = models.EmailField(max_lenght=100)
    date = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.title

