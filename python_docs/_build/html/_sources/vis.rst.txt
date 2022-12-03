Visualizer
==========

.. class:: Visualizer

	The Visualizer class that does most of the heavy lifting.

	.. py:attribute:: model

	The pytorch model we are testing

	.. py:attribute:: input_tensor

	The input image we are testing

	.. py:attribute:: input_shape

	Shape of the input_tensor

	.. py:attribute:: model_info

	A dictionary containing relevent details of the model such as number of parameters and layers of interest.

	.. py:function:: get_struct(self)

	Parses the structure of the inputted model to get relevant information and create an internal dictionary that includes the necessary info for later steps.

	:returns: torch summary struct from torchsummary


	.. py:function:: vis(self)

	Does the heavy-lifting of running the Grad-CAM algorithm. First identifies which layers we are interested in, then initializes the GradCAM object with these. After running the algorithm, converts the outputs in the to heatmap color format for visualization. Then converts the outputs into the json format that the backend and frontend expect and writes this file.

	:returns: None