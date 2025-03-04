from machine import Pin, PWM
from time import sleep

# Configuramos el pin y la frecuencia PWM para el ESC (50Hz-20ms)

esc = PWM(Pin(4))
esc.freq(50)
#duty_u16 = 0  # Configurar a 16bits - 0 -> 65535


# Formato ANSCII
GREEN = "\033[42m"
YELLOW = "\033[43m"
RED = "\033[41m"
BLUE = "\033[44m"
MAGENTA = "\033[45m"
WHITE = "\033[47m"
TBLACK = "\033[30m"
TRED ="\033[91m"
RESET = "\033[0m"

# Arming: Enviar señal mínima para armar el ESC

print("Waiting ESC 'Arming' ")
esc.duty(54)  # ~ 1000us
sleep(2)
print(f"{GREEN} 'Arming' Complete - ESC Ready {RESET}")
sleep(1)


# Funciones:
# Función de calibración del ESC

def esc_calibrate():
    print(f"{YELLOW}{TBLACK} Iniciando calibración del ESC...{RESET}")
    esc.duty(1023)  # 2000us - Max
    sleep(1)
    esc.duty(54)  # 1000us - Min
    sleep(3)
    print(f"{YELLOW}{TBLACK} Calibracion Completa! {RESET}\n")

def manual_speed():
    """Configura una velocidad en función de un valor del Duty Cycle"""
    while True:
        try:
            speed = int(input(f"{GREEN} Enter a Speed:{RESET}"))
            esc.duty(speed)
            pct = (int(speed*100)/1023)
            print(f"{TRED} Speed Setted @: {speed} - {pct}% {RESET}")
            sleep(0.1)
            return speed
        except ValueError:
            print(f"{RED}Error: You must enter an integer value! {RESET}\n")

def manual_pct():
    """Configura una velocidad en función de un valor porcentual"""
    while True:
        try:
            pct = int(input(f"{GREEN} Enter a PCT Speed:{RESET}"))
            pctSpeed = (int((pct*1023)/100))
            esc.duty(pctSpeed)
            print(f"{TRED} Speed Setted @: {pctSpeed}% {RESET}")
            sleep(0.1)
            return pctSpeed
        except ValueError:
            print(f"{RED}Error: You must enter an integer value! {RESET}\n")

def autonomous():
    """Acelera y Desacelera el motor en un rango de Duty 54 a 102"""
    for i in range(54,104,2):
        esc.duty(i)
        print(f"\r{BLUE} Accelerating: -{i}- {RESET}", end="")
        sleep(0.2)
    print("\n Keeping a steady Speed")
    sleep(5)
    for i in range(102,52,-2):
        esc.duty(i)
        print(f"\r{MAGENTA} Slowing Down: -{i}- {RESET}", end="")
        sleep(0.2)
    print(f"\n{WHITE}{TBLACK} STOP! {RESET}")
    sleep(2)
        
#INICIO
esc_calibrate()
sleep(2)
while True:
    autonomous()
    sleep(1)

    
