import flet as ft
from views.smartfarm1 import smartfarm1


def IndexView(page: ft.Page):
    page.scroll = ft.ScrollMode.AUTO
    page.padding = ft.padding.symmetric(horizontal=50)

    # Botão Minha SmartFarm
    smartfarm_button = ft.ElevatedButton(
        "Minha SF 1",
        expand=True,
        height=120,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=15)),
        on_click=lambda e: e.page.go("/smartfarm1")
    )
    smartfarm_button_2 = ft.ElevatedButton(
        "Minha SF 2",
        expand=True,
        height=120,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=15)),
    )
    add_smartfarm = ft.ElevatedButton(
        "Adicionar SmartFarm",
        expand=True,
        height=120,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=15)),
    )

    # Reservatórios
# Reservatório 1 com gradiente azul (75% forte, 25% fraco)
    reservatorio1 = ft.Container(
        gradient=ft.LinearGradient(
            begin=ft.alignment.top_center,
            end=ft.alignment.bottom_center,
            colors=[ft.Colors.BLUE_200, ft.Colors.BLUE_600],
            stops=[0.25, 0.75]
        ),
        border_radius=15,
        height=120,
        expand=True,
        content=ft.ElevatedButton(
            content=ft.Text("ALTO", size=24, weight=ft.FontWeight.BOLD),
            style=ft.ButtonStyle(
                color=ft.Colors.WHITE,
                bgcolor=ft.Colors.TRANSPARENT,
                shape=ft.RoundedRectangleBorder(radius=15),
            )
        )
    )
    # Reservatório 2 com gradiente (75% vermelho forte, 25% fraco)
    reservatorio2 = ft.Container(
        gradient=ft.LinearGradient(
            begin=ft.alignment.top_center,
            end=ft.alignment.bottom_center,
            colors=[ft.Colors.RED_200, ft.Colors.RED_400],
            stops=[0.65, 0.85]
        ),
        border_radius=15,
        height=120,
        expand=True,
        content=ft.ElevatedButton(
            content=ft.Text("BAIXO", size=24, weight=ft.FontWeight.BOLD),
            style=ft.ButtonStyle(
                color=ft.Colors.WHITE,
                bgcolor=ft.Colors.TRANSPARENT,
                shape=ft.RoundedRectangleBorder(radius=15),
            )
        )
    )

    # Umidade do Solo Alta (BOA) com gradiente
    umidade1 = ft.Container(
        gradient=ft.LinearGradient(
            begin=ft.alignment.top_center,
            end=ft.alignment.bottom_center,
            colors=[ft.Colors.BROWN_700,ft.Colors.BROWN_600],
            stops=[0.0, 0.85]
        ),
        border_radius=15,
        height=120,
        expand=True,
        content=ft.ElevatedButton(
            content=ft.Text("BOA", size=24, weight=ft.FontWeight.BOLD),
            style=ft.ButtonStyle(
                color=ft.Colors.WHITE,
                bgcolor=ft.Colors.TRANSPARENT,
                shape=ft.RoundedRectangleBorder(radius=15)
            )
        )
    )

    umidade2 = ft.Container(
        gradient=ft.LinearGradient(
            begin=ft.alignment.top_center,
            end=ft.alignment.bottom_center,
            colors=[ft.Colors.BROWN_300,ft.Colors.BROWN_400 ],
            stops=[0.0, 0.85]
        ),
        border_radius=15,
        height=120,
        expand=True,
        content=ft.ElevatedButton(
            content=ft.Text("Seca", size=24, weight=ft.FontWeight.BOLD),
            style=ft.ButtonStyle(
                color=ft.Colors.WHITE,
                bgcolor=ft.Colors.TRANSPARENT,
                shape=ft.RoundedRectangleBorder(radius=15)
            )
        )
    )
    # Nome das SmartFarms
    texto1 = ft.Container(
        content=ft.Text("Farm 1"),
        alignment=ft.alignment.center,
        expand=1
    )
    texto2 = ft.Container(
        content=ft.Text("Farm 2"),
        alignment=ft.alignment.center,
        expand=1
    )

    # Layout principal
    content = ft.Column(
        controls=[
            ft.Column(
                controls=[
                    ft.Text("Olá LITA", weight=ft.FontWeight.BOLD, size=30),
                    ft.Text("Minhas SmartFarms", weight=ft.FontWeight.BOLD, size=15)
                ]
            ),
            ft.Row(
                controls=[smartfarm_button, smartfarm_button_2],
                spacing=20,
                alignment=ft.MainAxisAlignment.CENTER
            ),
            ft.Row(
                controls=[add_smartfarm],
                alignment=ft.MainAxisAlignment.CENTER
            ),
            ft.Column(
                controls=[
                    ft.Text("Nível da água no reservatório", weight=ft.FontWeight.BOLD, size=15),
                    ft.Row(
                        controls=[reservatorio1, reservatorio2],
                        spacing=20
                    )
                ]
            ),
            ft.Row(controls=[texto1, texto2]),
            ft.Column(
                controls=[
                    ft.Text("Umidade do solo", weight=ft.FontWeight.BOLD, size=15),
                    ft.Row(
                        controls=[umidade1, umidade2],
                        spacing=20
                    )
                ]
            ),
            ft.Column(
                controls=[
                    ft.Text("Status da minha Farm", weight=ft.FontWeight.BOLD, size=15),
                    ft.Row(
                        controls=[],  # preencher futuramente
                        spacing=20
                    )
                ]
            )
        ]
    )

    return content
