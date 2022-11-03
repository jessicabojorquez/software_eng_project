import os
import argparse

import sys
from pathlib import Path
sys.path.append(str(Path(sys.argv[0]).absolute().parent.parent))

from CnnVisualizer.core.vis import Visualizer



def main(args):

    net_soucre = os.path.join('tests','test01','source','Net.py')
    net_ckpt = os.path.join('tests', 'test01', 'source', 'net.pth')
    input_path = ''
    a = Visualizer(net_soucre,net_ckpt,input_path)
    a.vis()


    return











if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    args = parser.parse_args()
    main(args)