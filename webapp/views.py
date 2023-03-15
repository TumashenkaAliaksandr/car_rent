from django.shortcuts import render

def index(request):
    return render(request, 'webapp/index.html')

def about(request):
    return render(request, 'webapp/about.html')

def contact(request):
    return render(request, 'webapp/contact.html')

def cars(request):
    return render(request, 'webapp/cars.html')

def services(request):
    return render(request, 'webapp/services.html')

def single(request):
    return render(request, 'webapp/../blog/templates/blog/single.html')

def blog(request):
    return render(request, 'webapp/../blog/templates/blog/blog.html')