from django.shortcuts import render

def index(request):
    return render(request, 'info/index.html')

def intro(request):
    return render(request, 'info/intro.html')