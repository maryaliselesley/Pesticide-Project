#import statements that allow packages to freely run
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
#creates the beginning of the pages 
root = tk.Tk()
#size of first window by pixels- can be expanded
root.geometry('400x300')
#Title you see in the window
root.title('Pesticides in Produce')

#Container that holds all the pages- somewhat like a main method 
MC = tk.Frame(root)
MC.pack(fill = tk.BOTH, expand = TRUE)


#Page one- Welcome
#Frames hold the page
pg1 = tk.Frame(MC)
#Labels hold the text
pg1label=tk.Label (pg1, text = 'Welcome!\n This application was created \nfor the purpose of displaying information \n about levels of pesticides in produce. \nPlease select next to continue.',font =('Times_New_Roman',45) )
#Pack makes sure that the label's contents get on the page
pg1label.pack()


#Page two- Celery
pg2 = tk.Frame(MC)
pg2label=tk.Label(pg2, text = 'Celery',font = ('Bold',30) )
info = tk.Label( pg2, text = 'What pesticides are found in Celery? \n Aldrin and Captan.\n  What is Aldrin?\n Aldrin is a pesticide that is used to deter insects from crops. \nAldrin is the type of pesticide that likes to stick around in produce and soil for a number of years. \n What health effects does Aldrin have?  \nLong time exposure to Aldrin has the following adverse effects:\n headaches, dizziness, irritability, vomiting, and uncontrolled muscle movement.',font =('Times_New_Roman',20))
pg2label.pack()
info.pack( side= "left")

#  Page three Box Plot Image - Celery
pg3 = tk.Frame(MC)
img_path = r'C:\Users\Wheez\Pictures\Screenshots\BoxPCelery.png'
image = Image.open(img_path)
img_tk = ImageTk.PhotoImage(image)
image = image.resize((500, 500))  
img_tk = ImageTk.PhotoImage(image)
image_label = Label(pg3, image=img_tk)
image_label.pack(pady=20,padx =20)


# Page four Scatter Plot Image-Celery
pg4 = tk.Frame(MC)
img_path2 =  r'C:\Users\Wheez\Pictures\Screenshots\ScatterCelery.png'
image2 = Image.open(img_path2)
img_tk2 = ImageTk.PhotoImage(image2)
image2 = image2.resize((500, 500)) 
img_tk2 = ImageTk.PhotoImage(image2)
image_label2 = Label(pg4, image=img_tk2)
image_label2.pack(pady=20,padx =20)
# Page five Bar graph Image - Celery
pg5 = tk.Frame(MC)
img_path3 =  r'C:\Users\Wheez\Pictures\Screenshots\Celerybar.png'
image3 = Image.open(img_path3)
img_tk3 = ImageTk.PhotoImage(image3)
image3 = image3.resize((500, 500)) 
img_tk3 = ImageTk.PhotoImage(image3)
image_label3 = Label(pg5, image=img_tk3)
image_label3.pack(pady=20,padx =20)



#Page six- Peaches

pg6 = tk.Frame(MC)
pg6label=tk.Label(pg6, text = 'Peaches',font = ('Bold',30) )
pg6label.pack()
info2 = tk.Label( pg6, text = 'What pesticides are found in Peaches? \n Aldrin and Captan.\n  What is Aldrin?\n Aldrin is a pesticide that is used to deter insects from crops. \nAldrin is the type of pesticide that likes to stick around in produce and soil for a number of years. \n What health effects does Aldrin have?  \nLong time exposure to Aldrin has the following adverse effects:\n headaches, dizziness, irritability, vomiting, and uncontrolled muscle movement.',font =('Times_New_Roman',20))
info2.pack( side= "left")

#  Page seven Box Plot Image - Peaches
pg7 = tk.Frame(MC)
img_path4 =  r'C:\Users\Wheez\Pictures\Screenshots\PeachesBox.png'
image4 = Image.open(img_path4)
img_tk4 = ImageTk.PhotoImage(image4)
image4 = image4.resize((500, 500)) 
img_tk4 = ImageTk.PhotoImage(image4)
image_label4 = Label(pg7, image=img_tk4)
image_label4.pack(pady=20,padx =20)


# Page eight Scatter Plot Image-Peaches
pg8 = tk.Frame(MC)
img_path5 =  r'C:\Users\Wheez\Pictures\Screenshots\ScatterPeaches.png'
image5 = Image.open(img_path5)
img_tk5 = ImageTk.PhotoImage(image5)
image5 = image5.resize((500, 500)) 
img_tk5 = ImageTk.PhotoImage(image5)
image_label5 = Label(pg8, image=img_tk5)
image_label5.pack(pady=20,padx =20)



# Page nine Bar graph Image - Peaches
pg9 = tk.Frame(MC)
img_path6 =  r'C:\Users\Wheez\Pictures\Screenshots\PeachesBar.png'
image6 = Image.open(img_path6)
img_tk6 = ImageTk.PhotoImage(image6)
image6 = image6.resize((500, 500)) 
img_tk6 = ImageTk.PhotoImage(image6)
image_label6 = Label(pg9, image=img_tk6)
image_label6.pack(pady=20,padx =20)




pg10 = tk.Frame(MC)
pg10label=tk.Label(pg10, text = 'Tomatoes',font = ('Bold',30) )
pg10label.pack()
info3 = tk.Label( pg10, text = 'What pesticides are found in Tomatoes? \n Aldrin and Captan.\n  What is Aldrin?\n Aldrin is a pesticide that is used to deter insects from crops. \nAldrin is the type of pesticide that likes to stick around in produce and soil for a number of years. \n What health effects does Aldrin have?  \nLong time exposure to Aldrin has the following adverse effects:\n headaches, dizziness, irritability, vomiting, and uncontrolled muscle movement.',font =('Times_New_Roman',20))
info3.pack( side= "left")

#  Page eleven Box Plot Image - Tomatoes
pg11 = tk.Frame(MC)
img_path7 =  r'C:\Users\Wheez\Pictures\Screenshots\Tomatoesbox.png'
image7 = Image.open(img_path7)
img_tk7 = ImageTk.PhotoImage(image7)
image7 = image7.resize((500, 500)) 
img_tk7 = ImageTk.PhotoImage(image7)
image_label7 = Label(pg11, image=img_tk7)
image_label7.pack(pady=20,padx =20)


# Page twelve Scatter Plot Image-Tomatoes
pg12 = tk.Frame(MC)
img_path8 =  r'C:\Users\Wheez\Pictures\Screenshots\TomatoesScatter.png'
image8 = Image.open(img_path8)
img_tk8 = ImageTk.PhotoImage(image8)
image8 = image8.resize((500, 500)) 
img_tk8 = ImageTk.PhotoImage(image8)
image_label8 = Label(pg12, image=img_tk8)
image_label8.pack(pady=20,padx =20)


# Page thirteen Bar graph Image - Tomatoes
pg13 = tk.Frame(MC)
img_path9 =  r'C:\Users\Wheez\Pictures\Screenshots\Tomatoesbar.png'
image9 = Image.open(img_path9)
img_tk9 = ImageTk.PhotoImage(image9)
image9 = image9.resize((500, 500)) 
img_tk9 = ImageTk.PhotoImage(image9)
image_label9 = Label(pg13, image=img_tk9)
image_label9.pack(pady=20,padx =20)


#This is the mechanism that allows the pages to move back and forth freely. The pages are placed in a list and a loop allows the list to be transversed
pages = [pg1,pg2,pg3,pg4,pg5,pg6,pg7,pg8,pg9,pg10,pg11,pg12,pg13]
count = 0

def next():
    global count 
    if  count < len(pages)-1:
       pages[count].pack_forget()
       count += 1
       pages[count].pack()

def back():
    global count 
    if  count > 0:
        pages[count].pack_forget()
        count -= 1
        pages[count].pack()

#Buttons that control the direction of the menu
F= tk.Frame(root)
bb= tk.Button(F, text = 'Back', font = ('Bold', 30), bg = '#CBC3E3', command = back)
bb.pack(side = tk.LEFT)

nb =tk.Button(F, text = 'Next', font = ('Bold',30), bg = '#CBC3E3', command = next)
nb.pack(side = tk.RIGHT)
F.pack(side = tk.BOTTOM)

pages[count].pack()
       
#THIS CONTROLS EVERYTHING. NOTHING WILL RUN WITHOUT THIS ONE SMALL LINE
root.mainloop()