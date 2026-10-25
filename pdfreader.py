import customtkinter as ctk
from tkinter import filedialog
import PyPDF2



def openfile():
    filename=filedialog.askopenfilename(title="Select PDF",filetypes=[("PDF","*.pdf")])
    if not filename:
        return

    
    reader=PyPDF2.PdfReader(filename)
    filelabel.configure(text=filename)
    text.delete("1.0",ctk.END)
    for page in range(len(reader.pages)):
        current_page=reader.pages[page].extract_text()
        text.insert(ctk.END,current_page)





window=ctk.CTk()

window.title("PDF Reader")


filelabel=ctk.CTkLabel(window,text="No file selected!")
filelabel.pack()
text=ctk.CTkTextbox(window,width=700,height=500)
text.pack()
openfilebutton=ctk.CTkButton(window,text="Open File",command=openfile)
openfilebutton.pack()

window.mainloop()