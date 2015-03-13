#!/usr/bin/env python
import sqlite3
import sys

def get_pinyin(conn, name):
    ret = ""
    for c in [name[i:i+3] for i in range(0,len(name),3)]:
        sql = 'select pinyin from pinyin where char = "%s"' % (c)
        cursor = conn.execute(sql)
        row = cursor.fetchone()
        if row:
            ret = ret+row[0]
    return  ret
        
def get_xing(conn, name):
    sql = 'select pinyin from xing where char = "%s"' % (name)
    cursor = conn.execute(sql)
    row = cursor.fetchone()
    if row:
        return row[0]
    else:
        return get_pinyin (conn, name)

def get_fuxing(conn, name):
    sql = 'select pinyin from fuxing where char = "%s"' % (name)
    cursor = conn.execute(sql)
    row = cursor.fetchone()
    if row:
        return row[0]
    else:
        return ""
    
if __name__ == '__main__':
    name = sys.argv[1].decode("GBK").encode("UTF-8")
    conn = sqlite3.connect("db/pinyin.db")
    surname_py = get_fuxing(conn, name[0:6])
    if surname_py:
        name_py = get_pinyin(conn, name[6:len(name)])
    else:
        surname_py = get_xing(conn, name[0:3])
        name_py = get_pinyin(conn, name[3:len(name)])
    print surname_py+" "+name_py