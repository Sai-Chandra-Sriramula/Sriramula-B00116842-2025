The Flickr8k_dataset is available for free from Illinois.edu website.Please use the link below to request the dataset: "https://illinois.edu/fb/sec/1713398"

The official edu site is not hosting the dataset at the current time.

Please refer to Jason Brownlee's GITHUB link to Download Flickr_8k dataset

Flickr8k_Dataset.zip https://github.com/jbrownlee/Datasets/releases/download/Flickr8k/Flickr8k_Dataset.zip

Flickr8k_text.zip https://github.com/jbrownlee/Datasets/releases/download/Flickr8k/Flickr8k_text.zip
The Above Datasets
1. Resized Images
	•	Loaded images from the Flickr8k Dataset.
	•	Resized each image to 224x224 pixels for consistency.

2. Tokenized Captions
	•	Loaded captions from Flickr8k.token.txt.
	•	Converted all text to lowercase.
	•	Removed punctuation to simplify processing.
	•	Tokenized the captions into words.
	•	Added  and  tokens to mark sentence boundaries.
