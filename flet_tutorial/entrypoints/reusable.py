import flet as ft
from reusable_components.main import main


def run():
    ft.app(target=main, view=ft.AppView.WEB_BROWSER)
