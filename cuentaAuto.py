import pyautogui as pg
from pynput.keyboard import Key, Controller
import time

keyboard = Controller()

def otra_cuenta():
    print('Crear otro usuario? (s/n)')
    return input().lower().startswith('s')

def empresa_auto_cuenta(nombre, user, passwd, anexo, correo):
    time.sleep(5)
    pg.click(1885, 240)
    pg.moveTo(2200, 179, duration = 0.3)
    pg.click()
    pg.typewrite(user)
    pg.typewrite(["tab"])
    pg.typewrite(["tab"])
    pg.typewrite(passwd)
    pg.typewrite(["tab"])
    pg.typewrite(nombre)
    pg.typewrite(["tab"])
    pg.typewrite("135")
    time.sleep(2)
    pg.typewrite("135")
    time.sleep(2)
    pg.typewrite("135")
    time.sleep(2)
    pg.typewrite("135")
    pg.typewrite(["tab"])
    pg.typewrite(["space"])
    time.sleep(2)
    pg.click()
    time.sleep(3)
    pg.moveTo(2229, 338, duration = 0.3)
    pg.doubleClick()
    pg.typewrite(anexo)
    pg.moveTo(2393, 449, duration = 0.3)
    pg.doubleClick()
    time.sleep(1)
    pg.doubleClick()
    pg.click()
    pg.typewrite(correo)
    keyboard.press('@')
    pg.typewrite("mundopacifico.cl")
    pg.scroll(-200)
    pg.click(2401, 721)
    time.sleep(1)
    pg.moveTo(2666, 374, duration = 0.3)
    pg.click()
    pg.moveTo(2433, 564, duration = 0.3)
    pg.click()


def televentas_auto_cuenta(nombre, user, passwd, anexo, correo):
    time.sleep(10)
    pg.click(1885, 240)
    pg.moveTo(2200, 179, duration = 0.3)
    pg.click()
    pg.typewrite(user)
    pg.typewrite(["tab"])
    pg.typewrite(["tab"])
    pg.typewrite(passwd)
    pg.typewrite(["tab"])
    pg.typewrite(nombre)
    pg.typewrite(["tab"])
    pg.typewrite("354")
    pg.typewrite(["tab"])
    pg.typewrite(["space"])
    time.sleep(2)
    pg.click()
    time.sleep(3)
    pg.moveTo(2229, 338, duration = 0.3)
    pg.doubleClick()
    pg.typewrite(anexo)
    pg.moveTo(2393, 449, duration = 0.3)
    pg.doubleClick()
    time.sleep(1)
    pg.doubleClick()
    pg.click()
    pg.typewrite(correo)
    keyboard.press('@')
    pg.typewrite("mundopacifico.cl")
    pg.scroll(-200)
    pg.click(2401, 721)
    time.sleep(1)
    pg.moveTo(2666, 374, duration = 0.3)
    pg.click()
    pg.moveTo(2433, 564, duration = 0.3)
    pg.click()


def contact_auto_cuenta(nombre, user, passwd, anexo, correo):
    time.sleep(10)
    pg.click(1885, 240)
    pg.moveTo(2200, 179, duration = 0.3)
    pg.click()
    pg.typewrite(user)
    pg.typewrite(["tab"])
    pg.typewrite(["tab"])
    pg.typewrite(passwd)
    pg.typewrite(["tab"])
    pg.typewrite(nombre)
    pg.typewrite(["tab"])
    pg.typewrite("554")
    pg.typewrite(["tab"])
    pg.typewrite(["space"])
    time.sleep(2)
    pg.click()
    time.sleep(3)
    pg.moveTo(2229, 338, duration = 0.3)
    pg.doubleClick()
    pg.typewrite(anexo)
    pg.moveTo(2393, 449, duration = 0.3)
    pg.doubleClick()
    time.sleep(1)
    pg.doubleClick()
    pg.click()
    pg.typewrite(correo)
    keyboard.press('@')
    pg.typewrite("mundopacifico.cl")
    pg.scroll(-200)
    pg.click(2401, 721)
    time.sleep(1)
    pg.moveTo(2666, 374, duration = 0.3)
    pg.click()
    pg.moveTo(2433, 564, duration = 0.3)
    pg.click()

def sporn2_auto_cuenta(nombre, user, passwd, anexo, correo):
    time.sleep(10)
    pg.click(1885, 240)
    pg.moveTo(2200, 179, duration = 0.3)
    pg.click()
    pg.typewrite(user)
    pg.typewrite(["tab"])
    pg.typewrite(["tab"])
    pg.typewrite(passwd)
    pg.typewrite(["tab"])
    pg.typewrite(nombre)
    pg.typewrite(["tab"])
    pg.typewrite("342")
    pg.typewrite(["tab"])
    pg.typewrite(["space"])
    time.sleep(2)
    pg.click()
    time.sleep(3)
    pg.moveTo(2229, 338, duration = 0.3)
    pg.doubleClick()
    pg.typewrite(anexo)
    pg.moveTo(2393, 449, duration = 0.3)
    pg.doubleClick()
    time.sleep(1)
    pg.doubleClick()
    pg.click()
    pg.typewrite(correo)
    keyboard.press('@')
    pg.typewrite("mundopacifico.cl")
    pg.scroll(-200)
    pg.click(2401, 721)
    time.sleep(1)
    pg.moveTo(2666, 374, duration = 0.3)
    pg.click()
    pg.moveTo(2433, 564, duration = 0.3)
    pg.click()


while True:
    if otra_cuenta():
        nombre = input('Indique Nombre completo del agente: ')
        user = input('Indique rut sin puntos ni digito verificador: ')
        passwd = input('Contraseña a usar por el agente: ')
        anexo = input('Anexo para el agente: ')
        correo = input('Correo del agente sin @: ')
        print('AREAS')
        print('1. Televentas')
        print('2. Contact Comercial')
        print('3. Contact Tecnico')
        print('4. Empresa')
        print('')
        area = input('Elija el número del área: ')
        if area == '1':
            televentas_auto_cuenta(nombre, user, passwd, anexo, correo)
        elif area == '2':
            contact_auto_cuenta(nombre, user, passwd, anexo, correo)
        elif area == '3':
            sporn2_auto_cuenta(nombre, user, passwd, anexo, correo)
        elif area == '4':
            empresa_auto_cuenta(nombre, user, passwd, anexo, correo)
        else:
            continue
    else:
        break
