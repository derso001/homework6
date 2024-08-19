import sqlite3
from pprint import pprint


def execute_query(sql: str) -> list:
    with sqlite3.connect('test.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


sql = """
SELECT s.id, s.name
FROM students s
JOIN groups g ON s.groups_id_fn = g.id
WHERE g.name = '11COT';
"""


pprint(execute_query(sql))

