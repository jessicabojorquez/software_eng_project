from django.http import HttpResponse
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
import random, os
from CnnVisualizer.core.vis import Visualizer
from cnn_visualizer.settings import BASE_DIR

def index_template(request):
    return render(request, 'visualizer_server/index.html')

def upload_request(request):
    model_id = "nomodel"
    if request.method == 'POST':
        uploaded_model = request.FILES['model']
        uploaded_ptn = request.FILES['pth']
        uploaded_image = request.FILES['image']
        fs = FileSystemStorage()
        model_id = "model" + str(random.randrange(10000))
        fs.save(model_id +'/' + uploaded_model.name, uploaded_model)
        fs.save(model_id +'/' + uploaded_ptn.name, uploaded_ptn)
        fs.save(model_id +'/' + uploaded_image.name, uploaded_image)
    response = HttpResponse(request)
    response['model-id'] = model_id
    return response

def run_model(request):
    if request.method == 'POST':
        model_id = request.headers['model-id']
        directory = os.path.join(BASE_DIR, 'media', model_id)
        net_source = ""
        net_ckpt = ""
        input_path =""
        for file in os.listdir(directory):
            if os.path.splitext(file)[1] == '.py':
                net_source = os.path.join(directory, file)
            elif os.path.splitext(file)[1] == '.pth':
                net_ckpt = os.path.join(directory, file)
            else:
                input_path = os.path.join(directory, file)
        os.mkdir(os.path.join(directory, 'output'))
        os.chdir(os.path.join(directory, 'output')) # change directory to process
        a = Visualizer(net_source,net_ckpt,input_path)
        a.vis()
    response = HttpResponse(request)
    response['model-id'] = model_id
    return response
    

def get_images(request):
    return HttpResponse(request)

def get_model(request):
    return HttpResponse(request)