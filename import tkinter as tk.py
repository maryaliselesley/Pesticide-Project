import tkinter as tk
from tkinter import *

# Create main window
root = tk.Tk()
root.geometry('400x300')
root.title('Pesticides in Produce')

# Container that holds all the pages
MC = tk.Frame(root)
MC.pack(fill=tk.BOTH, expand=True)

# Page 1 - Welcome
pg1 = tk.Frame(MC)
pg1label = tk.Label(pg1, text='Welcome!\nThis application was created\nfor the purpose of displaying information\nabout levels of pesticides in produce.\nPlease select next to continue.', font=('Times_New_Roman', 20))
pg1label.pack()

# Page 2 - Celery
pg2 = tk.Frame(MC)
pg2label = tk.Label(pg2, text='Celery', font=('Bold', 30))
info = tk.Label(pg2, text='What pesticides are found in Celery?\nAldrin and Captan.\n\nWhat is Aldrin?\nAldrin is a pesticide that is used to deter insects from crops. It lingers in produce and soil for a long time.\n\nHealth effects:\nLong-term exposure to Aldrin can cause headaches, dizziness, irritability, vomiting, and uncontrolled muscle movements.',font=('Times_New_Roman', 20))
pg2label.pack()
info.pack()

# Page 3 - Peaches
pg3 = tk.Frame(MC)
pg3label = tk.Label(pg3, text='Peaches', font=('Bold', 30))
pg3label.pack()

# Page 4 - Tomatoes
pg4 = tk.Frame(MC)
pg4label = tk.Label(pg4, text='Tomatoes', font=('Bold', 30))
pg4label.pack()

# List of all pages for navigation
pages = [pg1, pg2, pg3, pg4]
count = 0

def next():
    global count
    if count < len(pages) - 1:  # Ensure we're not going past the last page
        pages[count].pack_forget()  # Hide the current page
        count += 1  # Move to the next page
        pages[count].pack()  # Show the next page

def back():
    global count
    if count > 0:  # Ensure we're not going past the first page
        pages[count].pack_forget()  # Hide the current page
        count -= 1  # Move to the previous page
        pages[count].pack()  # Show the previous page

# Navigation buttons
F = tk.Frame(root)
bb = tk.Button(F, text='Back', font=('Bold', 20), bg='#CBC3E3', command=back)
bb.pack(side=tk.LEFT, padx=20)
nb = tk.Button(F, text='Next', font=('Bold', 20), bg='#CBC3E3', command=next)
nb.pack(side=tk.RIGHT, padx=20)
F.pack(side=tk.BOTTOM, pady=10)

# Show the first page initially
pages[count].pack()

# Run the application
root.mainloop()
