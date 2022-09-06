#!/usr/bin/env python3
import hashlib
import sqlite3 as sql
from flaskapp import dbLoc

## @package locker script which contains all functions regarding login ID and
## password verification and insertion into the database.


## Performs the login credentials verification for a given ID and password
## pair.
## @param ID login ID to be verified; str.
## @param password login password to be verified; str.
## @retval result  result of the login credentials verification; bool.
def loginCheck(ID, password):
    ## result of the login verification check; bool.
    result = False
    ## SQLite database.
    db = sql.connect(dbLoc)
    ## Cursor for accessing the SQLite database.
    cursor = db.cursor()
    cursor.execute('SELECT * FROM login WHERE ID=?', (ID,))
    ## Result of the cursor's query.
    query = cursor.fetchone()
    if query is not None:
        if hashlib.pbkdf2_hmac('sha256', password.encode("utf-8"), query[2], 100000)==query[1]:
            result = True
    db.close()
    return result


## Verifies if a given ID is already present at the SQLite database.
## @param ID login ID to be verified; str.
## @retval result result of the ID check; bool.
def IDexists(ID):
    result = True
    db = sql.connect(dbLoc)
    cursor = db.cursor()
    cursor.execute('SELECT ID FROM login WHERE ID=?', (ID,))
    if cursor.fetchone() is None:
        result =  False
    db.close()
    return result


## Creates a new user by iserting the given ID and password pair, while hashing
## the given password.
## @param ID login ID to be inserted into the database; str.
## @param password password to be inserted into the database; str.
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
