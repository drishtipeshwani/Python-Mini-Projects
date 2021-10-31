# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 19:03:32 2021

@author: Hrithik Sawhney
"""
# Import socket module
import socket			

# Create a socket object
s = socket.socket()		

# Define the port on which you want to connect
port = 12345			

# connect to the server on local computer
s.connect(('127.0.0.1', port))

# receive data from the server and decoding to get the string.
print (s.recv(1024).decode())
# close the connection
s.close()	
	


