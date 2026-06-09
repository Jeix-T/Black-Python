#!/usr/bin/env python3

from colorama import Fore, Style

"""----------------------------------------------------------------------------
Autor:          Jeix T
Archivo:        colors.py
Descripcion:    Muestra la impresion de texto en diferentes colores

"""

print(f"{Fore.GREEN}{Style.BRIGHT }[+] {Style.RESET_ALL}Éxito")
print(f"{Fore.RED}{Style.BRIGHT }[-] {Style.RESET_ALL}Error")
print(f"{Fore.YELLOW}{Style.BRIGHT }[!] {Style.RESET_ALL}Advertencia")
