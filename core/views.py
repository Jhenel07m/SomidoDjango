from django.shortcuts import render

def home(request):
    return render(request, 'core/home.html', {'project_jhenel': 'Somido Django Project'})