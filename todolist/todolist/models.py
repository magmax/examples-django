from django.db import models
import datetime


class Task(models.Model):
    created = models.DateField(default=datetime.date.today)
    title = models.CharField(max_length=50)
    description = models.TextField()
    duedate = models.DateField(blank=True, null=True)
    finished = models.DateField(blank=True, null=True)

    def __str__(self):
        if self.finished:
            return '{0} (finished)'.format(self.title)
        return self.title
