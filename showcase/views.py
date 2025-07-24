from django.shortcuts import render

def home(request):
    return render(request, 'showcase/home.html')

def features(request):
    return render(request, 'showcase/features.html')

def demo(request):
    return render(request, 'showcase/demo.html')

def about(request):
    return render(request, 'showcase/about.html')
