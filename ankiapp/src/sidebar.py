import flet as ft


class Sidebar(ft.Container):
    def __init__(self):
        self.nav_rail_visible = True
        self.top_nav_items = [
            ft.NavigationRailDestination(
                label_content=ft.Text("Decks"),
                label="Decks",
                icon=ft.Icons.BOOK_OUTLINED,
                selected_icon=ft.Icons.BOOK_OUTLINED,
            ),
            ft.NavigationRailDestination(
                label_content=ft.Text("Progress"),
                label="Progress",
                icon=ft.Icons.PERSON,
                selected_icon=ft.Icons.PERSON,
            ),
        ]

        self.top_nav_rail = ft.NavigationRail(
            selected_index=None,
            label_type=ft.NavigationRailLabelType.ALL,
            on_change=self.top_nav_change,
            destinations=self.top_nav_items,
            bgcolor=ft.Colors.BLUE_GREY,
            extended=True,
            height=110,
        )

        self.bottom_nav_rail = ft.NavigationRail(
            selected_index=None,
            label_type=ft.NavigationRailLabelType.ALL,
            on_change=self.bottom_nav_change,
            extended=True,
            expand=True,
            bgcolor=ft.Colors.BLUE_GREY,
        )
        self.toggle_nav_rail_button = ft.IconButton(ft.Icons.ARROW_BACK)

        super().__init__(
            content=ft.Column(
                [
                    ft.Row(
                        [
                            ft.Text("Workspace"),
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    ),
                    # divider
                    ft.Container(
                        bgcolor=ft.Colors.BLACK26,
                        border_radius=ft.border_radius.all(30),
                        height=1,
                        alignment=ft.alignment.center_right,
                        width=220,
                    ),
                    self.top_nav_rail,
                    # divider
                    ft.Container(
                        bgcolor=ft.Colors.BLACK26,
                        border_radius=ft.border_radius.all(30),
                        height=1,
                        alignment=ft.alignment.center_right,
                        width=220,
                    ),
                    self.bottom_nav_rail,
                ],
                tight=True,
            ),
            padding=ft.padding.all(15),
            margin=ft.margin.all(0),
            width=250,
            bgcolor=ft.Colors.BLUE_GREY,
            visible=self.nav_rail_visible,
        )



    def top_nav_change(self, e):
        index = e if (type(e) == int) else e.control.selected_index
        self.bottom_nav_rail.selected_index = None
        self.top_nav_rail.selected_index = index
        if index == 0:
            self.page.route = "/boards"
        elif index == 1:
            self.page.route = "/members"
        self.page.update()

    def bottom_nav_change(self, e):
        index = e if (type(e) == int) else e.control.selected_index
        self.top_nav_rail.selected_index = None
        self.bottom_nav_rail.selected_index = index
        self.page.route = f"/board/{index}"
        self.page.update()        