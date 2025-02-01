from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import TodoItem
import json

def home(request):
    print('home function called')
    return render(request, 'home.html')

def todos(request):
    print('todos function called')
    items = TodoItem.objects.all()
    return render(request, 'todos.html', {'todos': items})

@csrf_exempt
def toggle_complete(request, id):
    print('toggle_complete function called with id:', id)
    if request.method == 'POST':
        try:
            todo = TodoItem.objects.get(id=id)
            todo.completed = not todo.completed
            todo.save()
            return JsonResponse({'success': True})
        except TodoItem.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Todo not found'})

@csrf_exempt
def delete_task(request, id):
    print('delete_task function called with id:', id)
    if request.method == 'POST':
        try:
            todo = TodoItem.objects.get(id=id)
            todo.delete()
            return JsonResponse({'success': True})
        except TodoItem.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Todo not found'})

@csrf_exempt
def add_task(request):
    print('add_task function called')
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            title = data.get('title')
            if title:
                todo = TodoItem.objects.create(title=title, completed=False)
                return JsonResponse({'success': True, 'id': todo.id})
            else:
                return JsonResponse({'success': False, 'error': 'Title is required'})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})