import os
import shutil

from torchvision import datasets, transforms

def copy2(src,dst):
    shutil.copy2(src,dst)

def load_input(input_path):
    try:
        train_ds = datasets.MNIST('./data', train=True, download=True,
                                  transform=transforms.Compose([transforms.ToTensor()]))
        input_tensor = train_ds[1114][0].unsqueeze(0)
        return input_tensor
    except:
        return
