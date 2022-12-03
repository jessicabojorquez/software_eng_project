import json

from django.http import HttpResponse
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
import random, os
from CnnVisualizer.core.vis import Visualizer
from cnn_visualizer.settings import BASE_DIR
from django.views.decorators.csrf import csrf_exempt
import cv2

def index_template(request):
    return render(request, 'visualizer_server/index.html')

@csrf_exempt
def upload_request(request):
    model_id = "nomodel"
    fs = ''
    if request.method == 'POST':
        uploaded_model = request.FILES['model']
        uploaded_ptn = request.FILES['pth']
        uploaded_image = request.FILES['image']
        fs = FileSystemStorage()
        model_id = "model" + str(random.randrange(10000))
        fs.save(model_id +'/' + uploaded_model.name, uploaded_model)
        fs.save(model_id +'/' + uploaded_ptn.name, uploaded_ptn)
        fs.save(model_id +'/' + uploaded_image.name, uploaded_image)
    response = HttpResponse(model_id)
    run_model(model_id)
    return response

def run_model(model_id):
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
    print(net_ckpt)
    print(net_source)
    print(input_path)
    os.mkdir(os.path.join(directory, 'output'))
    a = Visualizer(net_source,net_ckpt,input_path,os.path.join(directory, 'output'))
    #os.chdir(os.path.join(directory, 'output')) # change directory to process
    return_files,model_info = a.vis()
    for file in return_files:
        output_path = os.path.join(directory,'output',file['image_name'])
        cv2.imwrite(output_path,file['image'])
    with open(os.path.join(directory,'output','output.json'),'w') as f:
        json.dump(model_info,f)


def get_images(request):
    return HttpResponse(request)

def get_model(request):
    return HttpResponse(request)

def auth(request):
    response = HttpResponse(request)
    response['Access-Control-Allow-Credentials'] = True
    return response