# Project Plan – Garbage Classification

## 1. Project Objective

The goal of this project is to develop and compare different machine learning models  
for the classification of garbage objects based on images.

The project aims to:
- analyze an image-based dataset of waste objects
- compare multiple classification approaches with increasing complexity
- evaluate model performance using appropriate and consistent metrics
- test the models on a custom dataset of images taken by the authors
- structure the data in a suitable **Database/Data Warehouse**, as required by the assignment

---

## 2. Dataset Description

The dataset consists of images representing different categories of garbage objects.

**Source:**
- Public dataset provided via Dropbox (see Assignment document)

**Main characteristics:**
- Image data (RGB images)
- Multiple waste categories
- Potential challenges:
  - class imbalance
  - variability in lighting conditions
  - heterogeneous backgrounds and object orientations

These characteristics motivate the comparison between traditional machine learning models and deep learning approaches.

---

## 3. Data Management and Storage

Raw image data will be stored locally and not tracked by GitHub.

### 3.1 Data Organization

The dataset will be organized as follows:
- `data/raw_flat/`: original images (unchanged)
- `data/external/`: images collected by the authors

### 3.2 Database / Data Warehouse

In accordance with the project guidelines, dataset metadata will be stored in a **PostgreSQL relational database**, as introduced during the course.

The database will store **metadata only**, while image files will remain on the filesystem.

Planned database structure includes:
- image identifier
- file path
- class label
- dataset split (train / validation / test / external)
- data source (raw / processed / external)

This approach ensures:
- structured data management
- reproducibility of experiments
- clear separation between raw data and derived data

---

## 4. Exploratory Data Analysis (EDA)

Before model training, an exploratory analysis will be performed to understand the dataset.

Main analyses:
- number of images per class
- visualization of sample images per category
- analysis of image dimensions and formats
- identification of potential issues (noise, imbalance, outliers)

The results of this phase will guide preprocessing choices and model selection.

---

## 5. Modeling Strategy

A **progressive modeling approach** will be adopted, in coherence with the course syllabus.

### 5.1 Baseline Model

A baseline classifier will be implemented using a **Logistic Regression** model.

- Images will be resized and transformed into feature vectors.
- Features will be normalized.
- The model will provide a simple and interpretable reference point.

### 5.2 Deep Learning Model

A **Convolutional Neural Network (CNN)** will be implemented for image classification.

The model may include:
- convolutional and pooling layers
- regularization techniques (e.g. dropout)
- optional data augmentation

If time permits, **transfer learning** may be explored as an extension.

All models will be implemented in a modular and reusable way.

---

## 6. Evaluation Methodology

Model performance will be evaluated using the same data split to ensure fairness.

Evaluation metrics include:
- accuracy
- confusion matrix
- class-wise performance measures (if needed)

Results will be compared quantitatively and discussed qualitatively.

---

## 7. Custom Test Dataset

A small custom dataset will be created using images taken by the authors.

Purpose:
- test model robustness on real-world data
- evaluate generalization beyond the original dataset

Results will be included in the evaluation and discussion sections.

---

## 8. Optional Extensions

If time permits, object detection techniques (e.g. YOLO) may be explored  
to identify multiple objects within a single image and classify them individually.

This part is optional and considered an additional contribution.

---

## 9. Final Deliverables

The project will include:
- a GitHub repository with structured code and documentation
- a PostgreSQL database for dataset metadata
- a written report (4–8 pages)
- presentation slides for a 5–10 minute oral discussion


a written report (4–8 pages)

presentation slides for a 5–10 minute oral discussion
