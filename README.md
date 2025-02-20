The Flickr8k_dataset is available for free from Illinois.edu website.Please use the link below to request the dataset: "https://illinois.edu/fb/sec/1713398"

The official edu site is not hosting the dataset at the current time.

Please refer to Jason Brownlee's GITHUB link to Download Flickr_8k dataset

Flickr8k_Dataset.zip https://github.com/jbrownlee/Datasets/releases/download/Flickr8k/Flickr8k_Dataset.zip

Flickr8k_text.zip https://github.com/jbrownlee/Datasets/releases/download/Flickr8k/Flickr8k_text.zip

✅ Step 1: Load and Preprocess the Dataset

Loaded images from Flickr8k_Dataset.
Loaded captions from Flickr8k_text.
Preprocessed captions (tokenized, removed special characters, padded sequences).


1️- Extracting Image Features with CNN (ResNet-50)
Imagine looking at a picture and identifying key details—like a dog, a beach, or a sunset. That’s what ResNet-50 will do for us! It will scan images and break them down into meaningful patterns (2048-number summaries) that our model can understand.

2️- Turning Features into Words with RNN (LSTM)
Now, we need to turn those image patterns into words. Our LSTM (a type of RNN) will act like a storyteller. It will take the image’s features and start forming a sentence—one word at a time—predicting what comes next based on what it has seen so far.

3️- Building the Full Captioning Model
This is where we connect the dots! The CNN extracts features, passes them to the LSTM, and the LSTM generates captions. The goal? Train this model so it learns to describe images just like a human would.
In This Week i am working to build this model which aligns to requirements of my project.


NOTE :-
hey professor when iam uploading my code source file to github, its uploading perfectly fine but when i open that file its not opening its sayinng "Unable to render code block"

i would like to scedule meeting regarding this problem even last week i couldnt resolve this.
