from django.http import HttpResponse
from django.shortcuts import render

def index_template(request):
    return render(request, 'visualizer_server/index.html')

def upload(request):
    if request.method == 'POST':
        print(request.headers)
        return HttpResponse(request)