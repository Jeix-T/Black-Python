#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import whois
import dns.resolver
from colorama import Fore, Style, init

init()

def banner():
    print(f"{Fore.CYAN}[+] Herramienta de Reconocimiento de Dominios v1.0{Style.RESET_ALL}")

def get_whois(domain):
    try:
        print(f"{Fore.YELLOW}[*] Consultando WHOIS...{Style.RESET_ALL}")
        w = whois.whois(domain)
        print(f"{Fore.GREEN}[+] Registrador: {w.registrar}{Style.RESET_ALL}")
        print(f"{Fore.GREEN}[+] Fecha Creacion: {w.creation_date}{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}[-] Error WHOIS: {e}{Style.RESET_ALL}")

def get_dns(domain):
    records = ['A', 'MX', 'NS', 'TXT']
    print(f"{Fore.YELLOW}[*] Consultando DNS...{Style.RESET_ALL}")

    for record_type in records:
        try:
            answers = dns.resolver.resolve(domain, record_type)
            print(f"{Fore.CYAN}     [+] {record_type}: {Style.RESET_ALL}", end="")
            for rdata in answers:
                print(f"{rdata}", end=" ")
            print("\n")
        except Exception as e:
            print(f"{Fore.RED}      [-] Error en {record_type}: {e}{Style.RESET_ALL}")

def main():
    banner()

    if len(sys.argv) < 2:
        print(f"{Fore.RED}[-] Uso: python3 domain_recon.py <dominio>{Style.RESET_ALL}")
        sys.exit(1)

    target = sys.argv[1]

    # Validacion basica
    if not target.endswith('.com') and not target.endswith('.org') and not target.endswith('.net'):
        print(f"{Fore.YELLOW}[!] Advertencia: El dominio podria no ser valido{Style.RESET_ALL}")

    get_whois(target)
    print("\n")
    get_dns(target)

if __name__=='__main__':
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Fore.RED}[-] Interrumpido por usuario.{Style.RESET_ALL}")    
