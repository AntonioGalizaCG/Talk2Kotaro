import hashlib
import sqlite3 as sql
from flaskapp import dbLoc

def loginCheck(ID, password):
    result = False
    db = sql.connect(dbLoc)
    cursor = db.cursor()
    cursor.execute('SELECT * FROM login WHERE ID=?', (ID,))
    query = cursor.fetchone()
    if query is not None:
        if hashlib.pbkdf2_hmac('sha256', password.encode("utf-8"), query[2], 100000)==query[1]:
            result = True
    db.close()
    return result

def IDexists(ID):
    result = True
    db = sql.connect(dbLoc)
    cursor = db.cursor()
    cursor.execute('SELECT ID FROM login WHERE ID=?', (ID,))
    if cursor.fetchone() is None:
        result =  False
    db.close()
    return result

def createUser(ID, password):
    from os import urandom
    new_salt = urandom(32) # A new salt for this user
    new_pepper = urandom(32)
    password = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), new_salt, 100000)
    db = sql.connect(dbLoc)
    cursor = db.cursor()
    cursor.execute("""
        INSERT INTO login
        (ID, Password, Salt, Pepper)
        VALUES (?,?,?,?)
    """,[ID,password,new_salt,new_pepper])
    db.commit()
    db.close()

################################################################################
################################################################################
################################################################################
