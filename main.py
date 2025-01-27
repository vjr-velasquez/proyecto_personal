import os
import colorama
from colorama import Fore, Style, init
import xml.etree.ElementTree as ET
from arbolAvl import ArbolAVL

init()

def login():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(Fore.MAGENTA + " == Login ==" + Style.RESET_ALL)
        print("")
        username = input(Fore.WHITE + "Username: " + Style.RESET_ALL)
        password = input(Fore.WHITE + "Password: " + Style.RESET_ALL)
        if username == "admin" and password == "admin123":
            print(Fore.GREEN + "Acceso concedido" + Style.RESET_ALL)
            return True
        else:
            print(Fore.RED + "Los datos no coinciden. Por favor intente nuevamente" + Style.RESET_ALL)
            input(Fore.YELLOW + "Presione Enter para continuar..." + Style.RESET_ALL)


def carga_datos_usuarios(arbol):
    ruta = input("Ingrese la ruta del archivo XML: ")
    tree = ET.parse(ruta)
    root = tree.getroot()
    for usuario in root.findall('usuario'):
        datos = {
            'id': usuario.find('id').text,
            'nombre': usuario.find('nombre').text,
            'correo': usuario.find('correo').text,
            'telefono': usuario.find('telefono').text,
        }
        arbol.insertar(datos['id'], datos)

def carga_productos():
    pass

def gestion_usarios():
    pass

def venta_productos():
    pass

def reportes():
    pass

def menu():
    while True:
        print(Fore.WHITE + " ====== Bienvenido al sistema de ventas ====== " + Style.RESET_ALL)
        print("")
        print(Fore.WHITE + "1. Carga de datos de usuarios" + Style.RESET_ALL)
        print(Fore.WHITE + "2. Carga de productos" + Style.RESET_ALL)
        print(Fore.WHITE + "3. Gestion de usuarios" + Style.RESET_ALL)
        print(Fore.WHITE + "4. Venta de productos" + Style.RESET_ALL)
        print(Fore.WHITE + "5. Reportes" + Style.RESET_ALL)
        print(Fore.WHITE + "6. Salir" + Style.RESET_ALL)
        print("")
        opcion = input(Fore.GREEN + "Ingrese una opcion: " + Style.RESET_ALL).strip()
        if opcion == '1':
            arbol = ArbolAVL()
            carga_datos_usuarios(arbol)
            print(Fore.YELLOW + "Usuarios cargados en el árbol AVL:" + Style.RESET_ALL)
            #arbol.preorden(arbol.root)
        elif opcion == '2':
            carga_productos()
        elif opcion == '3':
            gestion_usarios()
        elif opcion == '4':
            venta_productos()
        elif opcion == '5':
            reportes()
        elif opcion == '6':
            break
        else:
            print(Fore.RED + "Opción no válida, por favor intente de nuevo." + Style.RESET_ALL)

if __name__ == "__main__":
    if login():
        menu()