# CS 130 Project: See-NN
This is the official repo for CS 130 Team B6.

![avatar](./imgs/logo.jpeg)

The goal of this project is to develop a tool that can automatically generate visual representations of layers in a model and illustrate how layers are connected.

## Introduction
Our website will allow users to upload their trained models and view both interactable graphs representing model structure and learned filters or layers inside the "black box". Users would also be able to adjust or selectively include or exclude different filters. This would help improve speed and effectiveness on final model for the user, since users can decide if they should disregard parameters that are less influential in the classification of images.
## Code Overview
* ./client: our front-end code which holds all the information pertaining to the webpages, as well as the API used to call the backend
* ./
* ./ml_code: Our main model to generate heatmaps for CNN.
  
(please fill the missing part)

## Installation
Our installation instructions require conda to install python packages. Execute the following commands to set up the environment for our project:
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

In addition, our server utilizes Django. To install, execute the following commands in your conda environment:
```shell
pip install Django
pip install django-cors-headers
``` 

To set up the client, in the client folder execute:
```shell
npm install
```

## Quick Start

In the client folder, execute: 
```shell
npm run serve
```
to start the frontend.

In the server folder, execute: 
```shell
python manage.py runserver
```
to start the backend.

Once both are running, navigate to http://localhost:8080/static/src/vue/dist/ in a browser to access the application.

Note: 8080 is the default port to deploy to, but if that is busy, a different port will be used. The client terminal session will indicate the correct client URL in any case.

## Contact
* Jessica Bojorquez (email)
* Rishi Upadhyay ()
* Sicheng Mo (smo3@ucla.edu)
* Liyang Huang ()
* Deven Douglas (devendouglas@gmail.com)

