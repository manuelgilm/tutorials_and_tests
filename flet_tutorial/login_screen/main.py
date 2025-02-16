import flet as ft
from flet import TextField
from flet import Checkbox
from flet import ElevatedButton
from flet import Text
from flet import Row
from flet import Column
from flet_core.control_event import ControlEvent


def main(page: ft.Page) -> None:
    page.title = "Signup"
    page.vertical_aligment = ft.MainAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window_width = 400
    page.window_height = 400
    page.window_resizable = True

    # setup fields
    text_username: TextField = TextField(
        label="Username", text_align=ft.TextAlign.LEFT, width=200
    )
    text_password: TextField = TextField(
        label="Password", text_align=ft.TextAlign.LEFT, width=200, password=True
    )
    checkbox_signup: Checkbox = Checkbox(label="I agree to stuff", value=False)
    button_submit: ElevatedButton = ElevatedButton(
        text="Sign Up", width=200, disabled=True
    )

    # setup event handlers
    def validate(e: ControlEvent) -> None:
        if all([text_username.value, text_password.value, checkbox_signup.value]):
            button_submit.disabled = False
        else:
            button_submit.disabled = True

        page.update()

    def submit(e: ControlEvent) -> None:
        print(f"Username: {text_username.value}")
        print(f"Password: {text_password.value}")

        page.clean()
        page.add(
            Row(
                controls=[Text(value=f"Welcome : {text_username.value}", size=20)],
                alignment=ft.MainAxisAlignment.CENTER,
            )
        )

    checkbox_signup.on_change = validate
    text_username.on_change = validate
    text_password.on_change = validate
    button_submit.on_click = submit

    # Render the page sign-up page
    page.add(
        Row(
            controls=[
                Column([text_username, text_password, checkbox_signup, button_submit])
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )
