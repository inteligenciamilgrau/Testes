import serial # para instalar digite pip install pyserial
import threading

# Coloque a porta Serial de acordo com seu computador
porta = 'COM4' # no windows escolher a COMX e no linux ou mac em geral -> '/dev/ttyS0'
velocidadeBaud = 115200

try:
    SerialArduino = serial.Serial(porta,velocidadeBaud, timeout = 0.2)
    print("Conectado!! Arduino funcionando!!")
except:
    print("Verificar se a porta serial está aberta em outro programa ou religar arduino")


def read_from_port(ser):
    print("Serial funcionando correntamente")

# Dará erro "NameError: name 'SerialArduino' is not defined" caso
# 1) O Arduino estiver desconectado
# 2) O Arduino estiver com o Terminal Serial aberto em outro programa
# 3) A porta (COM ou TTY) estiver errada

lerSerialThread = threading.Thread(target=read_from_port, args=(SerialArduino,))
lerSerialThread.start()
