import numpy as np

def calculate_contrast(img) -> int:
	"""
	Calculate the contrast of a grayscale image.
	Args:
		img (numpy.ndarray): 2D array representing a grayscale image with pixel values between 0 and 255.
	"""

	max_pixel = np.max(np.max(img))
	min_pixel = np.min(np.min(img))

	return max_pixel - min_pixel
	# Your code here
	