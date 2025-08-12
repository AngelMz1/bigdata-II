'''
Dev : Angel Muñoz
Script description: SQLite3 database config
'''
#import engine database package
import sqlite3

#create database connection
con = sqlite3.connect('Database-Exercise/market.db')

#create cursor for CRUD
cur = con.cursor()

#create users table
user_table = '''
    CREATE TABLE IF NOT EXISTS users (
        id INTERGER PRIMARY KEY,
        firstname TEXT NOT NULL,
        lastname TEX NOT NULL,
        ide_number VARCHAR(15) UNIQUE NOT NULL,
        email TEXT UNIQUE NOT NULL,
        status BOOLEAN DEFAULT true,
        created_at TIMESTAMP DEFAULT (datetime('now','localtime')), 
        updated_at TIMESTAMP DEFAULT (datetime('now','localtime')),
        deleted_at TIMESTAMP NULL
    );
'''
#Execute SQL
cur.execute(user_table)


#safe changes oin database => push database
con.commit()