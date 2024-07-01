from django.shortcuts import render, get_object_or_404, redirect
from .models import Task
from .forms import TaskForm
from django.http import HttpResponse
# Главная страница со списком задач
def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'task_list.html', {'tasks': tasks})

# Страница для создания новой задачи
def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'task_form.html', {'form': form})

# Страница для редактирования существующей задачи
def task_edit(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'task_form.html', {'form': form})

# Страница для удаления задачи
def task_delete(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'task_confirm_delete.html', {'task': task})

# Страница для просмотра деталей задачи
def task_detail(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    return render(request, 'task_detail.html', {'task': task})

# Страница для изменения статуса задачи
def task_status(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.completed = not task.completed
    task.save()
    return redirect('task_list')

# Представление для поиска задач
def task_search(request):
    query = request.GET.get('q')
    if query:
        tasks = Task.objects.filter(title__icontains=query)
    else:
        tasks = Task.objects.all()
    return render(request, 'task_list.html', {'tasks': tasks, 'query': query})
# Представление для фильтрации задач
def task_filter(request, filter_type):
    if filter_type == 'completed':
        tasks = Task.objects.filter(completed=True)
    elif filter_type == 'pending':
        tasks = Task.objects.filter(completed=False)
    else:
        tasks = Task.objects.all()
    return render(request, 'task_list.html', {'tasks': tasks, 'filter_type': filter_type})
# Представление для экспорта задач
def task_export(request):
    # Ваш код для экспорта задач
    return HttpResponse("Экспорт задач")
def task_import(request):
    # Ваш код для импорта задач
    return HttpResponse("Импорт задач")



