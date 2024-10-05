from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.utils import timezone
from django.contrib.auth.decorators import login_required

def data(request):
    return render(request, 'data.html')

def test(request):
    return render(request, 'test.html')

def data(request):
    return render(request, 'data.html', {'message': 'Это страница данных'})

def test(request):
    return render(request, 'test.html')