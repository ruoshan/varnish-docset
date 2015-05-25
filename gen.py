#!/usr/local/bin/python

import os, re, sqlite3
from bs4 import BeautifulSoup, NavigableString, Tag

db = sqlite3.connect('./docSet.dsidx')
cur = db.cursor()

try:
    cur.execute('DROP TABLE searchIndex;')
except:
    pass

cur.execute('CREATE TABLE searchIndex(id INTEGER PRIMARY KEY, name TEXT, type TEXT, path TEXT);')
cur.execute('CREATE UNIQUE INDEX anchor ON searchIndex (name, type, path);')

docpath = './Documents'

#cur.execute('INSERT OR IGNORE INTO searchIndex(name, type, path) VALUES (?,?,?)', (name, 'Directive', path))

## parsing the vcl.html

vcl_page = open(docpath + "/reference/vcl.html", 'r')
vcl_soup = BeautifulSoup(vcl_page)

vcl_variables = vcl_soup.find("div", id="variables")
for sec in vcl_variables.find_all("div", class_="section"):
    name = sec["id"]
    path = "/reference/vcl.html#" + name
    cur.execute('INSERT OR IGNORE INTO searchIndex(name, type, path) VALUES (?,?,?)', (name, 'Variable', path))


## parsing built-in-subs.html
subr_page = open(docpath + "/users-guide/vcl-built-in-subs.html", 'r')
subr_soup = BeautifulSoup(subr_page)

subr_section = subr_soup.find("div", id="built-in-subroutines")
for sec in subr_section.find_all("div", class_="section"):
    for s in sec.find_all("div", recursive=False):
        name = s["id"]
        path = "users-guide/vcl-built-in-subs.html#" + name
        cur.execute('INSERT OR IGNORE INTO searchIndex(name, type, path) VALUES (?,?,?)', (name, 'Subroutine', path))


db.commit()
db.close()
