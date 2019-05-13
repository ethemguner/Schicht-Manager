import sqlite3

database = sqlite3.connect("database.db")
cursor = database.cursor()
"""
cursor.execute("CREATE TABLE IF NOT EXISTS admin (id, pass)")
cursor.execute("INSERT INTO admin VALUES(?,?)", ("muratguener", 120769))
"""

#cursor.execute("DELETE FROM shift3 WHERE date = ?",["2019-04-23"])

cursor.execute("UPDATE shift5 SET month = ? WHERE date = ?",("April", "2019-04-03"))


database.commit()