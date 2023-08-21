# File Organizer Documentation

The File Organiser is a utility designed to help you organise your files based on their file extensions. It categorises files into various predefined categories for better file management. We do this by searching for the folder of interest we want to categorise. The script will then intelligently go over all the folders, subfolders and files in the cwd and organise them into folders based on the file extension type.

## File Categories and Extensions

Here is a list of file categories and their associated extensions that the File Organizer supports:

### Text Files
- Extensions: .txt, .csv, .log, .md

### Binary Files
- Extensions: .jpg, .jpeg, .png, .gif, .bmp, .ico, .mp3, .wav, .ogg, .avi, .mp4, .mov

### Document Files
- Extensions: .doc, .docx, .pdf, .ppt, .pptx, .odt, .rtf

### Spreadsheet Files
- Extensions: .xls, .xlsx, .ods

### Database Files
- Extensions: .db, .sqlite, .mdb

### Executable Files
- Extensions: .exe, .sh, .bat

### Archive Files
- Extensions: .zip, .tar, .gz, .rar, .7z

### Configuration Files
- Extensions: .ini, .cfg, .xml, .json

### Web Files
- Extensions: .html, .htm, .css, .js, .php, .asp, .jsp

### Source Code Files
- Extensions: .c, .cpp, .h, .java, .py, .rb, .go, .swift, .ts

### Markup Files
- Extensions: .xml, .html, .htm, .xhtml

### Font Files
- Extensions: .ttf, .otf, .woff, .woff2

### Vector Image Files
- Extensions: .svg, .ai, .eps

### Raster Image Files
- Extensions: .jpg, .jpeg, .png, .gif, .bmp

### Audio Files
- Extensions: .mp3, .wav, .ogg

### Video Files
- Extensions: .avi, .mp4, .mov

### Compressed Files
- Extensions: .zip, .tar, .gz, .rar, .7z

### Miscellaneous
- Extensions: .dat, .bin, .jar, .dll, .so, .class

## Prerequisites
- Python 3.6+
- Required Python packages (listed in `requirements.txt`)

## Installation
1. git clone git@github.com:Ascendrospyder/FileOrganiser.git
2. cd FileOrganiser (change to project directory)
3. pip install -r requirements.txt (install any packages)
4. python main.py (run the script)


## How to Use

1. Launch the File Organizer utility.
2. Select the target folder you want to organize.
3. Click the "Organize Files" button to start the organization process.
4. The utility will create folders for each category and move the files based on their extensions into the corresponding folders.
5. A prompt will inform you when the files have been organized.
6. You have the option to open the organized folder to view the categorized files.

## Customization

You can customize the list of file categories and their associated extensions in the code to match your specific needs.

## Demo
![image](https://github.com/Ascendrospyder/FileOrganiser/assets/99483579/dbd5df5a-05f9-4183-bc2e-62e66ff89ce3)
![image](https://github.com/Ascendrospyder/FileOrganiser/assets/99483579/e22ba5d2-d916-4298-9202-acc740ba2063)
![image](https://github.com/Ascendrospyder/FileOrganiser/assets/99483579/9a91b308-1b31-4111-9a62-fc160f4eefc7)


## Important Note

This documentation provides a comprehensive list of common file categories and extensions, but it may not cover every possible file extension. The list can be adjusted and expanded based on your requirements.

