#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket

hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)

print(f"[+] Hostname: {hostname}")
print(f"[+] IP Local: {ip}")
