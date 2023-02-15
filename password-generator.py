# basic flet template for replit
print("running password-generator.py")  # remind console which file is running

import flet as ft
import string
import random


def main(page: ft.Page):

    def generate_password(e):

        # All the possible characters in a password - letters, numbers and symbols
        password_chars = string.ascii_letters + string.digits + string.punctuation

        new_password = ""

        for n in range(int(slider_pw_length.value)):
            new_password += random.choice(password_chars)

        txt_generated_password.value = new_password
        page.update()

    def slider_changed(e):
        txt_password_length.value = f"Password length: {int(slider_pw_length.value)} characters"
        page.update()

    page.title = "Password Generator"

    page.add(ft.Text("Password generator"))

    slider_pw_length = ft.Slider(value=4,
                                 min=4,
                                 max=30,
                                 divisions=30 - 4,
                                 label="{value}",
                                 on_change=slider_changed)
    txt_password_length = ft.Text(
        value=f"password length: {slider_pw_length.value} characters")
    txt_generated_password = ft.TextField(value="password goes here",
                                          read_only=True)
    btn_generate = ft.FilledButton(text="Generate password",
                                   on_click=generate_password)

    page.add(slider_pw_length, txt_password_length, txt_generated_password,
             btn_generate)
    page.update()


ft.app(target=main, assets_dir="assets", view=ft.WEB_BROWSER)
