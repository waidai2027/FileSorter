import os
import logging
import shutil
from pathlib import Path

# Define paths
filespath = "C:/Users/hunte/Desktop/learn/categories/automation/randomfiles/"
subdirectories_path = "C:/Users/hunte/Desktop/learn/categories/automation"

# Get list of files in the source directory
files_list = os.listdir(filespath)

# File category mappings
file_categories = {
    'images': ['.jpg', '.png'],
    'documents': ['.pdf'],
    'videos': ['.mp4', '.mov'],
    'audios': ['.wav', '.mp3']
}

# Iterate through files
for file in files_list:
    # Identify the file type and move it to the appropriate subdirectory
    for category, extensions in file_categories.items():
        if any(file.endswith(ext) for ext in extensions):
            destination_dir = os.path.join(subdirectories_path, category)
            
            # Create the subdirectory if it doesn't exist
            if not os.path.isdir(destination_dir):
                os.makedirs(destination_dir)
            
            # Move the file
            shutil.move(os.path.join(filespath, file), os.path.join(destination_dir, file))
            logging.info(f"{file} moved to {destination_dir}")
            break
    else:
        print(f"No matching file type for: {file}")
