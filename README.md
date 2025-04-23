# Image Captioning System using DenseNet201, Xception, and InceptionV3 with Attention Mechanism  
**Spring 2025 Project – Sai Chandra Sriramula (B00116842)**

---

##  Project Overview

This project explores the task of automatic image captioning using deep learning. The model combines CNN-based visual feature extraction with an RNN-based sequence generator enhanced with an attention mechanism. Specifically, three different CNN backbones — **DenseNet201**, **Xception**, and **InceptionV3** — are compared in terms of their performance in generating image descriptions.

Key features of the project:
-  **CNN Backbones**: Feature extraction using pretrained DenseNet201, Xception, and InceptionV3 (on ImageNet)
-  **Caption Generator**: GRU-based Recurrent Neural Network (RNN)
-  **Attention Mechanism**: Helps focus on important regions of the image while predicting each word
-  **Evaluation**: Comparison using BLEU scores to measure caption quality

>  **Real-world application**: The system can be adapted for **medical imaging**, where automatic captioning of diagnostic images (e.g., X-rays, MRIs) can assist in reporting and accessibility.

---

##  Dataset Information

The project uses the **Flickr8k** dataset, a standard benchmark dataset for image captioning:
-  8,000 real-world images
-  Each image is paired with 5 human-written captions

###  Download Instructions
Since the dataset is large, it's not included in the repository. Please download manually:

- https://www.kaggle.com/datasets/aladdinpersson/flickr8kimagescaptions

Place the unzipped folders in the following directory structure:

```
data/
├── Flickr8k_Dataset/
├── Flickr8k_text/
```

---

## ⚙ How to Run / Interact / Reproduce

###  Step 1: Clone the Repository
```bash
git clone https://github.com/Sai-Chandra-Sriramula/Sriramula-B00116842-Fall-2025.git
cd Sriramula-B00116842-Fall-2025
```

###  Step 2: Install Required Libraries
```bash
pip install tensorflow numpy matplotlib pillow
```

###  Step 3: Prepare the Dataset

After downloading and extracting the dataset files into the `data/` directory, ensure the following paths exist:
```
data/
├── Flickr8k_Dataset/      # Contains .jpg image files
├── Flickr8k_text/         # Contains captions.txt
```

###  Step 4: Run the Notebooks

Launch the following notebooks to run the full pipeline:

- `src/image-captioning Final Models.ipynb`  
   Contains preprocessing, feature extraction using 3 CNNs, and training with BLEU evaluation

- `src/image-caption-attention.ipynb`  
   Focuses on using attention during caption generation and visualizing attention weights

---

##  If Data is Too Big for `data/` Directory

If you're unable to store the dataset in your local repo:
- Download the dataset using the links above
- Extract the files externally and **point the notebook paths** to the correct folder location

---

