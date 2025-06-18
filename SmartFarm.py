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
BLUETOOTH_PORT = "COM4"      # Altere para sua porta Bluetooth (ex: COM5 no Windows, /dev/rfcomm0 no Linux)
BLUETOOTH_BAUDRATE = 9600
ESP32_CAM_STREAM_URL = "http://192.168.4.1:81/stream"  # URL do stream MJPEG da ESP32-CAM

def list_available_ports():
    """Lista todas as portas seriais disponíveis"""
    ports = []
    for port in list_ports.comports():
        ports.append(port.device)
    return ports

def main(page: ft.Page):
    page.title = "Arduino Bluetooth + ESP32-CAM"
    page.window_width = 500
    page.window_height = 700
    page.padding = 20

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

    page.add(
        ft.Column([
            status,
            port_dropdown,
            arduino_data,
            btn_bt,
            ft.Divider(),
            img,
            btn_cam,
        ], alignment=ft.MainAxisAlignment.START, spacing=20)
    )

    # Variáveis de controle
    bt_thread = None
    cam_thread = None
    stop_threads = threading.Event()
    ser = None

    # Função para ler dados do Arduino via Bluetooth
    def bluetooth_reader():
        nonlocal ser
        try:
            selected_port = port_dropdown.value or BLUETOOTH_PORT
            status.value = f"Tentando conectar na porta {selected_port}..."
            page.update()
            
            ser = serial.Serial(
                port=selected_port,
                baudrate=BLUETOOTH_BAUDRATE,
                timeout=1,
                write_timeout=1
            )
            
            # Teste inicial de conexão
            ser.write(b'AT\r\n')
            time.sleep(1)
            
            if ser.in_waiting:
                response = ser.readline().decode(errors="ignore").strip()
                if response:
                    status.value = "Bluetooth conectado e respondendo!"
                else:
                    status.value = "Bluetooth conectado, mas sem resposta do dispositivo."
            else:
                status.value = "Bluetooth conectado, aguardando dados..."
            
            page.update()
            
            while not stop_threads.is_set():
                if ser.in_waiting:
                    line = ser.readline().decode(errors="ignore").strip()
                    if line:
                        arduino_data.value = f"Dado do Arduino: {line}"
                        page.update()
                time.sleep(0.1)
                
        except serial.SerialException as e:
            status.value = f"Erro na conexão Bluetooth: {str(e)}\nVerifique se:\n1. A porta está correta\n2. O dispositivo está ligado\n3. Nenhum outro programa está usando a porta"
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

    # Função para atualizar lista de portas
    def update_ports():
        available_ports = list_available_ports()
        port_dropdown.options = [ft.dropdown.Option(port) for port in available_ports]
        if available_ports:
            port_dropdown.value = available_ports[0]
        page.update()

    # Função para exibir MJPEG stream da ESP32-CAM
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
                        encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 70]
                        _, buffer = cv2.imencode('.jpg', frame, encode_param)
                        if len(buffer) < 3 * 1024 * 1024:
                            img.src_base64 = base64.b64encode(buffer).decode()
                            page.update()
                        else:
                            status.value = "Frame muito grande, reduza a resolução do ESP32-CAM."
                            page.update()
        except requests.exceptions.ConnectionError:
            status.value = "Erro: Não foi possível conectar à câmera. Verifique se o ESP32-CAM está ligado e acessível."
            page.update()
        except Exception as e:
            status.value = f"Erro no stream: {e}"
            page.update()

    # Handlers dos botões
    def on_bt_click(e):
        nonlocal bt_thread
        if bt_thread and bt_thread.is_alive():
            stop_threads.set()
            status.value = "Desconectando Bluetooth..."
            page.update()
            bt_thread.join()
            btn_bt.text = "Conectar Bluetooth"
            status.value = "Bluetooth desconectado."
            page.update()
            stop_threads.clear()
        else:
            if not port_dropdown.value:
                status.value = "Por favor, selecione uma porta Bluetooth"
                page.update()
                return
                
            stop_threads.clear()
            bt_thread = threading.Thread(target=bluetooth_reader, daemon=True)
            bt_thread.start()
            btn_bt.text = "Desconectar Bluetooth"
            status.value = "Conectando Bluetooth..."
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

    # Encerra threads ao fechar o app
    def on_close(e):
        stop_threads.set()
        if bt_thread and bt_thread.is_alive():
            bt_thread.join()
        if cam_thread and cam_thread.is_alive():
            cam_thread.join()
        if ser and ser.is_open:
            ser.close()

    page.on_close = on_close

ft.app(target=main)
