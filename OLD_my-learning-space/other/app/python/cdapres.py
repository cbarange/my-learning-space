#!/usr/bin/env python3
# -*- coding : utf-8 -*-
import cgi
import cgitb
from os import environ

# Active debug mod, print error in browser windows
cgitb.enable()

# ---------- HEADER ----------
def header():
	print('Content-type: text/html')
	print('Content-Language: Latin')
	print('Age: 1234567980')
	print('Status: 442 Coroned')
	print('Location: https://www.google.com')
	print('Connection: Coroned')
	print('Server: Unknown')
	print('Date: Unknown')
	print('MyHeader0: Coroned')
	print('MyHeader1: Coroned')
	print('MyHeader2: Coroned')
	print('MyHeader3: Coroned')
	print('MyHeader4: Coroned')
	print('MyHeader5: Coroned')
	print('MyHeader6: Coroned')
	print('MyHeader7: Coroned')
	print('MyHeader8: Coroned')
	print('MyHeader9: Coroned')
	print('\n\n')
header()
# ---------- BODY ----------
print ("<h1>It's Work !</h1><br/>")

# ---------- DATA ----------
data = cgi.FieldStorage()
print(data)

# ---------- DEBUG ----------
print('<hr/>')
#cgi.print_environ()

