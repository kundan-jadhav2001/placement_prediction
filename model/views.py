from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "index1.html")

def signinup(request):
    return render(request, "index.html")

def contact(request):
    return render(request, "index1.html")

def about(request):
    return render(request, "about.html")

def blog(request):
    return render(request, "blog.html")

def course(request):
    return render(request, "course.html")