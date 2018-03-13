from django.shortcuts import render


def dashboard(request):
    return render(request, 'analytics_home.html', {})
