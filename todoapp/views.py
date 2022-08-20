from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Task
from . form import Todoforms
from django . views.generic import ListView
from django . views.generic.detail import DetailView
from django . views.generic.edit import UpdateView,DeleteView
from django . urls import reverse_lazy

# Create your views here.

# ----------------------class based or generic base (less code )-----------------
class TaskListView(ListView):
    model= Task
    template_name= 'task_home.html'
    context_object_name = 'obj1'

class TaskDetailView(DetailView):
    model = Task
    template_name = 'detail.html'
    context_object_name = 'i'

class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'update1.html'
    context_object_name = 'task'
    fields = ('name','priority','date')
    def get_success_url(self):
        return  reverse_lazy('cbvdetail',kwargs={'pk':self.object.id})





class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('cbvtask')



#-------------------------function based (more codes)---------------------

def task_home(request):
    obj1=Task.objects.all()
    if request.method=='POST':
        name=request.POST.get('name')
        priority=request.POST.get('priority')
        date=request.POST.get('date')

        obj=Task(name=name,priority=priority,date=date)
        obj.save()

    return render(request,'task_home.html',{'obj1':obj1})


def delete(request,taskid):
    task=Task.objects.get(id=taskid)
    if request.method=='POST':
        task.delete()
        return redirect('/')
    return render(request,'delete.html',{'task':task})

def update(request,id):
    task=Task.objects.get(id=id)
    form=Todoforms(request.POST or None,instance=task)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'update.html',{'task':task,'form':form})



# def task(request):
#     if request.method=='POST':
#         name=request.POST.get('name')
#         priority=request.POST.get('priority')
#         obj=Task(name=name,priority=priority)
#         obj.save()
#     return render(request,"task.html")       #for view in one page
