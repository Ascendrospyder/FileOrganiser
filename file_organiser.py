import os
import tkinter as tk
from tkinter import filedialog, messagebox

def organise_files_extensions(file_categories, folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            filename, file_extension = os.path.splitext(file)
            for category, extensions in file_categories.items():
                if file_extension.lower() in extensions:
                    category_path = os.path.join(root, category)
                    if not os.path.exists(category_path):
                        os.makedirs(category_path)
                    old_file_path = os.path.join(root, file)
                    new_file_path = os.path.join(category_path, file)
                    os.rename(old_file_path, new_file_path)
                    break
    
    messagebox.showinfo("Spyder's File Organiser", "Files have been organised!")
    open_folder = messagebox.askquestion("Open Folder", "Do you want to open the organised folder?")
    if open_folder == "yes":
        os.startfile(folder_path)

# Create the main window
root = tk.Tk()
root.title("File Organizer")

# Define the file categories
file_categories = {
    "Text Files": [".txt", ".csv", ".log", ".md"],
    "Binary Files": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".ico", ".mp3", ".wav", ".ogg", ".avi", ".mp4", ".mov"],
    "Document Files": [".doc", ".docx", ".pdf", ".ppt", ".pptx", ".odt", ".rtf"],
    "Spreadsheet Files": [".xls", ".xlsx", ".ods"],
    "Database Files": [".db", ".sqlite", ".mdb"],
    "Executable Files": [".exe", ".sh", ".bat"],
    "Archive Files": [".zip", ".tar", ".gz", ".rar", ".7z"],
    "Configuration Files": [".ini", ".cfg", ".xml", ".json"],
    "Web Files": [".html", ".htm", ".css", ".js", ".php", ".asp", ".jsp"],
    "Source Code Files": [".c", ".cpp", ".h", ".java", ".py", ".rb", ".go", ".swift", ".ts"],
    "Markup Files": [".xml", ".html", ".htm", ".xhtml"],
    "Font Files": [".ttf", ".otf", ".woff", ".woff2"],
    "Vector Image Files": [".svg", ".ai", ".eps"],
    "Raster Image Files": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Audio Files": [".mp3", ".wav", ".ogg"],
    "Video Files": [".avi", ".mp4", ".mov"],
    "Compressed Files": [".zip", ".tar", ".gz", ".rar", ".7z"],
    "Executable Files": [".exe", ".sh", ".bat"],
    "Document Files": [".doc", ".docx", ".pdf", ".ppt", ".pptx", ".odt", ".rtf"],
    "Miscellaneous": [".dat", ".bin", ".jar", ".dll", ".so", ".class"]
}


# Set window size and background color
root.geometry("400x300")
root.configure(bg="#f0f0f0")

# Create a label for title
title_label = tk.Label(root, text="Spyder's File Organizer", font=("Arial", 20), bg="#f0f0f0")
title_label.pack(pady=20)

# Create a button with styling
organize_button = tk.Button(root, text="Click me to organise files", command=lambda: organise_files_extensions(file_categories, filedialog.askdirectory()), bg="#4CAF50", fg="white", font=("Arial", 14))
organize_button.pack(pady=20)

# Run the GUI main loop
root.mainloop()
