#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import netifaces as ni

iface = 'eth0'
mac = ni.ifaddresses(iface)[ni.AF_LINK][0]['addr']

print(f'[+] Direccion MAC: {mac}')
