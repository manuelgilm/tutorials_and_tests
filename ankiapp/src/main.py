import flet as ft
from app import App


def main(page: ft.Page):
    page.title = "Anki-like App"
    app = App(page=page)
    page.add(app)
    page.update()
    app.initialize()



ft.app(target = main)
