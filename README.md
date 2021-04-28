# IMDB classification with Deep Learning
 Classify IMDB reviews as positive/negative using One Hot Encoding, Word Embedding and Recurrent Neural Network implemented with *Deep Learning with Python by Francois Chollet* Book.
 
## Techniques
#### 1. One Hot Encoding (Chapter 3 - Getting started wiht neural networks) - 85% Accuracy
#### 2. Task-spesific Word Embedding (Chapter 6 - Deep learning for text and sequences) - 76% Accuracy
- Sequences were limited to 20 words each. Incrase `max_len` for higher accuracy.
#### 3. Pretrained Word Embedding (Chapter 6 - Deep learning for text and sequences) - 50-60%
- I transformed the raw data into a dataframe for ease of access, However, you can download original review data from [Here](http://s3.amazonaws.com/text-datasets/aclImdb.zip) (75MB unzipped).
