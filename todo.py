#!/usr/bin/python
# -*- coding: utf-8-*-

import sqlite3
from datetime import datetime
import argparse
import os

db_name = "todo.db"

def createTable():
  conn = sqlite3.connect(db_name)
  c = conn.cursor()
  c.execute('''
  CREATE TABLE "todo_list" (
	"todo_id"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	"pwd"	TEXT,
	"todo"	TEXT NOT NULL,
	"date_time"	TEXT
	);
  ''')
  conn.commit()
  conn.close()

def insertTodo(todo):
  pwd = os.environ['PWD']
  now = datetime.now()
  time = "{}/{} {}:{}".format(now.month, now.day, now.hour, now.minute)
  conn = sqlite3.connect(db_name)
  c = conn.cursor()
  c.execute("""INSERT INTO todo_list("pwd", "todo", "date_time") VALUES("{}","{}","{}")""".format(pwd,todo,time))
  conn.commit()
  conn.close()

def selectTodo():
  conn = sqlite3.connect(db_name)
  c = conn.cursor()
  c.execute("""SELECT * FROM todo_list""")
  rows = c.fetchall()
  conn.close()
  return rows

def selectTodoPwd():
  pwd = os.environ['PWD']
  conn = sqlite3.connect(db_name)
  c = conn.cursor()
  c.execute("""SELECT * FROM todo_list WHERE pwd='{}'""".format(pwd))
  rows = c.fetchall()
  conn.close()
  return rows

def deleteTodo(id):
  result = False
  conn = sqlite3.connect(db_name)
  c = conn.cursor()
  c.execute("""SELECT * FROM todo_list WHERE todo_id='{}'""".format(id))
  if c.fetchone() != None:
    result = True
    c.execute("""DELETE FROM todo_list WHERE todo_id='{}'""".format(id))
    conn.commit()
  conn.close()
  return result

def printTodoPwd(rows):
  pwd = os.environ['PWD']
  result = ""
  if str(rows) == "[]":
    result = "✎------FINISH------✎\n📁: {}".format(pwd)
  else:
    result = "✎-------TODO-------✎\n📁: {}".format(pwd)
    for i in rows:
      result = result + "\n✓ {id} | 📋 : {todo} | 🕒 : {time} ".format(id=i[0],todo=i[2],time=i[3]) 
  return result

def printTodo(rows):
  result = ""
  if str(rows) == "[]":
    result = "✎------FINISH------✎"
  else:
    result = "✎-------TODO-------✎"
    for i in rows:
      result = result + "\n✓ {id} | 📋 : {todo} | 🕒 : {time} | 📁: {dir} ".format(id=i[0],dir=i[1],todo=i[2],time=i[3]) 
  return result

def checkDB():
  conn = sqlite3.connect(db_name)
  c = conn.cursor()
  c.execute("SELECT COUNT(*) FROM sqlite_master WHERE name='{}';".format("todo_list"))
  row = c.fetchone()
  conn.close()
  if row[0] == 0:
    createTable()

def main():
  checkDB()
  parser = argparse.ArgumentParser(description='Simple TODO!')
  parser.add_argument('-a', metavar='all', required=False, action="store_const", const="all",
                        help='Show all todo_list!')
  parser.add_argument('-d', metavar='del', type=int, nargs=1, required=False,
                        help='Delete todo!')
  parser.add_argument('-m', metavar='msg', type=str, nargs=1, required=False,
                        help='Add todo!')
  args = parser.parse_args()
  if args.a == "all":
    print(printTodo(selectTodo()))
  elif args.d != None:
    if deleteTodo(args.d[0]):
      print("Succes!")
    else:
      print("fail!")
  elif args.m != None:
    insertTodo(args.m[0])
    print("Succes!")
  else:
    print(printTodoPwd(selectTodoPwd()))

if __name__ == "__main__":
  main()