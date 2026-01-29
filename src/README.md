This folder contains function used frequently in notebooks operation. It will be divided in:

# Features

This folder contains all functions related to data preprocessing and feature extraction.

Typical operations include:
- image resizing
- normalization
- data augmentation
- any transformation applied to raw images before model training

Only reusable and stable code should be placed here.
Exploratory or temporary code should remain in notebooks.

# Data

This folder contains code to load and manage datasets.

Typical tasks:
- loading image paths and labels
- handling train/validation/test splits
- interfacing with the dataset storage structure

# Models

This folder contains model definitions and training routines.

It includes:
- model architectures
- training loops
- model saving and loading utilities

# Evaluation

This folder contains functions used to evaluate model performance.

Typical contents:
- accuracy and loss computation
- confusion matrix generation
- comparison of different classifiers
