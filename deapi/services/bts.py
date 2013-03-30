#!/usr/bin/env python
# -*- coding: utf-8 -*-

import SOAPpy

default_url = 'http://bugs.debian.org/cgi-bin/soap.cgi'
ws = SOAPpy.SOAPProxy(default_url)


def query(method, value):
	return getattr(ws, method)(value)

def query_get_versions(package, dist, arch):
	return getattr(ws, "get_versions")(package, dist, arch)
