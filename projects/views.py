from collections import defaultdict
from django.db.models import Sum, Avg
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from designers.models import Designer
from .forms import ProjectForm
from .models import Project, ConstructionType


class ProjectListView(ListView):
    model = Project
    template_name = 'projects/project_list.html'
    context_object_name = 'projects'
    ordering = ['-built_in', 'name']


class ProjectDetailView(DetailView):
    model = Project
    template_name = 'projects/project_detail.html'
    context_object_name = 'project'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'


class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectForm
    template_name = 'projects/project_form.html'
    success_url = reverse_lazy('project_list')


class ProjectUpdateView(UpdateView):
    model = Project
    form_class = ProjectForm
    template_name = 'projects/project_form.html'
    success_url = reverse_lazy('project_list')


class ProjectDeleteView(DeleteView):
    model = Project
    template_name = 'projects/project_confirm_delete.html'
    success_url = reverse_lazy('project_list')


class DesignerListView(ListView):
    model = Designer
    template_name = 'designers/designer_list.html'
    context_object_name = 'designers'
    ordering = ['full_name']


def project_stats(request: HttpRequest) -> HttpResponse:
    total_projects = Project.objects.count()
    total_value = Project.objects.filter(contract_value__isnull=False, contract_value_confidential=False).aggregate(total=Sum('contract_value'))['total'] or 0
    average_value = Project.objects.filter(contract_value__isnull=False, contract_value_confidential=False).aggregate(avg=Avg('contract_value'))['avg'] or 0

    context = {
        'total_projects': total_projects,
        'total_value': total_value,
        'average_value': average_value,
    }
    return render(request, 'projects/project_stats.html', context)


def projects_by_year(request):
    projects = Project.objects.order_by('-built_in', 'name')
    projects_by_year_dict = defaultdict(list)
    for project in projects:
        year = project.built_in
        if year:
            projects_by_year_dict[year].append(project)

    context = {
        'projects_by_year': dict(projects_by_year_dict),
    }
    return render(request, 'projects/projects_by_year.html', context)


def projects_by_type(request):
    from django.db.models import Prefetch
    construction_types = ConstructionType.objects.prefetch_related(
        Prefetch('projects', queryset=Project.objects.order_by('-built_in'))
    ).all()

    context = {
        'construction_types': construction_types,
    }
    return render(request, 'projects/projects_by_type.html', context)


def projects_by_designer(request: HttpRequest, designer_id: int) -> HttpResponse:
    designer = get_object_or_404(Designer, id=designer_id)
    projects = Project.objects.filter(participations__designer=designer).order_by('-built_in')
    context = {'projects': projects, 'designer': designer}
    return render(request, 'projects/projects_by_designer.html', context)

