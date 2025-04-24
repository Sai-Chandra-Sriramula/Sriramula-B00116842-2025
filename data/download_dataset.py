import os
import kaggle

# Set your dataset name and target path
KAGGLE_DATASET = 'aladdinpersson/flickr8kimagescaptions'
DOWNLOAD_DIR = 'flickr8k_dataset'

# Make sure directory exists
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

# Download dataset
print(f"📦 Downloading '{KAGGLE_DATASET}' to ./{DOWNLOAD_DIR}")
kaggle.api.dataset_download_files(KAGGLE_DATASET, path=DOWNLOAD_DIR, unzip=True)
print("✅ Download complete.")
