from datetime import datetime
import sqlite3

TODAY = datetime.today().strftime("%Y-%m-%d")

con = sqlite3.connect("crawling.db")

cur = con.cursor()

cur.execute(
    """
    CREATE TABLE IF NOT EXISTS daily_idiom
        (id INTEGER PRIMARY KEY, date text, name text, link text, meaning text, example text)
"""
)
cur.execute(
    """
    CREATE TABLE IF NOT EXISTS all_idioms
        (id INTEGER PRIMARY KEY, name text, link text, meaning text, example text)
"""
)
cur.execute(
    """
    CREATE TABLE IF NOT EXISTS daily_word
        (id INTEGER PRIMARY KEY, date text, word text, img_src text, link text)
"""
)

con.commit()
con.close()
