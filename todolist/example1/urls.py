from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from django.views.generic import ListView

from todolist import models, views

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', ListView.as_view(
        queryset=models.Task.objects.all(),
        template_name='task_list.html',
        context_object_name='tasks',
        paginate_by=5,
    ), name='task_list'),

    url(r'^task/create/?$', views.CreateTask.as_view(
    ), name='task_create'),

    url(r'^task/(?P<pk>\d+)/update/?$', views.UpdateTask.as_view(
    ), name='task_update'),

    url(r'^task/(?P<pk>\d+)/delete/?$', views.DeleteTask.as_view(
    ), name='task_delete'),
)
