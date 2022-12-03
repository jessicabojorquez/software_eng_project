import sys

from ..utils import *
# netron.start('net.pth')

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


# os.environ["CUDA_VISIBLE_DEVICES"] = '1'


class Visualizer():
    def __init__(self, model_code, model_ckpt, input_path, output_path):
        copy2(model_code, '.')  # Bring .py file into correct directory

        # Load the model from the .pth file -- also does some error checking and handling
        # self.model = torch.load(model_ckpt, map_location=torch.device('cuda' if torch.cuda.is_available() else 'cpu'))
        try:
            self.model = torch.load(model_ckpt, map_location=torch.device('cuda' if torch.cuda.is_available() else 'cpu'))
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        except Exception as e:
            if str(e) == "Ran out of input" or str(e).find("unpickling") >= 0: # Invalid input file
                print("Invalid .pth file")
                raise ValueError("Invalid .pth file")

        self.input_tensor = load_input(input_path)
        self.input_shape = self.input_tensor.shape
        self.output_path = output_path
        return

    def get_struct(self):

        # change print to some out file
        orig_stdout = sys.stdout
        with open('model_struct.txt', 'w') as f:
            sys.stdout = f
            struct = summary(self.model, input_size=self.input_shape)
            sys.stdout = orig_stdout

        with open('model_struct.txt', 'r') as f:
            struct_info = f.readlines()

        model_content = []

        total_params = 0
        trainable_params = 0
        non_trainable_params = 0

        start = False

        for each in struct_info:
            if each.startswith("====") and start == False:
                start = True
                continue
            if start == True:
                if each.startswith("=======") or each.startswith('-----------'):
                    continue
                else:
                    if each.startswith("Total params:"):
                        info = each.replace("Total params:", '').replace(' ', '').replace('\n', '').replace(',', '')
                        total_params = int(info)
                        # print(total_params)
                    elif each.startswith("Trainable params:"):
                        info = each.replace("Trainable params:", '').replace(' ', '').replace('\n', '').replace(',', '')
                        trainable_params = int(info)
                        # print(trainable_params)
                    # start processing with conv and pooling info
                    elif each.startswith("  "):
                        temp_info = each.replace('\n', '').split(" ")
                        temp_info = [each for each in temp_info if len(each) != 0]

                        layer_type = temp_info[0].lower()[:-2]
                        if 'conv' in layer_type or 'pool' in layer_type:
                            shape_info = temp_info[1:-1]
                            temp_shape = []
                            # print(shape_info)
                            for size in shape_info:
                                # print(size)
                                size = size.replace('[', '').replace(']', '').replace(',', '')
                                size = int(size)
                                temp_shape.append(size)

                            num_param = temp_info[-1].replace('\n', '').replace(',', '')
                            num_param = int(num_param)
                            model_content.append({
                                'layer_type': layer_type,
                                'output_shape': temp_shape,
                                'num_param': num_param,
                                'output_path': ''
                            })
                        else:
                            continue
        self.model_info = {
            'info': {
                'total_params': total_params,
                'trainable_params': trainable_params,
                'non_trainable_params': total_params - trainable_params
            },
            'layer_info': model_content
        }

        return struct

    def vis(self):
        # os.makedirs('~/output')

        # Choose which layers we want to visualize heatmaps for
        all_layers = [key for key in list(dict(self.model.named_modules()).keys()) if (key != '' and 'fc' not in key)]
        # self.target_layers = [getattr(self.model,all_layers[0])]
        #
        # self.target_layers = [self.model.conv1, self.model.pool, self.model.conv2]
        layer_idx = 0
        target = []
        target_name = []
        return_files = []
        self.input_shape = self.input_tensor.squeeze(0).shape
        self.get_struct()

        num_layers = len(all_layers)
        self.model_info['info'].update({'num_layers': num_layers})
        output_content = self.model_info['layer_info']

        for layer in all_layers:
            target.append(getattr(self.model, layer))
            target_name.append(layer)
            # Create GradCAM object with layers and model specified
            cam = GradCAM(model=self.model, target_layers=target, use_cuda=True if torch.cuda.is_available() else False)
            targets = [ClassifierOutputTarget(9)]
            try:
                grayscale_cam = cam(input_tensor=self.input_tensor, targets=targets)
            except RuntimeError as e:
                if str(e).find("is invalid for input of size") >= 0:
                    print("Input Image is not the right size!")
                    raise ValueError("Input Image is not the right size!")
            grayscale_cam = grayscale_cam[0, :]

            # Get heatmap from GradCAM and manipulate it to visualize it easily
            heatmap = grayscale_cam
            input_tensor = (self.input_tensor.squeeze(0).squeeze(0)).numpy()

            input_tensor2 = np.stack([input_tensor, input_tensor, input_tensor], axis=2)
            img = input_tensor2 * 255
            heatmap = cv2.resize(heatmap, (img.shape[1], img.shape[0]))
            heatmap = np.stack([heatmap, heatmap, heatmap], axis=2)
            heatmap = np.uint8(255 * heatmap)
            heatmap = cv2.applyColorMap(heatmap, cv2.COLORMAP_JET)

            superimposed_img = heatmap * 0.5 + img * 0.5

            image_name = os.path.join("map_{:03d}.jpg".format(layer_idx + 1))
            #print(image_name)
            output_content[layer_idx]['output_path'] = image_name

            #cv2.imwrite(image_name, superimposed_img)
            temp_dict = {
                'image':superimposed_img,
                'image_name': image_name,
            }
            return_files.append(temp_dict)
            layer_idx += 1

        # print(struct_info)

        # Updated information
        self.model_info.update({'layer_info': output_content})
        # with open(os.path.join('output.json'), 'w') as f:
        #     json.dump(self.model_info, f)

        return return_files,self.model_info
