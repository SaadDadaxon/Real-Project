from django.shortcuts import render


def about_views(request):
    return render(request, 'pages/aboutUs.html')
