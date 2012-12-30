#!/usr/bin/env python
# -*- coding: utf-8 -*-

import SOAPpy

default_url = 'http://packages.qa.debian.org/cgi-bin/soap-alpha.cgi'
ws = SOAPpy.SOAPProxy(default_url)


def query(method, source):
    return getattr(ws, method)(source=source)
