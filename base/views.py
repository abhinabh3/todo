from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Todo
import csv

# Create your views here.
def home(request):
    todo_obj = Todo.objects.all()
    data = {'todos': todo_obj}
    return render(request, 'index.html',context=data)

def create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        status = request.POST.get('status')
        Todo.objects.create(name=name, description=description, staus=status)

        return redirect('home')
    return render(request, 'create.html')

def edit(request,pk):
    todo_obj = Todo.objects.get(id = pk)
    if request.method == "POST":
        name = request.POST.get('name')
        description = request.POST.get('description')
        status = request.POST.get('status')
        todo_obj.name = name
        todo_obj.description = description
        todo_obj.staus = status
        todo_obj.save()
        return redirect('home')
    return render(request, 'edit.html', context={'todo':todo_obj})

def delete(request,pk):
    todo_obj = Todo.objects.get(id=pk)
    todo_obj.delete()
    return redirect('home')

def deleteall(request):
    todo_obj = Todo.objects.all()
    todo_obj.delete()
    return redirect('home')

def export_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="todo.csv"'
    writer = csv.writer(response)
    writer.writerow(['Name', 'Description', 'Status'])
    todo_obj = Todo.objects.all()
    for todo in todo_obj:
        writer.writerow([todo.name, todo.description, todo.staus])
    return response
