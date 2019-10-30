from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404

def melong(request):
    return render(request, 'melong.html')

def marker(request):
    return render(request, 'marker.html')

