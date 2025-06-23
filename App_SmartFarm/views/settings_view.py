import flet as ft
import threading
import serial
from serial.tools import list_ports
import time
import requests
import cv2
import numpy as np
import base64

# Configurações
BLUETOOTH_BAUDRATE = 9600
ESP32_CAM_STREAM_URL = "http://192.168.4.1:81/stream"

def list_available_ports():
    ports = []
    for port in list_ports.comports():
        ports.append(port.device)
    return ports

def BluetoothView(router_data=None):
    page = router_data.page  # Acesso à página
    stop_threads = threading.Event()
    ser = None


    # Widgets
    arduino_data = ft.Text("Aguardando dados do Arduino...", size=16)
    img = ft.Image(width=400, height=300, fit=ft.ImageFit.CONTAIN)
    btn_bt = ft.ElevatedButton("Conectar Bluetooth")
    btn_cam = ft.ElevatedButton("Iniciar Stream")
    status = ft.Text("Status: Pronto", size=12, color=ft.Colors.BLUE)
    port_dropdown = ft.Dropdown(
        label="Porta Bluetooth",
        options=[ft.dropdown.Option(port) for port in list_available_ports()],
        width=200
    )

    # Variáveis de controle de threads
    bt_thread = None
    cam_thread = None

    # ========== Funções ==========
    def bluetooth_reader():
        nonlocal ser
        try:
            selected_port = port_dropdown.value
            status.value = f"Tentando conectar na porta {selected_port}..."
            page.update()

            ser = serial.Serial(
                port=selected_port,
                baudrate=BLUETOOTH_BAUDRATE,
                timeout=1,
                write_timeout=1
            )

            ser.write(b'AT\r\n')
            time.sleep(1)

            if ser.in_waiting:
                response = ser.readline().decode(errors="ignore").strip()
                status.value = "Bluetooth conectado!" if response else "Conectado, sem resposta."
            else:
                status.value = "Bluetooth aguardando dados..."

            page.update()

            while not stop_threads.is_set():
                if ser.in_waiting:
                    line = ser.readline().decode(errors="ignore").strip()
                    if line:
                        arduino_data.value = f"Dado do Arduino: {line}"
                        page.update()
                time.sleep(0.1)

        except serial.SerialException as e:
            status.value = f"Erro na conexão: {str(e)}"
            page.update()
        except Exception as e:
            status.value = f"Erro inesperado: {str(e)}"
            page.update()
        finally:
            if ser and ser.is_open:
                try:
                    ser.close()
                except:
                    pass

    def update_ports():
        available_ports = list_available_ports()
        port_dropdown.options = [ft.dropdown.Option(port) for port in available_ports]
        if available_ports:
            port_dropdown.value = available_ports[0]
        page.update()

    def camera_streamer():
        try:
            stream = requests.get(ESP32_CAM_STREAM_URL, stream=True, timeout=5)
            bytes_ = b""
            for chunk in stream.iter_content(chunk_size=1024):
                if stop_threads.is_set():
                    break
                bytes_ += chunk
                a = bytes_.find(b'\xff\xd8')
                b = bytes_.find(b'\xff\xd9')
                if a != -1 and b != -1:
                    jpg = bytes_[a:b+2]
                    bytes_ = bytes_[b+2:]
                    frame = cv2.imdecode(np.frombuffer(jpg, dtype=np.uint8), cv2.IMREAD_COLOR)
                    if frame is not None:
                        _, buffer = cv2.imencode('.jpg', frame)
                        img.src_base64 = base64.b64encode(buffer).decode()
                        page.update()
        except Exception as e:
            status.value = f"Erro no stream: {e}"
            page.update()

    # ========== Handlers ==========
    def on_bt_click(e):
        nonlocal bt_thread
        if bt_thread and bt_thread.is_alive():
            stop_threads.set()
            bt_thread.join()
            btn_bt.text = "Conectar Bluetooth"
            status.value = "Bluetooth desconectado."
            page.update()
            stop_threads.clear()
        else:
            if not port_dropdown.value:
                status.value = "Selecione uma porta Bluetooth"
                page.update()
                return
            stop_threads.clear()
            bt_thread = threading.Thread(target=bluetooth_reader, daemon=True)
            bt_thread.start()
            btn_bt.text = "Desconectar Bluetooth"
            status.value = "Bluetooth conectado..."
            page.update()

    def on_cam_click(e):
        nonlocal cam_thread
        if cam_thread and cam_thread.is_alive():
            stop_threads.set()
            cam_thread.join()
            btn_cam.text = "Iniciar Stream"
            img.src_base64 = None
            status.value = "Stream parado."
            page.update()
            stop_threads.clear()
        else:
            stop_threads.clear()
            cam_thread = threading.Thread(target=camera_streamer, daemon=True)
            cam_thread.start()
            btn_cam.text = "Parar Stream"
            status.value = "Transmitindo vídeo..."
            page.update()

    btn_bt.on_click = on_bt_click
    btn_cam.on_click = on_cam_click

    # Layout final
    return ft.Column(
        scroll=ft.ScrollMode.AUTO,
        controls=[
            ft.Row(
                controls=[
                    ft.IconButton(icon=ft.Icons.ARROW_BACK, on_click=lambda e: page.go("/")),
                    ft.Text("Bluetooth & ESP32-CAM", size=20, weight=ft.FontWeight.BOLD),
                ]
            ),
            ft.Divider(),
            status,
            ft.Column([port_dropdown, btn_bt], spacing=10),
            arduino_data,
            ft.Divider(),
            img,
            btn_cam,
        ],
    )
