import os
import argparse

import sys
from pathlib import Path
sys.path.append(str(Path(sys.argv[0]).absolute().parent.parent))

from CnnVisualizer.core.vis import Visualizer



def main(args):
    assert test_01()
    assert test_02()
    assert test_03()
    assert test_04()
    assert test_05()
    assert test_06()
    return

def test_01(): # Test where the model successfully predicts the class

    net_soucre = os.path.join('tests','test01','source','Net.py')
    net_ckpt = os.path.join('tests', 'test01', 'source', 'net.pth')
    input_path = os.path.join('tests', 'test01', 'source', 'img.jpg')
    a = Visualizer(net_soucre,net_ckpt,input_path,'')
    a.vis()
    return True

def test_02(): # Test where the model is not able to predict the class
    net_soucre = os.path.join('tests','test01','source','Net.py')
    net_ckpt = os.path.join('tests', 'test01', 'source', 'net.pth')
    input_path = os.path.join('tests', 'test02', 'source', 'img.jpg')
    a = Visualizer(net_soucre,net_ckpt,input_path,'')
    a.vis()
    return True

def test_03(): # test where input image and net don't match
    net_source = os.path.join('tests','test03','source','Net.py')
    net_ckpt = os.path.join('tests', 'test03', 'source', 'net.pth')
    input_path = os.path.join('tests', 'test03', 'source', 'img.jpg')
    try:
        a = Visualizer(net_source, net_ckpt, input_path,'')
        a.vis()
    except ValueError:
        return True #This didn't work -- as expected
    return False

def test_04(): # test where the .pth file is invalid
    net_source = os.path.join('tests','test04','source','Net.py')
    net_ckpt = os.path.join('tests', 'test04', 'source', 'net.pth')
    input_path = os.path.join('tests', 'test04', 'source', 'img.jpg')
    try:
        a = Visualizer(net_source, net_ckpt, input_path,'')
        a.vis()
    except ValueError:
        return True # This didn't work as expected
    return False
def test_05(): # Test where the model with 3 layer input
    net_soucre = os.path.join('tests','test05','source','Net.py')
    net_ckpt = os.path.join('tests', 'test05', 'source', 'model.pth')
    input_path = os.path.join('tests', 'test05', 'source', 'img0.jpg')
    a = Visualizer(net_soucre,net_ckpt,input_path,'')
    a.vis()
    return True

def test_05(): # Test where the model with 3 layer input and fails
    net_soucre = os.path.join('tests','test06','source','Net.py')
    net_ckpt = os.path.join('tests', 'test06', 'source', 'model.pth')
    input_path = os.path.join('tests', 'test06', 'source', 'img2.jpg')
    a = Visualizer(net_soucre,net_ckpt,input_path,'')
    a.vis()
    return True


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    args = parser.parse_args()
    main(args)