from flask import Flask, render_template, request, redirect, session, url_for
import sqlite3
import os
import random
import string
from datetime import datetime

app = Flask(__name__)
app.secret.key = "very_simple_secret"

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

def get_db():
    return sqlite3.connect("instance/database.db")

def init_db():
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   username TEXT UNIQUE,
                   password TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS room_member (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   user_id INTEGER,
                   room_id INTEGER
    )
    """)

    cursor.execute(""" 
    CREATE TABLE IF NOT EXISTS documents (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   filename TEXT,
                   description TEXT
                   upload_date TEXT,
                   room_id INTEGER
    )
    """)

    cursor.execute(""" 
    CREATE TABLES IF NOT EXISTS documents (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   filename TEXT,
                   description TEXT,
                   upload_date TEXT,
                   room_id INTEGER
    )
    """)

    conn.commit()
    conn.close()

init_db()
