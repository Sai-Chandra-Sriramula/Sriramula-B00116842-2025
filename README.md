The Flickr8k_dataset is available for free from Illinois.edu website.Please use the link below to request the dataset: "https://illinois.edu/fb/sec/1713398"

The official edu site is not hosting the dataset at the current time.

Please refer to Jason Brownlee's GITHUB link to Download Flickr_8k dataset

Flickr8k_Dataset.zip https://github.com/jbrownlee/Datasets/releases/download/Flickr8k/Flickr8k_Dataset.zip

Flickr8k_text.zip https://github.com/jbrownlee/Datasets/releases/download/Flickr8k/Flickr8k_text.zip

✅ Step 1: Load and Preprocess the Dataset

Loaded images from Flickr8k_Dataset.
Loaded captions from Flickr8k_text.
Preprocessed captions (tokenized, removed special characters, padded sequences).


✅ Step 2: Prepared Captions as Model Input

Converted text captions into numerical sequences.
Applied padding to make sequences uniform in length.

since we have completed Data Prrprocessing, now we are movibg to build CNN-RNN model(prebuild and some manual Build tools) this week.
We'll use a model that consists of:

CNN (Encoder): A pretrained model like Inception to extract image features.

RNN (Decoder): An LSTM or GRU to generate captions.

iam working to build this model which aligns to requirements of my project.
