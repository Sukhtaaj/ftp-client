#!/usr/bin/python3

'''
List directories & files on remote server.
By Souad Elfane
'''

from ftplib import FTP

try:
	ftp = FTP("ftp.acc.umu.se")
	ftp.login()
	ftp.dir()
	
except Exception as error:
	print("Could not login.")
	print(error)
