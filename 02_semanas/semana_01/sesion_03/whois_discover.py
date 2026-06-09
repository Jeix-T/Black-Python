#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import whois

w = whois.whois('google.com')
print(w.domain_name, w.creation_date)
