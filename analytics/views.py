from django.shortcuts import render

def home(request):
    return render(request, 'analytics_home.html', {})
