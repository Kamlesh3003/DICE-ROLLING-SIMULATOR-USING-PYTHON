import tkinter
from PIL import Image, ImageTk
import random

# Widget which shows the main window of the applictaion
root = tkinter.Tk()
root.geometry('400x500')
root.title('Dice rolling simulator')

# Adding label into the frame
l0 = tkinter.Label(root, text="")
l0.pack()

# Adding label with different font and formatting
l1 = tkinter.Label(root, text="Welcome to Kamlesh's DICE!", fg = "light blue",
        bg = "dark blue",
        font = "Helvetica 16 bold italic")
l1.pack()

# Images
dice = ['die1.png', 'die2.png', 'die3.png', 'die4.png', 'die5.png', 'die6.png']

# Simulating the dice with random numbers between 0 to 6 and generating image
image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))

# Construct a label widget for image
label1 = tkinter.Label(root, image=image1)
label1.image = image1

# packing a widget in the parent widget 
label1.pack( expand=True)

# function activated by button
def rolling_dice():
    image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    # update image
    label1.configure(image=image1)
    # keep a reference
    label1.image = image1


# adding button, and command will use rolling_dice function
button = tkinter.Button(root, text='ROLL', fg='blue', command=rolling_dice)

# pack a widget in the parent widget
button.pack( expand=True)

# call the mainloop of Tk
# keeps window open
root.mainloop()