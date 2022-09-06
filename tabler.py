
def tabler():
    import os
    import sqlite3 as sql
    current_dir = os.getcwd()
    db = sql.connect(current_dir+"/memory/profile.sql")
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
