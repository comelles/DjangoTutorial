from importlib.metadata import requires
import profile
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Project
from .forms import ProjectForm



def projects(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'projects/projects.html', context)


def project(request, pk):
    projectObj = Project.objects.get(id=pk)
    return render(request, 'projects/single-project.html', {'projectObj': projectObj})

@login_required(login_url='login')
def createProject(request):
    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            proj = form.save(commit=False)
            proj.owner = request.user.profile
            proj.save()
            
            return redirect('account') 
    context = {'form' : form}
    return render(request, 'projects/project_form.html', context)

@login_required(login_url='login')
def updateProject(request, pk):                             #pasamos pk para identificar el proyecto
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    form = ProjectForm(instance=project)                    #instance para que modifique el el proyecto q queremos
    if request.method == 'POST':
        form = ProjectForm(request.POST,request.FILES, instance=project) #instance para que modifique el el proyecto q queremos
        if form.is_valid():
            form.save()
            return redirect('account') 
    context = {'form' : form}
    return render(request, 'projects/project_form.html', context)
    
@login_required(login_url='login')
def deleteProject(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('account')
    context = {'object' : project}
    return render(request, 'delete_template.html', context)

