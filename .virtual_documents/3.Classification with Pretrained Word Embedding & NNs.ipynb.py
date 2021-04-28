import keras
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


train_df = pd.read_csv('Raw Reviews/train.csv')
test_df = pd.read_csv('Raw Reviews/test.csv')

train_df.drop(columns = ['Unnamed: 0'], inplace = True)
test_df.drop(columns = ['Unnamed: 0'], inplace = True)

train_df.head()


maxlen = 100
training_samples = 200
validation_samples = 200
max_words = 1000

df = pd.concat([train_df, test_df])
texts = df['review']

tokenizer = Tokenizer(num_words = max_words)
tokenizer.fit_on_texts(texts)
sequences = tokenizer.texts_to_sequences(texts)
word_index = tokenizer.word_index

print('Unique tokens count:', word_index)

# Pad data
data = pad_sequence(sequences, maxlen = maxlen)


labels = np.array(df['value'])

print('Shape of Texts:', data.shape)
print('Shape of Labels:', labels.shape)

indices = np.arange(data.shape[0])
np.random.shuffle(indices)

data = list(data)

data = data[indices]
labels = labels[indices]

# Training data
x_train = data[:training_samples]
y_train = labels[:training_samples]

# Validation data
x_val = data[training_samples:  training_samples + validation_samples]
y_val = labels[training_samples: training_samples + validation_samples]












