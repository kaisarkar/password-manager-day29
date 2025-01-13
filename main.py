from tkinter import *
from passwordGenerator import *
from tkinter import messagebox
import pyperclip
import json
BG_COLOUR = "White"



# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def show_password():
    password_input.delete(0, END)
    new_password = generate_random_password()
    password_input.insert(0, new_password)
    pyperclip.copy(new_password)
# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_data():
    get_website = web_input.get()
    get_email = email_input.get()
    get_password = password_input.get()


    if len(get_email) == 0 or len(get_password) == 0 or len(get_website) == 0:
        messagebox.showerror(title="Error", message="Please fill all the fields")
    else:
        is_ok = messagebox.askokcancel(title=get_website,
                                           message=f"These are the details: \nEmail: {get_email} \nPassword: {get_password} \nIs that OK?")
        if is_ok:
            with open("data.txt", "a") as file:
                file.write(f"{get_website} | {get_email} | {get_password}\n")
                web_input.delete(0, END)
                email_input.delete(0, END)
                password_input.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20, bg = BG_COLOUR)

canvas = Canvas(width=200, height=200,  highlightthickness=0, bg=BG_COLOUR)
password_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image= password_img)
canvas.grid(column=1, row=0)


web_name = Label(text="Website: ", fg="black", bg=BG_COLOUR)
web_name.grid(column=0, row=1)
web_input = Entry(width=35, bg=BG_COLOUR)
web_input.grid(column=1, row=1, columnspan=2)

email = Label(text="Email/ Username: ", fg="black", bg=BG_COLOUR)
email.grid(column=0, row=2)
email_input = Entry(width=35, bg=BG_COLOUR)
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(0, "info@sarkar.uk")

password = Label(text="Password: ", fg="black", bg=BG_COLOUR)
password.grid(column=0, row=3)
password_input = Entry(width=17, bg=BG_COLOUR)
password_input.grid(column=1, row=3)

generated_passwords_btn = Button(text="Generate Password", command=show_password)
generated_passwords_btn.grid(column=2, row=3)

add_btn = Button(text="Add Password", fg="black", width=32, command=save_data)
add_btn.grid(column=1, row=4, columnspan=2)

window.mainloop()