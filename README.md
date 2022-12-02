# CS 130 Project: See-NN
This is the official repo for CS 130 Team B6.

![avatar](./imgs/logo.jpeg)

The goal of this project is to develop a tool that can automatically generate visual representations of layers in a model and illustrate how layers are connected.

## Introduction
Our website will allow users to upload their trained models and view both interactable graphs representing model structure and learned filters or layers inside the "black box". Users would also be able to adjust or selectively include or exclude different filters. This would help improve speed and effectiveness on final model for the user, since users can decide if they should disregard parameters that are less influential in the classification of images.
## Code Overview
* ./
* ./
* ./ml_code: Our main model to generate heatmaps for CNN.
  
(please fill the missing part)

## Installation
Our installation instructions require conda to install python packages. Using the follwing command to set up the environment for out project.
```shell
conda create -n see_nn python==3.8
conda activate see_nn
conda install pytorch torchvision torchaudio -c pytorch
pip install opencv-python
pip install grad-cam
pip install torchsummary
cd ml_code/vis_local
python setup.py install
cd ../..
```
## Quick Start
Using the following command to run backend and frontent.
```shell
fill the command here to run both front end and backend.
```


## Contact
* Jessica Bojorquez (email)
* Rishi Upadhyay ()
* Sicheng Mo (smo3@ucla.edu)
* Liyang Huang ()
* Deven Douglas ()

