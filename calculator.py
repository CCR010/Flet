## not complete yet

import flet as ft


def main(page: ft.Page):
    page.title = "Calc App"
    result = ft.Text(value="0", size=30)

    page.add(
        ft.Container(
            width=300,
            padding=10,
            bgcolor=ft.colors.BLACK,
            border_radius=ft.border_radius.all(20),
            border=ft.border.all(width=1, color=ft.colors.WHITE),
            content=ft.Column(controls=[
                #start column
                ft.Row(controls=[result], alignment="END"),
                ft.Row(controls=[
                    ft.ElevatedButton(text="AC", expand=True),
                    ft.ElevatedButton(text="+/-", expand=True),
                    ft.ElevatedButton(text="%", expand=True),
                    ft.ElevatedButton(text="/", expand=True),
                ]),  # end row
                ft.Row(controls=[
                    ft.ElevatedButton(text="7", expand=True),
                    ft.ElevatedButton(text="8", expand=True),
                    ft.ElevatedButton(text="9", expand=True),
                    ft.ElevatedButton(text="*", expand=True),
                ]),  # end row
                ft.Row(controls=[
                    ft.ElevatedButton(text="4", expand=True),
                    ft.ElevatedButton(text="5", expand=True),
                    ft.ElevatedButton(text="6", expand=True),
                    ft.ElevatedButton(text="-", expand=True),
                ]),  # end row
                ft.Row(controls=[
                    ft.ElevatedButton(text="1", expand=True),
                    ft.ElevatedButton(text="2", expand=True),
                    ft.ElevatedButton(text="3", expand=True),
                    ft.ElevatedButton(text="+", expand=True),
                ]),  # end row
                ft.Row(controls=[
                    ft.ElevatedButton(text="0", expand=True),
                    ft.ElevatedButton(text=".", expand=True),
                    ft.ElevatedButton(text="=", expand=True),
                ]),  # end row
            ])  #end column
        )  #end container
    )  # end page.add

    

ft.app(target=main, view=ft.WEB_BROWSER)
