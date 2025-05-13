pip install pyttsx3 PyPDF4

import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import Label, Button, Entry, IntVar, StringVar
from PyPDF4 import PdfFileReader
import pyttsx3

def read():
    path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if not path:
        return
    try:
        pdf_file = open(path, 'rb')
        pdf_reader = PdfFileReader(pdf_file)
        speaker = pyttsx3.init()

        start = int(start_pgNo.get())
        end = int(end_pgNo.get())

        for i in range(start, end + 1):
            page = pdf_reader.getPage(i)
            text = page.extractText()
            speaker.say(text)
            speaker.runAndWait()
        pdf_file.close()
    except Exception as e:
        messagebox.showerror("Error", str(e))

def pdf_to_audio():
    global start_pgNo, end_pgNo
    wn1 = tk.Tk()
    wn1.title("PDF to Audio Converter")
    wn1.geometry('500x400')
    wn1.config(bg='snow3')

    start_pgNo = IntVar()
    end_pgNo = IntVar()

    Label(wn1, text='PDF to Audio Converter', font=('Courier', 15)).pack(pady=10)
    Label(wn1, text='Start Page No.').pack()
    Entry(wn1, textvariable=start_pgNo).pack()
    Label(wn1, text='End Page No.').pack()
    Entry(wn1, textvariable=end_pgNo).pack()

    Button(wn1, text="Choose PDF and Convert to Audio", command=read).pack(pady=20)
    wn1.mainloop()

# Main GUI
root = tk.Tk()
root.title("PDF/Audio Converter")
root.geometry("400x200")
root.config(bg="lightblue")

Button(root, text="Convert PDF to Audio", font=('Courier', 12), command=pdf_to_audio).pack(pady=50)
root.mainloop()
