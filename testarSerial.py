# instalar a lib pyserial com pip install pyserial
#
# caso ocorra o erro:
# NameError: name 'SerialArduino' is not defined
#
# Verificar
# 1) Se o Arduino está conectado na serial
# 2) Se a porta serial está correta
# 3) Se o monitor serial do arduino não está aberto bloqueando a conexão serial
# 4) Se a lib pyserial foi instalada corretamente

import serial # pip install pyserial

porta = 'portaSerialDoSeuArduino' # no windows em geral 'COM2' e linux ou mac em geral -> '/dev/ttyS0'
# porta = 'COM3' # exemplo
velocidadeBaud = 115200 # Mesmo se a velocidade estiver errada, a conexão com a serial irá funcionar normalmente

SerialArduino = serial.Serial(porta,velocidadeBaud, timeout = 0.2)
