from django.shortcuts import render, redirect
from .forms import ContactForms


def contact_views(request):
    form = ContactForms(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('.')
    context = {
        'form': form
    }
    return render(request, 'pages/contacts.html', context)

