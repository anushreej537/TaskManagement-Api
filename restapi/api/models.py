from django.db import models

class Task(models.Model):
    task_name = models.CharField(max_length = 250)
    description = models.CharField(max_length = 300)
    def __str__(self):
        return self.task_name
