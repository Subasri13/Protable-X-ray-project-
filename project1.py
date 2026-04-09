import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage.metrics import peak_signal_noise_ratio, structural_similarity
import os


# --------------------------------------------------
# Load and preprocess X-ray image
# --------------------------------------------------
def load_xray_image(image_path):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    if image is None:
        raise ValueError(f"❌ Image not found: {image_path}")

    image = cv2.resize(image, (512, 512))
    image = image.astype(np.float32) / 255.0
    return image


# --------------------------------------------------
# Noise Estimation
# --------------------------------------------------
def estimate_noise(image):
    laplacian = cv2.Laplacian(image, cv2.CV_32F)
    return np.std(laplacian)


# --------------------------------------------------
# Adaptive Denoising
# --------------------------------------------------
def adaptive_denoising(image, noise_level):
    image_uint8 = np.uint8(image * 255)

    if noise_level < 0.02:
        denoised = cv2.GaussianBlur(image_uint8, (3, 3), 0)
    elif noise_level < 0.05:
        denoised = cv2.medianBlur(image_uint8, 3)
    else:
        denoised = cv2.bilateralFilter(image_uint8, 9, 75, 75)

    return denoised.astype(np.float32) / 255.0


# --------------------------------------------------
# Adaptive Contrast Enhancement
# --------------------------------------------------
def adaptive_contrast(image, noise_level):
    image_uint8 = np.uint8(image * 255)

    clip_limit = 1.5 if noise_level > 0.05 else 2.5
    clahe = cv2.createCLAHE(clipLimit=clip_limit, tileGridSize=(8, 8))

    enhanced = clahe.apply(image_uint8)
    return enhanced.astype(np.float32) / 255.0


# --------------------------------------------------
# Edge-Preserving Sharpening
# --------------------------------------------------
def edge_preserving_sharpen(image):
    blurred = cv2.GaussianBlur(image, (3, 3), 0)
    sharpened = cv2.addWeighted(image, 1.2, blurred, -0.2, 0)
    return np.clip(sharpened, 0, 1)


# --------------------------------------------------
# Complete Pipeline
# --------------------------------------------------
def portable_xray_pipeline(image_path):
    original = load_xray_image(image_path)
    noise_level = estimate_noise(original)

    denoised = adaptive_denoising(original, noise_level)
    contrast_enhanced = adaptive_contrast(denoised, noise_level)
    final_image = edge_preserving_sharpen(contrast_enhanced)

    return original, final_image, noise_level


# --------------------------------------------------
# Evaluation Metrics
# --------------------------------------------------
def evaluate_image(original, enhanced):
    original_uint8 = np.uint8(original * 255)
    enhanced_uint8 = np.uint8(enhanced * 255)

    psnr_val = peak_signal_noise_ratio(original_uint8, enhanced_uint8)
    ssim_val = structural_similarity(original_uint8, enhanced_uint8)

    return psnr_val, ssim_val


# --------------------------------------------------
# MAIN (Batch Processing)
# --------------------------------------------------
if __name__ == "__main__":

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    DATASET_DIR = os.path.join(BASE_DIR, "dataset")

    image_files = [
        f for f in os.listdir(DATASET_DIR)
        if f.lower().endswith((".png", ".jpg", ".jpeg"))
    ]

    print(f"\nFound {len(image_files)} X-ray images\n")

    for img_name in image_files:
        image_path = os.path.join(DATASET_DIR, img_name)

        print(f"Processing: {img_name}")

        original, enhanced, noise = portable_xray_pipeline(image_path)
        psnr_val, ssim_val = evaluate_image(original, enhanced)

        # Display results
        plt.figure(figsize=(10, 4))

        plt.subplot(1, 2, 1)
        plt.title("Original X-ray")
        plt.imshow(original, cmap="gray")
        plt.axis("off")

        plt.subplot(1, 2, 2)
        plt.title("Enhanced X-ray")
        plt.imshow(enhanced, cmap="gray")
        plt.axis("off")

        print(f"Noise Level : {noise:.4f}")
        print(f"PSNR       : {psnr_val:.2f} dB")
        print(f"SSIM       : {ssim_val:.4f}")
        print("-" * 40)

        plt.suptitle(img_name)
        plt.show()

