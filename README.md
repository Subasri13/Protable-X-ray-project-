Portable X-Ray Image Enhancement System
📌 Project Overview

This project focuses on developing an intelligent image processing pipeline for portable X-ray systems. It enhances low-quality X-ray images using adaptive techniques to improve diagnostic accuracy, especially in remote and low-resource healthcare environments.

Unlike traditional systems, this solution dynamically adjusts processing techniques based on image noise levels, ensuring optimal clarity and detail preservation.

🎯 Objectives
Enhance low-quality X-ray images for better diagnosis
Reduce noise while preserving important edges
Improve contrast for better visibility of structures
Provide automated image quality evaluation
🧠 Core Concept

The system uses an adaptive pipeline:

Detect noise level in the image
Apply suitable denoising technique
Enhance contrast dynamically
Sharpen edges without losing details
Evaluate output quality using metrics
⚙️ Features
🔍 Automatic Noise Estimation
🧹 Adaptive Denoising
Gaussian Blur (low noise)
Median Filter (medium noise)
Bilateral Filter (high noise)
🌗 Adaptive Contrast Enhancement (CLAHE)
✨ Edge-Preserving Sharpening
📊 Quality Metrics
PSNR (Peak Signal-to-Noise Ratio)
SSIM (Structural Similarity Index)
📁 Batch Processing of Multiple Images
🛠️ Technologies Used
Python
OpenCV (cv2)
NumPy
Matplotlib
scikit-image
🔬 System Pipeline
Image Loading
Converts image to grayscale
Resizes to 512x512
Normalizes pixel values
Noise Estimation
Uses Laplacian operator to detect noise level
Adaptive Denoising
Selects filter based on noise:
Low → Gaussian Blur
Medium → Median Filter
High → Bilateral Filter
Contrast Enhancement
Uses CLAHE (Contrast Limited Adaptive Histogram Equalization)
Sharpening
Edge-preserving sharpening using weighted addition
Evaluation
PSNR → measures image quality
SSIM → measures structural similarity
📊 Output Example

For each image:

Original X-ray displayed
Enhanced X-ray displayed
Noise level printed
PSNR and SSIM values shown
🚀 How to Run
Install dependencies:
pip install opencv-python numpy matplotlib scikit-image
Create dataset folder:
project/
 ├── dataset/
 │    ├── image1.jpg
 │    ├── image2.png
Run the script:
python your_script_name.py
📈 Results
Improved clarity of X-ray images
Reduced noise while preserving edges
Better visibility of bones and tissues
Quantitative improvement using PSNR & SSIM
🔮 Future Enhancements
Integrate AI for disease detection
Real-time X-ray processing
Web-based dashboard for doctors
Integration with hospital systems (HMS)
