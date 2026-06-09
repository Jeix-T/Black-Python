#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import dns.resolver

answers = dns.resolver.resolve('google.com', 'A')

for rdata in answers:
    print(rdata.address)
