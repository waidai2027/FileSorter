# File Organizer

File Organizer is a Python script designed to automate the organization of files in a specified directory into categorized subdirectories. It efficiently moves files based on their extensions, helping you keep your workspace tidy.

## Features
- Automatically categorizes and organizes files into subdirectories: images, documents, videos, and audios.
- Supports common file types:
  - Images: .jpg, .png
  - Documents: .pdf
  - Videos: .mp4, .mov
  - Audios: .wav, .mp3
- Creates subdirectories if they do not already exist.
- Logs each file movement for easy tracking and debugging.

## Prerequisites
- Python 3.x installed on your machine.
- No external dependencies required; only built-in Python modules.

## Installation
1. Clone the repository:

git clone https://github.com/your-username/file-organizer.git

2. Navigate to the project directory:

cd file-organizer

3. Ensure your file paths in the script are correct.

## Usage
1. Open the script and update the following paths:
- filespath: The directory containing files to be organized.
- subdirectories_path: The directory where organized subfolders will be created.

Example:
filespath = "C:/path/to/randomfiles/" subdirectories_path = "C:/path/to/subdirectories/"

2. Run the script:
   
   python file_organizer.py

3. The script will categorize files and move them into the respective subdirectories. Check the console for logging information about each file moved.

## Logging
- The script logs detailed information about each file movement, indicating where files were moved to, aiding in easy tracking.

## Customization
You can easily extend the script to support additional file types by updating the file_categories dictionary with new extensions and corresponding subdirectory names.

Example to add .docx support:

file_categories = { 'images': ['.jpg', '.png'], 'documents': ['.pdf', '.docx'], ... }


## Contributing
Contributions are welcome! Feel free to fork the repository, make changes, and submit a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

