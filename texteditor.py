import tkinter as tk
from tkinter import filedialog, messagebox, font
from tkinter import PhotoImage

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, "r") as file:
            text_editor.delete("1.0", tk.END)
            text_editor.insert(tk.END, file.read())

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, "w") as file:
            text_content = text_editor.get("1.0", tk.END)
            file.write(text_content)
        messagebox.showinfo("File Saved", "File has been saved successfully.")

def set_font():
    selected_font = font.Font(family="Arial", size=12, weight="normal")
    font_str = selected_font.actual()["family"] + " " + str(selected_font.actual()["size"]) + " " + selected_font.actual()["weight"]
    text_editor.configure(font=font_str)

def about():
    messagebox.showinfo("About", "This is a simple text editor created using Python and Tkinter.")

root = tk.Tk()
root.title("Text Editor")
root.geometry("800x600")

image_icon = PhotoImage(file="logo png.png")
root.iconphoto(False, image_icon)

text_editor = tk.Text(root)
text_editor.pack(fill=tk.BOTH, expand=True)

menu_bar = tk.Menu(root)

file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)
menu_bar.add_cascade(label="File", menu=file_menu)

format_menu = tk.Menu(menu_bar, tearoff=0)
format_menu.add_command(label="Font", command=set_font)
menu_bar.add_cascade(label="Format", menu=format_menu)

help_menu = tk.Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About", command=about)
menu_bar.add_cascade(label="Help", menu=help_menu)

root.config(menu=menu_bar)
root.mainloop()
