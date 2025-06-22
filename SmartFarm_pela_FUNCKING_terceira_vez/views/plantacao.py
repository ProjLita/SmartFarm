
import flet as ft

def ProfileView(router_data=None):
     
    saude = ft.Column(
                [
                ft.Text("Saúde", weight=ft.FontWeight.BOLD, size=17),
                ft.Text("Sua plantação precisa de fertilizante", size=13, color="orange"),
                ],
                spacing=-2
            )
    ambiente = ft.Column(
                    [
                    ft.Text("Ambiente", weight=ft.FontWeight.BOLD, size=17),
                    ft.Text("Adequado", size=13, color=ft.Colors.GREY,),
                    ],
                    spacing=-2
                )
    colheita = ft.Column(
                    [
                    ft.Text("Colheita", weight=ft.FontWeight.BOLD, size=17),
                    ft.Text("Data prevista em 2 dias", size=13, color=ft.Colors.GREY),
                    ],
                    spacing=-2
                )
    umidade = ft.Column(
                    [
                    ft.Text("Umidade do solo", weight=ft.FontWeight.BOLD, size=17),
                    ft.Text("Adequada (72%)", size=13, color=ft.Colors.GREY),
                    ],
                    spacing=-2
                )
    data_plantio = ft.Column(
                    [
                    ft.Text("Data de plantio", weight=ft.FontWeight.BOLD, size=17),
                    ft.Text("24 de dez. de 2024", size=13, color=ft.Colors.GREY),
                    ]
                    ,spacing=-2
                )
    editar = ft.ElevatedButton(
                        "Editar plantação",
                        style=ft.ButtonStyle(
                            bgcolor=ft.LinearGradient(
                                begin=ft.alignment.center_left,
                                end=ft.alignment.center_right,
                                colors=["#00FF88", "#FFD600"],
                            ),
                            color="black",
                            shape=ft.RoundedRectangleBorder(radius=20),
                            padding=20,
                        ),
                    )
    back_button = ft.IconButton(icon=ft.Icons.ARROW_BACK, on_click=lambda e: e.page.go("/smartfarm1"))

    content=ft.Column(  
                controls=[
                    ft.Row(
                    controls=[back_button],
                    alignment=ft.MainAxisAlignment.START
                    ),
                    ft.Text("Morango", size=24, weight=ft.FontWeight.BOLD),
                    ft.Text("Fragaria", size=14, color=ft.Colors.GREY),
                    ft.Divider(),
                    ft.Row(
                        controls=[
                            ft.Icon(ft.Icons.HEALTH_AND_SAFETY, color="orange"),
                            saude,
                            ft.Icon(ft.Icons.INFO_OUTLINE, color="orange", size=16),
                        ],
                        alignment=ft.MainAxisAlignment.START,
                    ),
                    ft.Row(
                        controls=[
                            ft.Icon(ft.Icons.ECO_OUTLINED),
                            ambiente
                        ],                   
                    ),
                    ft.Row(
                        controls=[
                            ft.Icon(ft.Icons.CALENDAR_MONTH_OUTLINED),
                            colheita
                        ],
                    ),
                    ft.Row(
                        controls=[
                            ft.Icon(ft.Icons.OPACITY),
                            umidade
                        ],
                    ),
                    ft.Row(
                        controls=[
                            ft.Icon(ft.Icons.EVENT_AVAILABLE_OUTLINED),
                            data_plantio
                        ],
                    ),
                    #editar
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20
            )       
        


    return content 
