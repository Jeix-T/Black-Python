#!/usr/bin/env python3

import os
import sys
from colorama import Fore, Style

"""----------------------------------------------------------------------------
Autor:          Jeix t
Archivo:        isRoot.py
Descripcion:    Comprueba que se tengan permisos de root

"""
if os.geteuid() != 0:
    print(f"{Fore.RED}[-] Este script requiere privilegios de root.{Style.RESET_ALL}")
    sys.exit(1)
else:
    print(f"{Fore.GREEN}[+] Ejecutando con provilegios root.{Style.RESET_ALL}")
