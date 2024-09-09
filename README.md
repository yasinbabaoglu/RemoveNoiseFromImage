# Image Filtering with Averaging and Median Filters

This project provides a Python script that applies averaging and median filters to .pgm image files using OpenCV. The script reads .pgm images from the current directory, applies the filters, and saves the filtered images in the result directory.

## Prerequisites

Before running the script, ensure that you have Python installed along with the required libraries:

1. [Python](https://www.python.org/downloads/) (version 3.6 or higher recommended)
2. [OpenCV](https://pypi.org/project/opencv-python/) 
3. [NumPy](https://numpy.org/)

You can install the required libraries using pip:

bash
pip install opencv-python numpy


## How It Works

The script performs the following steps:

1. *Reading the Image*: The read function reads a .pgm image from the specified path in grayscale mode, displays it, and returns the image as a NumPy array.

2. *Applying Filters*:
   - *Averaging Filter*: The averaging_filter function applies an averaging filter to smooth the image. It creates a kernel for each pixel in the image and replaces the pixel with the average of the kernel values.
   - *Median Filter*: The median_filter function applies a median filter to reduce noise. It creates a kernel for each pixel and replaces the pixel with the median value of the kernel.

3. *Saving and Displaying Results*: The filtered images are displayed using OpenCV and saved in the result directory with modified filenames.

## Usage

1. Place your .pgm images in the same directory as the script.
2. Run the script with:

   bash
   python filter.py
   

3. The script will process all .pgm files in the directory, applying both filters and saving the results in the result directory.

### Functions Overview

- **read(path)**: Reads the image from the given path and returns it as a grayscale NumPy array.
- **create_kernel(image, i, j, k)**: Creates a kernel around the specified pixel (i, j) with size k x k.
- **averaging_filter(image, path, k=3)**: Applies an averaging filter with a kernel size k.
- **median_filter(image, path, k=3)**: Applies a median filter with a kernel size k.

## Output

Filtered images will be saved in a result directory, with filenames modified to indicate the type of filter applied (_average_new or _median_new).
