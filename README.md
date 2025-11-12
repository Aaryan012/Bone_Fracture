# Bone Fracture Detection Web App

A web application that detects bone fractures from user-provided images using **Machine Learning** and **Computer Vision** techniques.

---

## Overview

This project uses **Streamlit** to create an interactive web interface where users can upload an X-ray image, and the app predicts whether the bone is fractured or normal. The system leverages:

- **Python Libraries:** OpenCV, NumPy, Pandas, Matplotlib, Seaborn  
- **Machine Learning Algorithm:** XGBoost (achieved highest accuracy compared to other models)  
- **Computer Vision Techniques** for image preprocessing  

---

## Features

- Upload an X-ray image via a simple web interface.  
- Real-time bone fracture detection.  
- Visual insights using plots and image analysis.  
- High accuracy using XGBoost model.  

---
### Dataset & Files

- Due to size limitations, the dataset and final CSV are hosted on Google Drive:
 https://drive.google.com/drive/folders/1U_xWBCQuUfhVZe31DfsK5NDlnL0ju1G2?usp=drive_link
- Contains images for both fractured
- Contains preprocessed data ready for model training/testing.

## Installation Instructions

- Download the files from the links above.  
- Place the images in the `combine/` folder in your project directory.  
- Place the CSV file in the folder.  

Clone the repository:
```bash
git clone https://github.com/<your-username>/<repo-name>.git
