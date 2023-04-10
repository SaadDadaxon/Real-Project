from django.shortcuts import render, redirect
from contact.forms import ContactForms


def index(request):
    form = ContactForms(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('.')
    context = {
        'form': form
    }
    return render(request, 'pages/index.html', context)


def investor(request):
    form = ContactForms(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('.')
    context = {
        'form': form
    }
    return render(request, 'pages/forInvestors.html', context)


def project_views(request):
    return render(request, 'pages/ourProjects.html')


def service_views(request):
    return render(request, 'pages/service.html')


def solution_views(request):
    return render(request, 'pages/solution.html')




