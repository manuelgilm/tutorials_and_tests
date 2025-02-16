import flet as ft


def create_product(name, price, color):
    product = ft.Container(
        content=ft.Column(
            [
                ft.Text(
                    value=name,
                    size=16,
                    color=ft.colors.WHITE,
                    weight=ft.FontWeight.BOLD,
                ),
                ft.Text(value=f"${price}", size=14),
                ft.ElevatedButton(text="Add to cart", color=ft.colors.WHITE),
            ]
        ),
        bgcolor=color,
        border_radius=10,
        padding=20,
        alignment=ft.alignment.center,
    )
    return product


def main(page: ft.Page):
    page.title = "Galeria de Productos"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = ft.colors.BLUE_GREY_900
    title = ft.Text(
        value="Galeria de Productos",
        size=32,
        color=ft.colors.WHITE,
        weight=ft.FontWeight.BOLD,
    )
    products = [
        create_product(name="Laptop", price=1000, color=ft.colors.BLUE_GREY_800),
        create_product(name="Smartphone", price=500, color=ft.colors.BLUE_GREY_700),
        create_product(name="Tablet", price=300, color=ft.colors.BLUE_GREY_600),
        create_product(name="Smartwatch", price=200, color=ft.colors.BLUE_GREY_500),
    ]
    galeria = ft.ResponsiveRow(
        [
            ft.Container(product, col={"sm": 12, "md": 6, "lg": 3})
            for product in products
        ],
    )
    content = ft.Column(
        [title, ft.Divider(height=20, color=ft.colors.WHITE24), galeria],
        spacing=20,
        scroll=ft.ScrollMode.AUTO,
        expand=True,
    )
    page.add(content)
