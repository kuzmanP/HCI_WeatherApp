from django.db import models

# from datetime import datetime

# # Create your models here.

# class Todo(models.Model):
#     Activity_name = models.CharField(max_length=1000)
#     details = models.CharField(max_length=10000)
#     date = models.DateTimeField(default=datetime.now)
    
# class Snippet(models.Model):
#     name = models.CharField(max_length=100)
#     body = models.TextField(max_length=100000)
                

    
class SearchHistory(models.Model):
    city = models.CharField(max_length=255)
    search_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.city
