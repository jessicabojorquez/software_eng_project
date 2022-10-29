from django.shortcuts import render

def index_template(request):
    return render(request, 'visualizer_server/index.html')