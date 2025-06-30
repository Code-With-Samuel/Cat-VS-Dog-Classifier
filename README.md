# 🐱🐶 Cat vs Dog Image Classifier (PyTorch Lightning)

This project is a simple yet powerful image classifier that distinguishes between images of **cats** and **dogs** using a **Convolutional Neural Network (CNN)** built with **PyTorch Lightning**.

---

## 🧠 Project Overview

- **Framework:** PyTorch & PyTorch Lightning  
- **Model:** Convolutional Neural Network (CNN)  
- **Task:** Binary Classification (Cat or Dog)  
- **Input:** Image (e.g., 32x32 RGB)  
- **Output:** Class label (0 = Cat, 1 = Dog)

---

## 📁 Folder Structure

cat_dog_classifier/
├── data/ # Dataset folder
├── model.py # Model definition (CNN using PyTorch Lightning)
├── train.py # Training loop
├── predict.py # Inference script
├── requirements.txt # All dependencies
└── README.md # You are here!

---

## 🔧 Setup Instructions

### 1. 🐍 Create & Activate Virtual Environment *(optional but recommended)*
```
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 2. Install Dependencies
```
pip install -r requirements.txt
```

---

## Model Architecture:
Input → Conv2D (3→16) → ReLU → MaxPool
      → Conv2D (16→32) → ReLU → MaxPool
      → Flatten → Linear(32*8*8 → 64) → ReLU
      → Linear(64 → 2)





