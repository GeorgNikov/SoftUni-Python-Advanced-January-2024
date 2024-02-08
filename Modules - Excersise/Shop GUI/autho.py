from tkinter import Button, Entry
from canvas import root, frame
from helpers import clean_screen, get_password_hash
from json import dump, loads
from shop import display_products


def get_users_data():
    info_data = []

    with open("db/user_information.txt", "r") as user_file:
        for line in user_file:
            info_data.append(loads(line))

    return info_data


def render_entry():
    register_button = Button(
        root,
        text="Register",
        bg="green",
        fg="white",
        bd=0,
        width=90,
        height=40,
        command=register
    )

    login_button = Button(
        root,
        text='Login',
        bg='blue',
        fg='white',
        bd=0,
        width=90,
        height=40,
        command=login
    )

    frame.create_window(50, 20, height=35, width=120, window=register_button)
    frame.create_window(50, 50, height=35, width=120, window=login_button)


def register():
    clean_screen()

    frame.create_text(100, 50, text="First Name: ")
    frame.create_text(100, 100, text="Last Name: ")
    frame.create_text(100, 150, text="Username: ")
    frame.create_text(100, 200, text="Password: ")

    frame.create_window(200, 50, height=22,  window=first_name_box)
    frame.create_window(200, 100, window=last_name_box)
    frame.create_window(200, 150, window=username_box)
    frame.create_window(200, 200, window=password_box)

    register_button = Button(
        root,
        text="Register",
        bg="green",
        fg="white",
        bd=0,
        command=registration
    )

    frame.create_window(200, 250, height=30, width=120,  window=register_button)


def registration():
    info_dict = {
        "First name": first_name_box.get(),
        "Last name": last_name_box.get(),
        "Username": username_box.get(),
        "Password": password_box.get(),
    }

    if check_registration(info_dict):
        with open("db/user_information.txt", "a") as user_files:
            info_dict["Password"] = get_password_hash(info_dict["Password"])
            dump(info_dict, user_files)
            user_files.write("\n")


def check_registration(info_dict):
    frame.delete("error")

    for key, value in info_dict.items():
        if not value.strip():
            frame.create_text(
                200,
                300,
                text=f"{key} cannot be entry!",
                fill='red',
                tags='error',
            )

            return False

    users_data = get_users_data()

    for user in users_data:
        if user["Username"] == info_dict["Username"]:
            frame.create_text(
                200,
                300,
                text=f"{info_dict["Username"]} is already taken!",
                fill='red',
                tags='error',
            )
            return False

    return True


def login():
    clean_screen()

    frame.create_text(100, 50, text="Username")
    frame.create_text(100, 100, text="password")

    frame.create_window(200, 50, window=username_box)
    frame.create_window(200, 100, window=password_box)

    frame.create_window(200, 150, height=22, width=80, window=login_button)


def logging():
    frame.delete("error")
    if check_logging():
        display_products()
    else:
        frame.create_text(
            200,
            200,
            text="Invalid username or password",
            fill="red",
            tags="error"
        )


def check_logging():

    users_data = get_users_data()

    user_username = username_box.get()
    user_password = get_password_hash(password_box.get())

    for user in users_data:
        current_user_username = user["Username"]
        current_user_password = user["Password"]

        if current_user_username == user_username and current_user_password == user_password:
            return True

    return False


def change_login_button(event):
    info = [
        username_box.get(),
        password_box.get(),
    ]

    for el in info:
        if not el.strip():
            login_button["state"] = "disabled"
            break
    else:
        login_button["state"] = "normal"


first_name_box = Entry(root, bd=0)
last_name_box = Entry(root, bd=0)
username_box = Entry(root, bd=0)
password_box = Entry(root, bd=0, show="*")


login_button = Button(
    root,
    text="Login",
    bg="green",
    fg='white',
    bd=0,
    command=logging
)

login_button["state"] = "disabled"

root.bind("<KeyRelease>", change_login_button)
