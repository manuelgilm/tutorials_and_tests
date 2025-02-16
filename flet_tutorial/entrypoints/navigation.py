import flet as ft
from navigation.main import main


def run() -> None:
    ft.app(target=main, view=ft.AppView.WEB_BROWSER)
