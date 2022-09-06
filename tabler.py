#!/usr/bin/env python3
import os
import sqlite3 as sql

## Creates a new empty SQLite database with all the correct tables and fields.
def tabler():
    ## current directory where the script is being executed; str.
    current_dir = os.getcwd()
    ## SQLite database.
    db = sql.connect(current_dir+"/memory/profile.sql")
    ## cursor for acessing the SQLite database.
    cursor = db.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS analysis (
            ID TEXT,
            phrase TEXT,
            prosody TEXT,
            voiceFile TEXT,
            videoFile TEXT,
            emotion TEXT
        )''')
    db.commit()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS info (
        ID TEXT,
        age TEXT,
        gender TEXT,
        originReg TEXT,
        motherLang TEXT,
        spokenLang TEXT,
        whereAbroad TEXT,
        timeAbroad TEXT
        )''')
    db.commit()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS likert (
        ID TEXT,
        q1 TEXT,
        q2 TEXT,
        q3 TEXT,
        q4 TEXT,
        q5 TEXT,
        q6 TEXT,
        q7 TEXT,
        q8 TEXT,
        q9 TEXT,
        q10 TEXT
        )''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS login (
            ID TEXT,
            Password BLOB,
            Salt BLOB,
            Pepper BLOB
        )''')
    db.commit()

    db.close()
