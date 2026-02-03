All files of coding:
- **01_populate_db.ipynb**  
It populates the Database already structured with the data taken from images and correctly divided in train(70) / val(15) / test(15) from raw_flat. 
We will have an ID, path(relative), label (es: plastic), split (es:train), width, height, channels, file_hash and time of creation.

- **02_dataset_loader_from_db.ipynb**  
It shows how we work with images and data showing the pipeline used also in future models. It loads the information from the DB reading image_id, filepath, label, split, source, width, height, channels. Then he create 3 different database based on the split saved in DB. Finally it defines the complete path necessary to take the image for the model training.

- **03_eda_images.ipynb**  
  Performs exploratory data analysis on the image dataset, including class distributions, image properties,
  and basic pixel-level statistics.

- **04_baseline_logreg.ipynb**  
  Implements a Logistic Regression baseline using flattened image pixels, evaluates performance on validation and test sets, and analyzes results through classification reports and confusion matrices.

- **05_CNN_baseline.ipynb**  
  Trains and evaluates a baseline Convolutional Neural Network using a tf.data pipeline with on-the-fly preprocessing. The model clearly outperforms the logistic regression baseline and provides insight into class-specific confusions via confusion matrices and classification reports.

- **06_CNN_transfer.ipynb**  
  Trains and evaluates a Convolutional Neural Network using pretrained CNN on ImageNet. The pipeline involves an on-the-fly preprocessing, adapted to MobileNetV2, an head-only model training phase and finally a finetuning phase to slightly adapt the backbone. The model clearly outperforms the CNN baseline and provides great result with almost all the classes except trash.
