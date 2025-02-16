import flet as ft


def main(page: ft.Page):
    page.title = "Sticky Notes"
    page.padding = 20
    page.theme_mode = "light"
    page.bgcolor = ft.colors.BLUE_GREY_800

    def add_note(e):
        new_note = create_note("New note")
        grid.controls.append(new_note)
        page.update()

    def delete_note(note):
        grid.controls.remove(note)
        page.update()

    def create_note(text):
        note_content = ft.TextField(
            value=text, multiline=True, bgcolor=ft.colors.BLUE_GREY_50
        )
        note = ft.Container(
            content=ft.Column(
                [
                    note_content,
                    ft.IconButton(
                        icon=ft.icons.DELETE, on_click=lambda _: delete_note(note)
                    ),
                ]
            ),
            bgcolor=ft.colors.BLUE_GREY_100,
            padding=10,
            border_radius=10,
            width=200,
            height=200,
        )
        return note

    grid = ft.GridView(
        expand=True,
        max_extent=220,
        child_aspect_ratio=1,
        spacing=10,
        run_spacing=10,
    )
    notes = [
        create_note("My first note"),
        create_note("My second note"),
        create_note("My third note"),
    ]
    for note in notes:
        grid.controls.append(note)

    page.add(
        ft.Row(
            [
                ft.Text(
                    value="Sticky Notes", size=24, color=ft.colors.WHITE, weight="bold"
                ),
                ft.IconButton(
                    icon=ft.icons.ADD, on_click=add_note, icon_color=ft.colors.WHITE
                ),
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        ),
        grid,
    )
