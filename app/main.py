#!/usr/bin/env python3
#hi
#first edit
from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import json
import os
import mysql.connector
from mysql.connector import Error
app = FastAPI()
app = FastAPI()
from fastapi.middleware.cors import CORSMiddleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


DBHOST = "ds2022.cqee4iwdcaph.us-east-1.rds.amazonaws.com"
DBUSER = "admin"
DBPASS = os.getenv('DBPASS')
DB = "dtv9vd"


db = mysql.connector.connect(user=DBUSER, host=DBHOST, password=DBPASS, database=DB)
cur=db.cursor()

app = FastAPI()

@app.get("/")  # zone apex
def zone_apex():
    return("Good day Anaya")

@app.get("/sum/{a}/{b}")
def add(a: int, b: int):
	return {"sum": a + b}

@app.get("/square/{a}")
def get_square(a: int):
    return{"result":a ** 2}

@app.get("/multiply/{c}/{d}")
def multiply(c: int, d: int):
    return {"product": c * d}

@app.get('/genres')
def get_genres():
    query = "SELECT * FROM genres ORDER BY genreid;"
    db = mysql.connector.connect(user=DBUSER, host=DBHOST, password=DBPASS, database=DB)
    cur = db.cursor()

    try:
        cur.execute(query)
        headers = [x[0] for x in cur.description]
        results = cur.fetchall()
        json_data = []
        for result in results:
            json_data.append(dict(zip(headers, result)))
        cur.close()
        db.close()
        return json_data
    except Error as e:
        cur.close()
        db.close()
        return {"Error": "MySQL Error: " + str(e)}

@app.get('/songs')
def get_songs():
    db = mysql.connector.connect(user=DBUSER, host=DBHOST, password=DBPASS, database=DB)
    cur = db.cursor()
    query = """
        SELECT songs.title, songs.album, songs.artist, songs.year, songs.file, 
               songs.image, genres.genre 
        FROM songs 
        JOIN genres ON songs.genre = genres.genreid;
    """

    try:
        cur.execute(query)
        headers = [x[0] for x in cur.description]
        results = cur.fetchall()
        json_data = []
        for result in results:
            json_data.append(dict(zip(headers, result)))
        cur.close()
        db.close()
        return json_data
    except Error as e:
        cur.close()
        db.close()
        return {"Error": "MySQL Error: " + str(e)}      



import mysql.connector
from mysql.connector import Error

