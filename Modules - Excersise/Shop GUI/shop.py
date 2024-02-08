from tkinter import Button
from helpers import clean_screen
from canvas import frame, root
from json import load, dump
from PIL import ImageTk, Image



def display_products():
    clean_screen()
    display_stock()

def display_stock():
    with open("db/products.json", "r") as stock:
        info = load(stock)

    x, y = 150, 50

    for item_name, item_info in info.items():
        pillow_image = Image.open(item_info["image"])
        resize_pillow_image = pillow_image.resize((100, 100))
        item_img = ImageTk.PhotoImage(resize_pillow_image)
        images.append(item_img)

        frame.create_text(x, y, text=item_name, font=("Comic Sans MS", 15))
        frame.create_image(x, y + 100, image=item_img)

        if item_info["quantity"] > 0:
            color = 'green'
            text = f"in Stock: {item_info['quantity']}"

            item_button = Button(
                root,
                text="Buy",
                bg='green',
                fg='white',
                font=("Comic Sans MS", 13),
                width=50,
                command=lambda x=item_name, y=info: buy_product(x, y)
            )

            frame.create_window(x, y + 220, width=80, height=28, window=item_button)
        else:
            color = 'red'
            text = 'Out of Stock'

        frame.create_text(x, y + 180, text=text, fill=color, font=("Comic Sans MS", 14))


        x += 200

        if x >= 650:
            y += 270
            x = 150


def buy_product(product_name, info):
    info[product_name]["quantity"] -= 1

    with open("db/products.json", "w") as stock:
        dump(info, stock)

    display_products()



images = []