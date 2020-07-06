from CONFIG import *

from pyshorteners import Shortener
adfly = Shortener('Adfly', uid=ADFLY_UID, key=ADFLY_API_KEY, type='int', timeout=10)

import sqlite3
conn = sqlite3.connect(DATABASE_PATH)
c = conn.cursor()

try:
    c.execute('CREATE TABLE users(user_id INTEGER)')
except sqlite3.OperationalError:
    pass

def add_user(user_id):
    c.execute('SELECT * FROM users WHERE user_id=?', (user_id,))
    if not c.fetchall():
        c.execute('INSERT INTO users VALUES(?)', (user_id,))
    conn.commit()

def remove_user(user_id):
    c.execute('DELETE FROM users WHERE user_id=?', (user_id,))
    conn.commit()

def count_users():
    c.execute('SELECT COUNT(*) FROM users')
    for res in c.fetchall():
        return res[0]

def short(service, url):
    url = 'http://' + url.replace('https://', '').replace('http://', '') # Simple but it works

    if service.lower() == 'adfly':
        return adfly.short(url)

