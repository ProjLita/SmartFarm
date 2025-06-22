import flet as ft

def smartfarm1(router_data=None):
    page = router_data.page
    is_dark = page.theme_mode == ft.ThemeMode.DARK


    # Cores
    bg_color = ft.Colors.BLACK if is_dark else ft.Colors.WHITE
    text_color = ft.Colors.WHITE if is_dark else ft.Colors.BLACK
    border_color = ft.Colors.GREY_700 if is_dark else ft.Colors.GREY_300

    # Card do gráfico
    chart_card = ft.Container(
        bgcolor=bg_color,
        padding=20,
        border_radius=15,
        shadow=ft.BoxShadow(
            color=ft.Colors.with_opacity(0.2, ft.Colors.BLACK) if not is_dark else ft.Colors.with_opacity(0.3, ft.Colors.WHITE),
            blur_radius=10,
            spread_radius=2,
            offset=ft.Offset(2, 4)
        ),
        content=ft.Column(
            spacing=10,
            controls=[
                ft.Text(
                    "Métricas da SmartFarm",
                    size=22,
                    weight=ft.FontWeight.BOLD,
                    color=text_color,
                    text_align=ft.TextAlign.CENTER
                ),
                ft.BarChart(
                    bar_groups=[
                        ft.BarChartGroup(x=0, bar_rods=[ft.BarChartRod(to_y=2, color=ft.Colors.GREEN_ACCENT, width=20)]),
                        ft.BarChartGroup(x=1, bar_rods=[ft.BarChartRod(to_y=3, color=ft.Colors.LIGHT_GREEN, width=20)]),
                        ft.BarChartGroup(x=2, bar_rods=[ft.BarChartRod(to_y=4, color=ft.Colors.LIME, width=20)]),
                        ft.BarChartGroup(x=3, bar_rods=[ft.BarChartRod(to_y=6, color=ft.Colors.YELLOW, width=20)]),
                        ft.BarChartGroup(x=4, bar_rods=[ft.BarChartRod(to_y=7, color=ft.Colors.ORANGE, width=20)]),
                        ft.BarChartGroup(x=5, bar_rods=[ft.BarChartRod(to_y=8, color=ft.Colors.AMBER, width=20)]),
                    ],
                    border=ft.border.all(1, border_color),
                    left_axis=ft.ChartAxis(
                        labels_size=30,
                        title=ft.Text("Crescimento", size=12, weight=ft.FontWeight.BOLD, color=text_color),
                    ),
                    bottom_axis=ft.ChartAxis(
                        labels=[
                            ft.ChartAxisLabel(value=0, label=ft.Text("Jan", color=text_color)),
                            ft.ChartAxisLabel(value=1, label=ft.Text("Fev", color=text_color)),
                            ft.ChartAxisLabel(value=2, label=ft.Text("Mar", color=text_color)),
                            ft.ChartAxisLabel(value=3, label=ft.Text("Abr", color=text_color)),
                            ft.ChartAxisLabel(value=4, label=ft.Text("Mai", color=text_color)),
                            ft.ChartAxisLabel(value=5, label=ft.Text("Jun", color=text_color)),
                        ],
                        labels_size=30,
                    ),
                    max_y=10,
                    animate=True,
                    interactive=False,
                )
            ]
        )
    )

    back_button = ft.IconButton(icon=ft.Icons.ARROW_BACK, on_click=lambda e: page.go("/"))

    primavera = ft.Container(
    content=ft.Column(
        controls=[
            ft.Text(
                "Primavera", 
                size=24, 
                weight=ft.FontWeight.BOLD,
                color=ft.Colors.BLACK
            ),
            ft.Text(
                "3", 
                size=40, 
                weight=ft.FontWeight.BOLD,
                color=ft.Colors.BLACK
            )
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=-6
    ),
    expand=True,
    height=120,
    bgcolor=ft.Colors.PINK_100,
    border_radius=10,
    alignment=ft.alignment.center,
)
    verao = ft.Container(
    content=ft.Column(
        controls=[
            ft.Text(
                "Verão", 
                size=24, 
                weight=ft.FontWeight.BOLD,
                color=ft.Colors.BLACK
            ),
            ft.Text(
                "2", 
                size=40, 
                weight=ft.FontWeight.BOLD,
                color=ft.Colors.BLACK
            )
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=-6
    ),
    expand=True,
    height=120,
    bgcolor=ft.Colors.RED_100,
    border_radius=10,
    alignment=ft.alignment.center,
)
    outono = ft.Container(
    content=ft.Column(
        controls=[
            ft.Text(
                "Outono", 
                size=24, 
                weight=ft.FontWeight.BOLD,
                color=ft.Colors.BLACK
            ),
            ft.Text(
                "0", 
                size=40, 
                weight=ft.FontWeight.BOLD,
                color=ft.Colors.BLACK
            )
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=-6
    ),
    expand=True,
    height=120,
    bgcolor=ft.Colors.ORANGE_100,
    border_radius=10,
    alignment=ft.alignment.center,
)
    inverno = ft.Container(
    content=ft.Column(
        controls=[
            ft.Text(
                "Inverno", 
                size=24, 
                weight=ft.FontWeight.BOLD,
                color=ft.Colors.BLACK
            ),
            ft.Text(
                "1", 
                size=40, 
                weight=ft.FontWeight.BOLD,
                color=ft.Colors.BLACK
            )
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=-6
    ),
    expand=True,
    height=120,
    bgcolor=ft.Colors.BLUE_100,
    border_radius=10,
    alignment=ft.alignment.center,
)



    minha_plant= ft.Container(
                    content=ft.Row(
                        controls=[
                            ft.Container(
                                width=1,
                                height=70,
                                bgcolor=ft.Colors.GREY,
                            ),
                            ft.Column(
                                controls=[
                                    ft.Text("Morango", weight=ft.FontWeight.BOLD, size=30),
                                    ft.Text("Fragaria", size=16,)
                                ],
                                alignment=ft.MainAxisAlignment.CENTER,
                                spacing=-2
                            ),
                            ft.Icon(
                                name=ft.Icons.KEYBOARD_ARROW_RIGHT,
                                size=30
                            )
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                        spacing=50
                    ),
                    expand=True,
                    height=110,
                    border=ft.border.all(2, ft.Colors.GREY_200),
                    border_radius=10,
                    alignment=ft.alignment.center,
                    on_click=lambda e: e.page.go("/plantacao")
                )

    editar_farm = ft.ElevatedButton(
        "Editar SmartFarm",
        color=ft.Colors.WHITE,
        bgcolor=ft.Colors.GREEN_400,
        expand=True,
        height=45,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=40)),
    )

    camera = ft.Container(
        content=ft.Column(   
            controls=[
                ft.IconButton(
                icon=ft.Icons.PLAY_CIRCLE_OUTLINE,
                icon_size=40
                ),
            ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),    
        expand=True,
        height=120,
        bgcolor=ft.Colors.GREY_300,
        border_radius=10,
        alignment=ft.alignment.center,
    )

    return ft.Column(
        spacing=30,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[
            ft.Row(
                controls=[
                back_button,
                ft.Text(
                "SmartFarm 1 - Visão Geral",
                size=20,
                weight=ft.FontWeight.BOLD,
                text_align=ft.TextAlign.CENTER
                    )
                ],
            ),
            chart_card,
            ft.Column(
                controls=[
                    ft.Text(
                        "Minha plantação",
                        weight=ft.FontWeight.BOLD,
                        size=20
                    ),
                    minha_plant 
                ]
                
            ),
            ft.Column(
                controls=[
                    ft.Text(
                        "Total de colheitas feitas",
                        weight=ft.FontWeight.BOLD,
                        size=20
                    ),
                    ft.Row(
                        controls=[
                            primavera,
                            verao
                        ],
                        spacing=20
                    ),
                    ft.Row(
                        controls=[
                            outono,
                            inverno
                        ],
                        spacing=20
                    )
                ]
            ),
            ft.Column(
                controls=[
                    ft.Text(
                        "Câmera ao vivo",
                        weight=ft.FontWeight.BOLD,
                        size=20
                    ),
                    camera,
                ],
                spacing=10,
            ),
            ft.Row(
                controls=[
                    editar_farm
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            )                  
        ],
        alignment=ft.MainAxisAlignment.CENTER
    )