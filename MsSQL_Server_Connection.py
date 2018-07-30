# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 12:45:43 2018

@author: murali.nsr
"""

import pyodbc
conn = pyodbc.connect(
    r'DRIVER={ODBC Driver 11 for SQL Server};'
    r'SERVER=10.10.11.28;'
    r'DATABASE=murli;'
    r'UID=sa;'
    r'PWD=Passw0rd'
    )
 
cursor = conn.cursor()
cursor.execute('SELECT * FROM Customer')