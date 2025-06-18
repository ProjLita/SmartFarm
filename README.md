# SmartFarm - Aplicativo de Monitoramento

## Requisitos
- Python 3.7 ou superior
- Dispositivo Bluetooth compatível
- ESP32-CAM configurado

## Instalação

1. Clone este repositório ou baixe os arquivos

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

## Uso

1. Execute o programa:
```bash
python SmartFarm.py
```

2. No aplicativo:
   - Selecione a porta Bluetooth correta no dropdown
   - Clique em "Conectar Bluetooth" para iniciar a conexão
   - Clique em "Iniciar Stream" para visualizar a câmera

## Solução de Problemas

### Bluetooth
- Verifique se o dispositivo Bluetooth está ligado
- Confirme se a porta COM está correta
- Certifique-se que nenhum outro programa está usando a porta

### Câmera
- Verifique se o ESP32-CAM está ligado
- Confirme se o endereço IP está correto (padrão: 192.168.4.1)
- Verifique se está na mesma rede do ESP32-CAM 