import tensorflow as tf
from tensorflow import keras
from .paths import abs_path

AUTOTUNE = tf.data.AUTOTUNE

# Crea le mappe label<->id
def build_label_maps(labels):
    labels = sorted(list(labels))
    label2id = {lab: i for i, lab in enumerate(labels)}
    id2label = {i: lab for lab, i in label2id.items()}
    return label2id, id2label

# Carica e preprocessa un'immagine
def load_and_preprocess(path, label, img_size):
    img_bytes = tf.io.read_file(path)
    img = tf.image.decode_image(img_bytes, channels=3, expand_animations=False)
    img.set_shape([None, None, 3])

    # resize con pad: preserva aspect ratio (non taglia, non “zoomma”)
    img = tf.image.resize_with_pad(img, img_size[0], img_size[1])  # (H,W)

    # [0,255] -> [0,1]
    img = tf.cast(img, tf.float32) / 255.0
    return img, label

#effettua augmentazione dati (verrà usata solo nel training)
def get_augmentation():
    return keras.Sequential([
        keras.layers.RandomFlip("horizontal"),
        keras.layers.RandomRotation(0.05),
        keras.layers.RandomZoom(0.1),
    ], name="data_augmentation")

# Crea il dataset tf.data.Dataset per training/validation
def make_dataset(df_split, training, img_size, batch_size, seed, augment=False):
    paths = [str(abs_path(p)) for p in df_split["filepath"].tolist()]
    labels = df_split["label_id"].astype("int32").tolist()

    ds = tf.data.Dataset.from_tensor_slices((paths, labels))

    if training:
        ds = ds.shuffle(buffer_size=len(df_split), seed=seed, reshuffle_each_iteration=True)

    ds = ds.map(lambda p, y: load_and_preprocess(p, y, img_size),
                num_parallel_calls=AUTOTUNE)

    if training and augment:
        aug = get_augmentation()
        ds = ds.map(lambda x, y: (aug(x, training=True), y),
                    num_parallel_calls=AUTOTUNE)

    ds = ds.batch(batch_size).prefetch(AUTOTUNE)
    return ds
