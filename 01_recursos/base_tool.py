#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os
from colorama import Fore, Style, init

# Inicializar colorama
init()

def banner():
    print(f"{Fore.CYAN}")
    print(r"""
    _    _ ____  ___ ______________  
    | |  | | __ \ | |/ /_  _/   _  \ 
    | |  | | |__) | ' /  | | | |  | |
    | |  | |  ___/|  <   | | | |  | |
    | |__| | |    | . \ _| |_| |__| |
     \____/|_|    |_|\_\_____\_____/ 
    """)
    print(f"{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}Curso Python para Pentesting-{Style.RESET_ALL}\n")

def check_root():
    if os.geteuid() != 0:
        print(f"{Fore.RED}[-] Error: Se requieren privilegios de root.{Style.RESET_ALL}")
        sys.exit(1)
    else:
        print(f"{Fore.GREEN}[+] Privilegios verificados.{Style.RESET_ALL}")

def main():
    banner()
    check_root()
    
    if len(sys.argv) < 2:
        print(f"{Fore.YELLOW}[!] Uso: python3 {sys.argv[0]} <objetivo>{Style.RESET_ALL}")
        sys.exit(1)
    
    target = sys.argv[1]
    print(f"{Fore.GREEN}[+] Iniciando herramienta contra: {target}{Style.RESET_ALL}")
    
    # Aquí irá la lógica en futuras sesiones
    print(f"{Fore.CYAN}[*] Esperando comandos...{Style.RESET_ALL}")

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Fore.RED}[-] Salida forzada por el usuario.{Style.RESET_ALL}")
        sys.exit(0)
