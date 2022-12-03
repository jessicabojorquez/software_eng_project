import json
import os
import shutil

from torchvision import datasets, transforms
from torch.utils.data import Dataset
import cv2


class OneImageDataset(Dataset):
    """OneImageDataset: A pytorch dataset that returns only 1 image. Used for testing

    :param input_path: the filename of the one image
    :type input_path: str
    :param transform: transform to be applied to the image before returning
    :type transform: torchvision.transform, optional
    
    """
    def __init__(self,input_path,transform=None):
        """
        Constructor
        """
        self.input_path = [input_path]
        self.transform = transform


    def __len__(self):
        """Returns the length of this dataset. In this case always 1
        """
        return 1

    def __getitem__(self, idx):
        """Returns a single item identified by idx
    
        :param idx: the index of the item to retrieve
        :type idx: int
        """
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
        dataset = OneImageDataset(input_path,transform=transforms.Compose([transforms.ToTensor()]))
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

