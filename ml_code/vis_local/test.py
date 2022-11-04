import os
import argparse

import sys
from pathlib import Path
sys.path.append(str(Path(sys.argv[0]).absolute().parent.parent))

from CnnVisualizer.core.vis import Visualizer



def main(args):
    assert test_01()
    assert test_02()
    return



def test_01():

    net_soucre = os.path.join('tests','test01','source','Net.py')
    net_ckpt = os.path.join('tests', 'test01', 'source', 'net.pth')
    input_path = os.path.join('tests', 'test01', 'source', 'img.jpg')
    a = Visualizer(net_soucre,net_ckpt,input_path)
    a.vis()
    return True

def test_02():
    net_soucre = os.path.join('tests','test01','source','Net.py')
    net_ckpt = os.path.join('tests', 'test01', 'source', 'net.pth')
    input_path = os.path.join('tests', 'test02', 'source', 'img.jpg')
    a = Visualizer(net_soucre,net_ckpt,input_path)
    a.vis()
    return True





if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    args = parser.parse_args()
    main(args)