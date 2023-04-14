from datetime import datetime

from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import ListView, DetailView
from .models import Task, Tag


class TagListView(generic.ListView):
    model = Tag
    context_object_name = "tags"
    template_name = 'todolist/tag_list.html'
    paginate_by = 5


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todolist:tag-list")


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    template_name = "todolist/tag_form.html"
    success_url = reverse_lazy("todolist:index")


class TagDeleteView(generic.DeleteView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todolist:tag-list")


class TagDetailView(generic.DetailView):
    model = Tag
    context_object_name = "tag"
    template_name = "todolist/tag_detail.html"
    success_url = reverse_lazy("todolist:tag-list")


#
# class TaskListView(generic.ListView):
#     model = Task
#     template_name = 'todolist/task_list.html'
#     context_object_name = 'tasks'
#
#     def get_queryset(self):
#         queryset = super().get_queryset()
#         return queryset.order_by('-done', '-datetime_created')
#
class TaskListView(generic.ListView):
    model = Task
    template_name = 'todolist/task_list.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        return Task.objects.order_by('done', '-datetime_created')


'''toggle "Complete"/"Undo"  button  '''
class TaskToggleView(generic.View):
    def post(self, request, **kwargs):
        task = get_object_or_404(Task, pk=kwargs['pk'])
        task.done = not task.done
        task.save()
        return redirect('todolist:task-list')


class TaskCreateView(generic.CreateView):
    model = Task
    fields = ['content', 'deadline', 'tags']
    success_url = reverse_lazy("todolist:task-list")

    def form_valid(self, form):
        form.instance.datetime_created = datetime.now()
        return super().form_valid(form)


class TaskUpdateView(generic.UpdateView):
    model = Task
    fields = ['content', 'deadline', 'tags']
    success_url = reverse_lazy("todolist:task-list")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("todolist:task-list")


# class TaskDetailView(generic.DetailView):
#     model = Task
#     context_object_name = "task"
#     template_name = "todolist/task_detail.html"
#     success_url = reverse_lazy("todolist:task-list")

class TaskCompleteView(generic.UpdateView):
    model = Task
    fields = ['done']
    success_url = reverse_lazy("todolist:task-list")

    def get_object(self):
        task = super().get_object()
        task.done = True
        task.save()
        return task


class TaskUndoView(generic.UpdateView):
    model = Task
    fields = ['done']
    success_url = reverse_lazy("todolist:task-list")
