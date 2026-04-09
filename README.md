Portable X-Ray Image Enhancement System

Project Overview

This project focuses on developing an intelligent image processing pipeline for portable X-ray systems. It enhances low-quality X-ray images using adaptive techniques to improve diagnostic accuracy, especially in remote and low-resource healthcare environments.Unlike traditional systems, this solution dynamically adjusts processing techniques based on image noise levels, ensuring optimal clarity and detail preservation.

Objectives

Enhance low-quality X-ray images for better diagnosis
Reduce noise while preserving important edges
Improve contrast for better visibility of structures
Provide automated image quality evaluation

 Core Concept
The system uses an adaptive pipeline:
Detect noise level in the image
Apply suitable denoising technique
Enhance contrast dynamically
Sharpen edges without losing details
Evaluate output quality using metrics

 Features
 Automatic Noise Estimation
 Adaptive Denoising
Gaussian Blur (low noise)
Median Filter (medium noise)
Bilateral Filter (high noise)
Adaptive Contrast Enhancement (CLAHE)
Edge-Preserving Sharpening

 Quality Metrics
PSNR (Peak Signal-to-Noise Ratio)
SSIM (Structural Similarity Index)
 Batch Processing of Multiple Images
 
  Technologies Used
Python
OpenCV (cv2)
NumPy
Matplotlib
scikit-image


