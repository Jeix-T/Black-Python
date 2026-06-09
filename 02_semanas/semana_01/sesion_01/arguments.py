#!/usr/bin/env python3

from colorama import Fore, Style
import sys

"""----------------------------------------------------------------------------
Autor:          Jeix t
Archivo:        arguments.py
Descripcion:    Comprueba que se pasen argumentos de forma correcta

"""

# ]> Evalua si se pasaron argumentos
if len(sys.argv) < 2:
    name = sys.argv[0]
    print(f"{Fore.RED}{Style.BRIGHT}[-] ERROR{Style.RESET_ALL} - Uso:")
    print(f"\t{name} <IP_OBJETIVO>")
    sys.exit(1)

target = sys.argv[1]

print(f"{Style.BRIGHT}[+] TARGET: {Style.RESET_ALL}{target}")
