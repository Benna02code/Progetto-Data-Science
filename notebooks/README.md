All files of coding:
- 01: It populates the Database already structured with the data taken from images and correctly divided in train(70) / val(15) / test(15) from raw_flat. 
We will have an ID, path(relative), label (es: plastic), split (es:train), width, height, channels, file_hash and time of creation.

- 02: It loads the information from the DB reading image_id, filepath, label, split, source, width, height, channels. Then he create 3 different database based on the split saved in DB. Finally it defines the complete path necessary to take the image for the following model training.
