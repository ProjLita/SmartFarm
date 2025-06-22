import flet as ft
from views.smartfarm1 import smartfarm1


def IndexView(page: ft.Page):
    page.scroll = ft.ScrollMode.AUTO,
    page.padding = ft.padding.symmetric(horizontal=50)

    # Botão Minha SmartFarm
    smartfarm_button = ft.ElevatedButton(
        "Minha SmartFarm 1",
        expand=True,
        height=120,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=15)),
        on_click=lambda e: e.page.go("/smartfarm1")
    )
    smartfarm_button_2 = ft.ElevatedButton(
        "Minha SmartFarm 2",
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
    reservatorio1 = ft.ElevatedButton(
    content=ft.Text(
        "ALTO", 
        size=24, 
        weight=ft.FontWeight.BOLD
        ),
    color=ft.Colors.BLUE_500,
    bgcolor=ft.Colors.BLUE_200,
    expand=True,
    height=120,
    style=ft.ButtonStyle(
        shape=ft.RoundedRectangleBorder(radius=15)
        ),
    )
    reservatorio2 = ft.ElevatedButton(
       content=ft.Text( 
        "BAIXO",
        size=24,
        weight=ft.FontWeight.BOLD,
       ),
        color=ft.Colors.RED_400,
        bgcolor=ft.Colors.RED_200,
        expand=True,
        height=120,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=15)
        ),
    )

    # Umidade do solo
    umidade1 = ft.ElevatedButton(
       content=ft.Text( 
        "BOA",
        size=24,
        weight=ft.FontWeight.BOLD
       ),
        color=ft.Colors.WHITE60,
        bgcolor=ft.Colors.BROWN_500,
        expand=True,
        height=120,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=15)
        ),
    )
    umidade2 = ft.ElevatedButton(
       content=ft.Text( 
        "Regular",
        size=24,
        weight=ft.FontWeight.BOLD
       ),
        color=ft.Colors.WHITE60,
        bgcolor=ft.Colors.BROWN_200,
        expand=True,
        height=120,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=15)
        ),
    )

    # Só o nome de cada reservatório
    texto1=ft.Container(
        content=ft.Text("SmartFarm 1"),
        alignment=ft.alignment.center,
        expand=1 
    )
    texto2=ft.Container(
        content=ft.Text("SmartFarm 2"),
        alignment=ft.alignment.center,
        expand=1 
    )

   
    content = ft.Column(
        controls=[
            ft.Column(
                controls=[
                    ft.Text("Olá LITA", weight=ft.FontWeight.BOLD, size=30),
                    ft.Text("Minhas SmartFarms", weight=ft.FontWeight.BOLD, size=15)
                ],
            ),
            ft.Row(
                controls=[
                    smartfarm_button,
                    smartfarm_button_2
                ],
                spacing=20,
                alignment=ft.MainAxisAlignment.CENTER
            ),
            ft.Row(
                controls=[
                    add_smartfarm
                ],
                alignment=ft.MainAxisAlignment.CENTER
            ),
            ft.Column(   
                controls=[
                    ft.Text("Nível da água no reservatório", weight=ft.FontWeight.BOLD, size=15),
                    ft.Row( 
                            controls=[
                                reservatorio1,
                                reservatorio2,
                            ],
                            spacing=20
                        )   
                ],
            ),
            ft.Row(
                controls=[
                texto1,
                texto2
                ],
            ),
            ft.Column(
                controls=[
                    ft.Text("Umidade do solo", weight=ft.FontWeight.BOLD, size=15),
                    ft.Row( 
                        controls=[
                            umidade1,
                            umidade2
                        ],
                        spacing=20
                    )
                ]
            ),
            ft.Row(
                controls=[
                texto1,
                texto2
            ],
            ) ,
            ft.Column(   
                controls=[
                    ft.Text("Status da minha Farm", weight=ft.FontWeight.BOLD, size=15),
                    ft.Row(  
                            controls=[
                                
                            ],
                            spacing=20
                        )   
                    ],
                ),
            ]
        )


    
    return content