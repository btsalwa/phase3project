import sqlite3

CONN = sqlite3.connect('main.db')
CURSOR = CONN.cursor()