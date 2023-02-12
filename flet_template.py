# basic flet template for replit
print("running flet_template.py") # remind console which file is running

import flet as ft

def main(page: ft.Page):
    page.title = "My App"
    page.vertical_alignment = "CENTER"

    page.add(ft.Text("hello world"))
    page.add(ft.Image(src="/images/flet.png"))
    
    

ft.app(target=main, assets_dir="assets", view=ft.WEB_BROWSER)
