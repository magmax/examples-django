from django.shortcuts import render
from django.views.generic import edit
from django.core.urlresolvers import reverse

from models import Task


class CreateTask(edit.CreateView):
    model = Task

    def get_success_url(self):
        return reverse('task_list')


class UpdateTask(edit.UpdateView):
    model = Task

    def get_success_url(self):
        return reverse('task_list')

class DeleteTask(edit.DeleteView):
    model = Task

    def get_success_url(self):
        return reverse('task_list')

