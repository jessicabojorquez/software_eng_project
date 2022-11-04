from ..utils import *
#netron.start('net.pth')

from torchsummary import summary
import torch
import os
import numpy as np
import cv2
from pytorch_grad_cam import GradCAM, HiResCAM, ScoreCAM, GradCAMPlusPlus, AblationCAM, XGradCAM, EigenCAM, FullGrad
from pytorch_grad_cam.utils.model_targets import ClassifierOutputTarget
from torchvision import datasets, transforms
from pytorch_grad_cam.utils.image import show_cam_on_image
import matplotlib.pyplot as plt
#os.environ["CUDA_VISIBLE_DEVICES"] = '1'

def nothing():
    input_shape = (1, 28, 28)
    model = torch.load('net.pth', map_location=torch.device('cuda' if torch.cuda.is_available() else 'cpu'))
    train_ds = datasets.MNIST('./data', train=True, download=True,
                              transform=transforms.Compose([transforms.ToTensor()]))

    str1 = summary(model, input_size=input_shape)
    # inputs = torch.zeros(input_shape)
    # with SummaryWriter() as writer:
    #     writer.add_graph(model=model.cpu(),input_to_model=inputs,verbose=False)
    print(model.state_dict().keys())

    target_layers = [model.conv1, model.pool, model.conv2]
    print(target_layers)

    cam = GradCAM(model=model, target_layers=target_layers, use_cuda=True)
    targets = [ClassifierOutputTarget(9)]

    input_tensor = train_ds[100][0].unsqueeze(0)
    print(input_tensor.shape)
    # You can also pass aug_smooth=True and eigen_smooth=True, to apply smoothing.
    grayscale_cam = cam(input_tensor=input_tensor, targets=targets)

    # In this example grayscale_cam has only one image in the batch:
    grayscale_cam = grayscale_cam[0, :]
    print(grayscale_cam.shape)
    print(grayscale_cam.dtype)
    # grayscale_cam = grayscale_cam*255
    # grayscale_cam = grayscale_cam.astype(np.uint8)
    print(grayscale_cam.dtype)
    print(grayscale_cam)
    # cv2.imshow('image',grayscale_cam)
    # cv2.waitKey(0)

    # plt.imshow(grayscale_cam)
    # plt.show()

    heatmap = grayscale_cam
    input_tensor = (input_tensor.squeeze(0).squeeze(0)).numpy()
    input_tensor = np.stack([input_tensor, input_tensor, input_tensor], axis=2)
    # img = cv2.imread('./data/Elephant/data/05fig34.jpg')
    img = input_tensor * 255
    # plt.imshow(img)
    # plt.show()
    heatmap = cv2.resize(heatmap, (img.shape[1], img.shape[0]))
    heatmap = np.uint8(255 * heatmap)
    heatmap = cv2.applyColorMap(heatmap, cv2.COLORMAP_JET)
    superimposed_img = heatmap * 0.5 + img * 0.5
    cv2.imwrite('./map.jpg', superimposed_img)


class Visualizer():
    def __init__(self,model_code,model_ckpt,input_path):
        copy2(model_code,'.')

        try:
            self.model = torch.load(model_ckpt, map_location=torch.device('cuda' if torch.cuda.is_available() else 'cpu'))
        except Exception as e:
            if str(e) == "Ran out of input" or str(e).find("unpickling") >= 0: # Invalid input file
                print("Invalid .pth file")
                raise ValueError("Invalid .pth file")

        self.input_tensor = load_input(input_path)
        self.input_shape = self.input_tensor.shape

        return

    def get_struct(self):
        struct = summary(self.model, input_size=self.input_shape)
        return struct







    def vis(self):

        all_layers = [key for key in list(dict(self.model.named_modules()).keys()) if (key != '' and 'fc' not in key)]
        self.target_layers = [getattr(self.model,all_layers[0])]

        self.target_layers = [self.model.conv1, self.model.pool, self.model.conv2]

        cam = GradCAM(model=self.model, target_layers=self.target_layers, use_cuda=True if torch.cuda.is_available() else False)
        targets = [ClassifierOutputTarget(9)]
        try:
            grayscale_cam = cam(input_tensor=self.input_tensor, targets=targets)
        except RuntimeError as e:
            if str(e).find("is invalid for input of size") >= 0:
                print("Input Image is not the right size!")
                raise ValueError("Input Image is not the right size!")
        grayscale_cam = grayscale_cam[0, :]
        heatmap = grayscale_cam
        input_tensor = (self.input_tensor.squeeze(0).squeeze(0)).numpy()
        input_tensor = np.stack([input_tensor, input_tensor, input_tensor], axis=2)
        img = input_tensor * 255
        heatmap = cv2.resize(heatmap, (img.shape[1], img.shape[0]))
        heatmap = np.stack([heatmap,heatmap,heatmap],axis=2)
        heatmap = np.uint8(255 * heatmap)
        heatmap = cv2.applyColorMap(heatmap, cv2.COLORMAP_JET)


        superimposed_img = heatmap * 0.5 + img * 0.5
        cv2.imwrite('./map.jpg', superimposed_img)

        return
