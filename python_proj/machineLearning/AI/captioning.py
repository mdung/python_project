import tensorflow as tf
from tensorflow.keras import layers, Model, optimizers
from tensorflow.keras.preprocessing import image
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.applications.inception_v3 import InceptionV3
from tensorflow.keras.applications.inception_v3 import preprocess_input
from tensorflow.keras.utils import to_categorical
from tensorflow.keras import Input
from tensorflow.keras.models import load_model
import numpy as np
import pickle

# Download the Flickr8k dataset or use any other suitable dataset
# Flickr8k dataset: https://www.kaggle.com/adityajn105/flickr8k

# Load Flickr8k dataset
image_dir = "path/to/Flicker8k_Dataset"
captions_file = "path/to/Flickr8k.token.txt"

# Load the image filenames and captions
def load_data(image_dir, captions_file):
    with open(captions_file, 'r') as f:
        lines = f.readlines()

    image_filenames = []
    captions = []

    for line in lines:
        parts = line.strip().split('\t')
        image_filename = parts[0]
        caption = parts[1]
        image_filenames.append(image_filename)
        captions.append(caption)

    return image_filenames, captions

image_filenames, captions = load_data(image_dir, captions_file)

# Create a tokenizer to process captions
tokenizer = tf.keras.preprocessing.text.Tokenizer(oov_token="<OOV>")
tokenizer.fit_on_texts(captions)
vocab_size = len(tokenizer.word_index) + 1

# Convert text to sequences and pad sequences
sequences = tokenizer.texts_to_sequences(captions)
max_sequence_length = max(len(seq) for seq in sequences)
padded_sequences = pad_sequences(sequences, maxlen=max_sequence_length, padding='post')

# Load InceptionV3 model pre-trained on ImageNet
image_model = InceptionV3(include_top=False, weights='imagenet')

# Extract features from images using InceptionV3
def extract_image_features(image_path):
    img = image.load_img(image_path, target_size=(299, 299))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)
    features = image_model.predict(img_array)
    features = tf.reshape(features, (features.shape[0], -1, features.shape[3]))
    return features

# Build the image captioning model
def build_captioning_model(vocab_size, max_sequence_length):
    # Image input
    image_input = Input(shape=(8, 8, 2048))

    # LSTM layer to process sequence data
    lstm = layers.LSTM(256)(image_input)

    # Output layer
    output = layers.Dense(vocab_size, activation='softmax')(lstm)

    # Combine the inputs and the output into a model
    model = Model(inputs=image_input, outputs=output)

    # Compile the model
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

    return model

# Build the model
caption_model = build_captioning_model(vocab_size, max_sequence_length)

# Train the captioning model
for epoch in range(10):
    for image_filename, sequence in zip(image_filenames, padded_sequences):
        image_path = os.path.join(image_dir, image_filename)
        image_features = extract_image_features(image_path)
        image_features = tf.reshape(image_features, (1, 8, 8, 2048))

        target_sequence = np.zeros((max_sequence_length, vocab_size))
        target_sequence[np.arange(len(sequence)), sequence] = 1

        caption_model.fit(image_features, target_sequence, epochs=1, verbose=0)

# Save the model and tokenizer
caption_model.save("image_caption_model.h5")
with open("tokenizer.pickle", "wb") as handle:
    pickle.dump(tokenizer, handle, protocol=pickle.HIGHEST_PROTOCOL)
