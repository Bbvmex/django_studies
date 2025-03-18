from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def toggle_completed(self):
        self.completed = not self.completed
        self.save()

    def __str__(self):
        return self.title
