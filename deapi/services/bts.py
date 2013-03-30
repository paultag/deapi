#!/usr/bin/env python
# -*- coding: utf-8 -*-

import SOAPpy

default_url = 'http://bugs.debian.org/cgi-bin/soap.cgi'
ws = SOAPpy.SOAPProxy(default_url)


def query_get_status(bugnumbers):
	return getattr(ws, "get_status")(bugnumbers)


def query_get_bugs(conditions):
	return getattr(ws, "get_bugs")(conditions)


def query_get_usertag(email):
	return getattr(ws, "get_usertag")(email)


def query_get_bug_log(bugnumber):
	return getattr(ws, "get_bug_log")(bugnumber)


def query_newest_bugs(amount):
	return getattr(ws, "newest_bugs")(amount)


def query_get_versions(package, dist, arch):
	return getattr(ws, "get_versions")(package, dist, arch)
