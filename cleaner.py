from tkinter import *
from tkinter import messagebox, filedialog
import os
from tkinter.scrolledtext import ScrolledText
root = Tk()
root.title("Welcome to Python Automatic Cleaner")
root.geometry("500x500")


def browse_button():
    global folder_path
    currdir = os.getcwd()
    tempdir = filedialog.askdirectory(
        parent=root, initialdir=currdir, title='Please select a directory')
    folder_path.set(tempdir)


def print_to_textbox(wordlist):
    for lines in wordlist:
        text_box.insert("end", "\n"+lines)
    if len(wordlist) == 0:
        text_box.insert("1.0", "\nNothing To Display")


def search_files():
    folderPath = folder_path.get()
    text_box.delete("1.0", END)
    wordlist = []
    for i in os.listdir(folderPath):
        wordlist.append(i)
    print_to_textbox(wordlist)


def cleanup():
    def createIfNotExist(folder):
        if not os.path.exists(folder):
            os.makedirs(folder)

    def move(folderName, files):
        for file in files:
            os.replace(file, f"{folderName}/{file}")

    if __name__ == "__main__":
        folderPath = folder_path.get()
        os.chdir(folderPath)
        files=os.listdir()
        print(files)
        # files.remove("main.py")

        createIfNotExist('Images')
        createIfNotExist('Docs')
        createIfNotExist('Media')
        createIfNotExist('Others')

        imgExts = [".png", ".jpg", ".jpeg",".gif",".webp",".svg",".jfif"]
        images = [file for file in files if os.path.splitext(file)[
            1].lower() in imgExts]

        docExts = [".xls",".xlsx",".txt", ".docx", "doc", ".pdf",".pptx",".csv"]
        docs = [file for file in files if os.path.splitext(file)[
            1].lower() in docExts]

        mediaExts = [".mp4", ".mp3", ".flv",".avi",".wmv",".mpeg",".ogg",".3gp"]
        medias = [file for file in files if os.path.splitext(file)[
            1].lower() in mediaExts]

        others = []
        for file in files:
            ext = os.path.splitext(file)[1].lower()
            if (ext not in mediaExts) and (ext not in docExts) and (ext not in imgExts) and os.path.isfile(file):
                others.append(file)

        move("Images", images)
        move("Docs", docs)
        move("Media", medias)
        move("Others", others)


select_directory = Button(root, text="Select Directory", command=browse_button)
select_directory.pack()

folder_path = StringVar()
directory_label = Label(root, textvariable=folder_path, bg="#D3D3D3", width=70)
directory_label.pack()

go_button = Button(root, text="Go", command=search_files)
go_button.pack()

quit_button = Button(root, text="Cleanup", command=cleanup)
quit_button.pack()

text_box = ScrolledText(width=110, borderwidth=2, relief="sunken", padx=20)
text_box.pack()

root.mainloop()