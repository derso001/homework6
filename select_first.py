import sqlite3
from pprint import pprint


def execute_query(sql: str) -> list:
    with sqlite3.connect('test.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


sql = """
SELECT s.name, m.value 
FROM students AS s
INNER JOIN marks AS m ON m.student_id_fn = s.id
"""
sql1 = """
SELECT name
FROM students
"""

result = execute_query(sql)

students_dict = dict()
for stud in execute_query(sql1):
    students_dict[stud[0]] = 0

for i in result:
    if i[0] in students_dict:
        students_dict[i[0]] += int(i[1])/20

sort_dict = sorted(students_dict.items(), key=lambda item: item[1], reverse=True)

for i in range(5):
    pprint(sort_dict[i])

