from django.shortcuts import render  # check what is render
from django.http import HttpResponse

# Create your views here.
def hello(request):
    return render(request, 'Hokage/hello.html')
