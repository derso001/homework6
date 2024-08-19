from sqlite3 import Error

from connect import create_connection, database
from random import randint
import faker



def create_group(conn, group):
    sql = ''' 
    INSERT INTO groups(name) VALUES(?); 
    '''
    cur = conn.cursor()
    try:
        cur.execute(sql, group)
        conn.commit()
    except Error as e:
        print(e)
    finally:
        cur.close()

    return cur.lastrowid

def create_student(conn, student):

    #  id integer PRIMARY KEY,
    #  name text NOT NULL,
    #  groups_id_fn integer NOT NULL,



    sql = ''' 
    INSERT INTO students (name, groups_id_fn) VALUES(?, ?); 
    '''
    cur = conn.cursor()
    try:
        cur.execute(sql, student)
        conn.commit()
    except Error as e:
        print(e)
    finally:
        cur.close()

    return cur.lastrowid

def create_lector(conn, lector):
    sql = ''' 
    INSERT INTO lectors(name) VALUES(?); 
    '''
    cur = conn.cursor()
    try:
        cur.execute(sql, lector)
        conn.commit()
    except Error as e:
        print(e)
    finally:
        cur.close()

    return cur.lastrowid

def create_subject(conn, student):
    sql = ''' 
    INSERT INTO subjects (name, lector_id_fn) VALUES(?, ?); 
    '''
    cur = conn.cursor()
    try:
        cur.execute(sql, student)
        conn.commit()
    except Error as e:
        print(e)
    finally:
        cur.close()

    return cur.lastrowid

def create_mark(conn, mark):

    sql = ''' 
    INSERT INTO marks (value, timestamp, student_id_fn, subject_id_fn) VALUES(?, ?, ?, ?); 
    '''
    cur = conn.cursor()
    try:
        cur.execute(sql, mark)
        conn.commit()
    except Error as e:
        print(e)
    finally:
        cur.close()

    return cur.lastrowid


if __name__ == '__main__':
    fake_data = faker.Faker()
    subjects_name_list = ["Філософія", "Вища математика", "Психологія", "Педагогіка", "Технології"]


    group_id_list = []
    students_id_list = []
    lectors_id_list = []
    subjects_id_list = []
    marks_id_list =[]



    with create_connection(database) as conn:
       
        group1 = ('11COT',)
        group_id = create_group(conn, group1)
        print(group_id)
        group_id_list.append(group_id)

        group2 = ('12COT',)
        group_id = create_group(conn, group2)
        print(group_id)
        group_id_list.append(group_id)

        group3 = ('13COT',)
        group_id = create_group(conn, group3)
        print(group_id)
        group_id_list.append(group_id)

        for group_id in group_id_list:
            for _ in range(10):
                students_id = create_student(conn, (fake_data.name(), str(group_id)))
                print(students_id)
                students_id_list.append(students_id)

        for _ in range(5):
            lector_id = create_lector(conn, (fake_data.name(),))
            print(lector_id)
            lectors_id_list.append(lector_id)

        for i in range(0, 5):
            subject_id = create_subject(conn, (subjects_name_list[i], str(lectors_id_list[i])))
            print(subject_id)
            subjects_id_list.append(subject_id)

        for student_id in students_id_list:
            for subject_id in subjects_id_list:
                for _ in range(4):
                    mark_id = create_mark(conn, (str(randint(15, 25)), f"2023-0{randint(1,3)}-{randint(1,31)}", str(student_id), str(subject_id)))
                    marks_id_list.append(mark_id)

        




