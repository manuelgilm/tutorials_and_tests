import flet as ft
import random


def main(page: ft.Page):
    page.bgcolor = ft.colors.BLUE_GREY_800
    page.title = "Tabs in Flet"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    title = ft.Text(
        value="Tabs in Flet",
        size=24,
        color=ft.colors.WHITE,
        weight=ft.FontWeight.BOLD,
    )

    tabs = ft.Tabs(
        selected_index=0,
        animation_duration=300,
        tabs=[
            ft.Tab(text="Tasks", icon=ft.icons.LIST_ALT),
            ft.Tab(text="Profile", icon=ft.icons.PERSON),
            ft.Tab(text="Settings", icon=ft.icons.SETTINGS),
        ],
        expand=1,
    )

    page.add(title, tabs)
