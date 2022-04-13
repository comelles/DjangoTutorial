from importlib.metadata import requires
from django.shortcuts import render, redirect
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

def createProject(request):
    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('projects') 
    context = {'form' : form}
    return render(request, 'projects/project_form.html', context)


def updateProject(request, pk):                             #pasamos pk para identificar el proyecto
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)                    #instance para que modifique el el proyecto q queremos
    if request.method == 'POST':
        form = ProjectForm(request.POST,request.FILES, instance=project) #instance para que modifique el el proyecto q queremos
        if form.is_valid():
            form.save()
            return redirect('projects') 
    context = {'form' : form}
    return render(request, 'projects/project_form.html', context)

def deleteProject(request, pk):
    project = Project.objects.get(id=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('projects')
    context = {'object' : project}
    return render(request, 'projects/delete_template.html', context)

