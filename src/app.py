import tkinter as tk
from tkinter import *
import tkinter.font as font

window = tk.Tk()
window.title("Markdown Editor")


def h1_markdown():
    selection = txt_edit.selection_get()
    txt_result.insert(tk.END, "# "+selection)
def h2_markdown():
    selection = txt_edit.selection_get()
    txt_result.insert(tk.END, "## "+selection)
def h3_markdown():
    selection = txt_edit.selection_get()
    txt_result.insert(tk.END, "### "+selection)
def body_markdown():
    selection = txt_edit.selection_get()
    txt_result.insert(tk.END, selection)
def italic_markdown():
    selection = txt_edit.selection_get()
    txt_result.insert(tk.END, "*"+selection+"*")

txt_edit = tk.Text(window)
txt_result = tk.Text(window)

h1Font = font.Font(weight="bold", size=38)
h2Font = font.Font(weight="bold", size=28)
h3Font = font.Font(weight="bold", size=22)
bodyFont =  font.Font(size=12)
italicFont =  font.Font(slant="italic", size=12)

button_h1 = Button(window, text="Headline1", command=h1_markdown)
button_h1["font"] = h1Font
button_h1.pack()

button_h2 = Button(window, text="Headline2", command=h2_markdown)
button_h2["font"] = h2Font
button_h2.pack()

button_h3 = Button(window, text="Headline3", command=h3_markdown)
button_h3["font"] = h3Font
button_h3.pack()

button_body = Button(window, text="Body", command=body_markdown)
button_body["font"] = bodyFont
button_body.pack()

button_italic = Button(window, text="Italic", command=italic_markdown)
button_italic["font"] = italicFont
button_italic.pack()

txt_edit.pack()
txt_result.pack()

window.mainloop() 
