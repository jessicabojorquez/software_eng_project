import json
import os
import shutil

from torchvision import datasets, transforms
from torch.utils.data import Dataset
import cv2


class OneImageDataset(Dataset):
    def __init__(self,input_path,transform=None):
        self.input_path = [input_path]
        self.transform = transform


    def __len__(self):
        return 1

    def __getitem__(self, idx):
        path = self.input_path[idx]
        img = cv2.imread(path,cv2.IMREAD_UNCHANGED)

        if self.transform:
            img = self.transform(img)

        return img


def copy2(src,dst):
    shutil.copy2(src,dst)

def load_input(input_path):
    try:
        # read image
        #img = cv2.imread(input_path)

        img = cv2.imread(input_path, cv2.IMREAD_UNCHANGED)
        dims = img.shape
        if len(dims) ==3  and dims[-1] ==3:
            img_transforms = transforms.Compose([transforms.ToTensor(),transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])
        else:
            img_transforms = transforms.Compose([transforms.ToTensor()])
        dataset = OneImageDataset(input_path,transform=img_transforms)
        image = dataset[0]
        #print('1')

        return image.unsqueeze(0)

    except:
        # load any image from
        train_ds = datasets.MNIST('./data', train=True, download=True,
                                  transform=transforms.Compose([transforms.ToTensor()]))
        input_tensor = train_ds[1114][0].unsqueeze(0)
        return input_tensor


def write_json(content,path):
    with open(path,'w')  as f:
        json.dump(content,f)

