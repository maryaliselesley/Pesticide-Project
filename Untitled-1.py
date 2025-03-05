from tkinter import *
from PIL import Image, ImageTk

# Create main window
root = Tk()
root.geometry('400x400')  # Set the window size

# Image path
img_path = r'C:\Users\Wheez\Pictures\Screenshots\BoxPCelery.png'
# Open the image using PIL
image = Image.open(img_path)
# Convert the image to a format that Tkinter can display
img_tk = ImageTk.PhotoImage(image)
image = image.resize((50, 50))  # Resize to 200x200 pixels, for example
img_tk = ImageTk.PhotoImage(image)

# Keep a reference to the image
 # This is important to prevent the image from being garbage collected

# Start the Tkinter main loop
root.mainloop()
