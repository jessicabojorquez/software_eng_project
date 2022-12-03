Utils
========

.. class:: OneImageDataset

	Creates a pytorch dataset that has only 1 image.

	.. py:attribute:: input_path

	The path to the directory with the images for this dataset

	.. py:attribute:: transform

	A pytorch transform that is applied to the image before returning. Optional


	.. py:function:: __len__(self)

	Returns the number of items in this dataset. Always 1. 

	.. py:function:: __getitem__(self, idx)

	Retrieves and returns the item corresponding to idx in the dataset.

	:param int idx: idx of item we want to retrieve
	:returns: image corresponding to idx

.. py:function:: copy2(src,dst)

	Copies files from src directory to dst directory

	:param str src: directory to copy from
	:param str dst: directory to copy to

.. py:function:: load_image(input_path)

	Loads an image from input_path if it exists else loads an image from the MNIST dataset

	:param str input_path: the input path to try to load a OneImageDataset from
	:returns: image

.. py:function:: write_json(content, path)

	Writes content to path in json format.

	:param dict content: The dictionary we want to write as json data
	:param str path: The path to save the json to

