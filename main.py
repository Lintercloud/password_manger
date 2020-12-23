from tkinter import *
from tkinter import messagebox   # import *是指所有的class
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_entry.delete(0, END)

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)   #隨機選出8~10個字
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for letter in range(nr_letters)]
    password_symbols = [random.choice(symbols) for symbol in range(nr_symbols)]
    password_numbers = [random.choice(symbols) for number in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)  #將密碼打散

    password = "".join(password_list)  #用join將iterable結合為string
    password_entry.insert(0, password)
    pyperclip.copy(password)     #將密碼自動複製

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    web = web_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    if len(web) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty")
    else:
        sure_check = messagebox.askokcancel(title=web, message=f"These are the details entered: \nEmail:{email} \nPassword:{password} "
                                                  f"\nis it ok")     #最後確認資料是否執行
        if sure_check:
            with open("Password.csv", "a") as f:
                f.write(f"{web}  / {email}  / {password}\n")
                web_entry.delete(0, END)  # 資料填寫完後刪除app上的資料
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("password Manger")
window.config(padx=30, pady=30)

#canves logo
canves = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canves.create_image(100, 100, image=logo_img)
canves.grid(column=1, row=0)

#label
web_label = Label(text="Website: ")
web_label.grid(column=0, row=1)

email_label = Label(text="Email/Username: ")
email_label.grid(column=0, row=2)

password_label = Label(text="PASSWORD: ")
password_label.grid(column=0, row=3)

#Entry
web_entry = Entry(width=35)
web_entry.grid(column=1, row=1, columnspan=2)
web_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0,"123@gmail.com")

password_entry = Entry(width=26)
password_entry.grid(column=1, row=3)

#Button
password_button = Button(text="Generate", command=generate_password)
password_button.grid(column=2, row=3)

data_add_button = Button(width=36, text="Add", command=save_data)
data_add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()