# Project Plan – Garbage Classification

## 1. Project Objective
The goal of this project is to develop and compare different machine learning models
for the classification of garbage objects based on images.

The project aims to:
- analyze an image-based dataset of waste objects
- compare multiple classification approaches
- evaluate model performance using appropriate metrics
- test the models on a custom dataset of images taken by the authors

---

## 2. Dataset Description
The dataset consists of images representing different categories of garbage objects.

Source:
- Public dataset provided via Dropbox (see Assignment document)

Main characteristics:
- Image data
- Multiple waste categories
- Potential challenges: class imbalance, variability in lighting and backgrounds

---

## 3. Data Management and Storage
Raw data will be stored locally and not tracked by GitHub.

Data organization:
- `data/raw/`: original images (unchanged)
- `data/processed/`: preprocessed images ready for training
- `data/external/`: images collected by the authors

Preprocessing steps may include:
- image resizing
- normalization
- optional data augmentation

The dataset will be split into:
- training set
- validation set
- test set

---

## 4. Exploratory Data Analysis (EDA)
Before model training, an exploratory analysis will be performed to understand the dataset.

Main analyses:
- number of images per class
- visualization of sample images
- identification of potential issues (noise, imbalance, outliers)

The results of this phase will guide preprocessing and model selection.

---

## 5. Modeling Strategy
A progressive modeling approach will be adopted.

Steps:
1. Definition of a baseline classifier
2. Implementation of more advanced models (e.g. CNNs or transfer learning)
3. Comparison of different classifiers

Models will be implemented in a modular way to ensure reproducibility and clarity.

---

## 6. Evaluation Methodology
Model performance will be evaluated using quantitative metrics.

Possible metrics include:
- accuracy
- confusion matrix
- class-wise performance measures

Models will be compared using the same test set to ensure fairness.

---

## 7. Custom Test Dataset
A small custom dataset will be created using images taken by the authors.

Purpose:
- test model robustness on real-world data
- evaluate generalization beyond the original dataset

Results will be discussed qualitatively and quantitatively.

---

## 8. Optional Extensions
If time permits, object detection techniques (e.g. YOLO) may be explored
to identify multiple objects within a single image and classify them individually.

This part is optional and considered an additional contribution.

---

## 9. Final Deliverables
The project will include:
- a GitHub repository with structured code and documentation
- a written report (4–8 pages)
- presentation slides for a 5–10 minute oral discussion
