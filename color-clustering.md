# 🖼️ Image Color Clustering App
Discover the `dominant colors` in any image using unsupervised machine learning!

## 🔗 Live App
Access the live deployed project at [https://samyak-jain-ml.streamlit.app/](https://samyak-jain-ml.streamlit.app/)
<img width="1920" height="964" alt="image" src="https://github.com/user-attachments/assets/1be70071-3833-4aca-830b-140a0ee5c63b" />
A look at the webpage.

## Overview
This Streamlit app allows users to upload an image and instantly visualize its `top 5 dominant colors`. The app leverages clustering algorithms to analyze the color distribution and present the results in an intuitive, interactive format.

Features
Image Upload: Supports `.jpg`, `.jpeg`, and `.png` formats.
Color Extraction: Uses `KMeans`, `Agglomerative Clustering`, and `Gaussian Mixture Models` to find color clusters.
Visual Output: Displays color swatches for each algorithm, showing the most representative colors in your image.
Automatic Cleanup: Uploaded images are deleted after processing to keep your workspace tidy.
How It Works:
- Upload an Image:
- The app reads your image and resizes it for efficient processing.
- The image is converted to a DataFrame of RGB values.
- KMeans: Groups pixels into clusters based on color similarity.
- Agglomerative Clustering: Hierarchically merges pixels into color groups.
- Gaussian Mixture Models: Models the color distribution as a mixture of Gaussian components.
