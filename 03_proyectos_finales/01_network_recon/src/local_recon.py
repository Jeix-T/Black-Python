#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
import netifaces as ni
import sys
import os
from colorama import Fore, Style, init

init()

def banner():
    print(f"{Fore.CYAN}[+] Herramienta de reconocimiento Local v1.0{Style.RESET_ALL}")

def get_local_info():

    try:
        # 1. Hostname e IP Principal
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
        print(f"{Fore.GREEN}[+] Hostname: {hostname}{Style.RESET_ALL}")
        print(f"{Fore.GREEN}[+] IP Local: {local_ip}{Style.RESET_ALL}")

        # 2. Interfaces de red
        interfaces = ni.interfaces()
        print(f"{Fore.YELLOW}[*] Interfaces encontradas: {interfaces}{Style.RESET_ALL}")

        for iface in interfaces:
            if iface == 'lo': continue # Saltar loopback

            addrs = ni.ifaddresses(iface)
            gws = ni.gateways()

            # IPV4
            if ni.AF_INET in addrs:
                ip = addrs[ni.AF_INET][0]['addr']
                netmask = addrs[ni.AF_INET][0]['netmask']
                gateway = gws['default'][ni.AF_INET][0]
                print(f"{Fore.CYAN}     [+] {iface} | IP: {ip} | Mask: {netmask} | Gateway: {gateway}{Style.RESET_ALL}")

            # MAC
            if ni.AF_LINK in addrs:
                mac = addrs[ni.AF_LINK][0]['addr']
                print(f"{Fore.CYAN}     [+] {iface} | MAC: {mac}{Style.RESET_ALL}")

    except KeyError as error:
        print(f"{Fore.RED}[-] No se ha encontrado ninguna puerta de enlace predeterminada: {error}{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}[-] Error obteniendo info de red: {e}{Style.RESET_ALL}")

def main():
    banner()
    get_local_info()

if __name__=='__main__':
    main()    
