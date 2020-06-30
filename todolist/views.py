from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse,HttpResponseRedirect
from .models import Todo
from django.template import loader
from django.conf import settings
from django.contrib import messages 
from .forms import AddNotesForm
# Create your views here.
def index(request):
    #return HttpResponse("Welcome to To Do list")
    task_list = Todo.objects.all()
    #print(settings.BASE_DIR)
    return render(request, 'index.html', {'task_list': task_list})
#def add(request,todo_id):
	#return HttpResponse("Enter the new task %s" % todo_id)
 #   new_task= Todo.objects.get(pk=todo_id)
 #  return render(request, 'add.html', {'new_task': new_task})

def add(request):
    if request.method=='POST':
        form=AddNotesForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse('index'))

    else:
        form=AddNotesForm()
        return render(request, 'add.html', {'form':form})
def delete(request,todo_id):
    #return HttpResponse("Deleted the task %s" % todo_id)
    #item = Todo.objects.get(pk=todo_id) 
    #print(item)
    #item.delete() 
    #messages.info(request, "item removed !!!") 
    #return redirect('index') 
    Todo.objects.get(id=todo_id).delete()
    return HttpResponseRedirect(reverse('index'))
#def edit(request,todo_id):
#	return HttpResponse("Edit the task %s" % todo_id)

