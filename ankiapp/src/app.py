import flet as ft
from app_layout import AppLayout
from sidebar import Sidebar

class App(AppLayout):
    def __init__(self, page: ft.Page):
        self.page = page
        super().__init__()
        self.sidebar = Sidebar()
        # self.controls.append(self.sidebar)
        

    def initialize(self):
        self.page.views.append(
            ft.View(
                "/",
                [self.sidebar, self],
                padding=ft.padding.all(0),
                bgcolor=ft.Colors.BLUE_GREY_200,
            )
        )
        self.page.update()
        self.page.go("/")
