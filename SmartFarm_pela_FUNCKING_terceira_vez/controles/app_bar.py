import flet as ft

def NavBar(page):
    page.scroll = ft.ScrollMode.AUTO
    # Função para alternar tema claro/escuro
    def toggle_dark_mode(e):
        if page.theme_mode == "dark":
            page.theme_mode = "light"
        else:
            page.theme_mode = "dark"
        page.update()

    NavBar = ft.AppBar(
        actions=[
            ft.IconButton(
                icon=ft.Icons.WB_SUNNY_OUTLINED,
                tooltip="Alternar Tema",
                on_click=toggle_dark_mode
            ),
            ft.IconButton(
                icon=ft.Icons.HOME,
                tooltip="Home",
                on_click=lambda _: page.go('/')
            ),
            ft.IconButton(
                icon=ft.Icons.SETTINGS_ROUNDED,
                tooltip="Configurações",
                on_click=lambda _: page.go('/settings')
            )
        ]
    )

    return NavBar
