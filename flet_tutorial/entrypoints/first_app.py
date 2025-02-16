import flet as ft
from first_python_app.main import main


def run():
    ft.app(target=main, view=ft.AppView.WEB_BROWSER)
