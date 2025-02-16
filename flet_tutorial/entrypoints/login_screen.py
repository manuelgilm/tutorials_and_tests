from login_screen.main import main 
import flet as ft

def run():
    ft.app(target = main, view = ft.AppView.WEB_BROWSER)
