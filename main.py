from tkinter import *
from passwordGenerator import generated_passwords
BG_COLOUR = "White"



# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20, bg = BG_COLOUR)

canvas = Canvas(width=200, height=200,  highlightthickness=0, bg=BG_COLOUR)
password_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image= password_img)
canvas.grid(column=1, row=1)





window.mainloop()