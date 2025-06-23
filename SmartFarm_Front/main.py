import flet as ft
from views.routes import router
from controles.app_bar import NavBar

def main(page: ft.Page):

    page.theme_mode = "light"
    page.appbar = NavBar(page)
    page.on_route_change = router.route_change
    router.page = page
    page.add(
        router.body
    )
    page.go('/')
    page.padding = ft.padding.only(left=20, right=20, bottom=20)
    page.scroll = ft.ScrollMode.AUTO

ft.app(target=main, assets_dir="assets")