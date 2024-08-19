from sqlite3 import Error

from connect import create_connection, database


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
        conn.commit()
    except Error as e:
        print(e)


if __name__ == '__main__':
    sql_create_groups_table = """
    CREATE TABLE IF NOT EXISTS groups (
     id integer PRIMARY KEY,
     name text NOT NULL
    );
    """

    sql_create_students_table = """
    CREATE TABLE IF NOT EXISTS students (
     id integer PRIMARY KEY,
     name text NOT NULL,
     groups_id_fn integer NOT NULL,
     FOREIGN KEY (groups_id_fn) REFERENCES groups (id)
    );
    """

    sql_create_lectors_table = """
    CREATE TABLE IF NOT EXISTS lectors (
     id integer PRIMARY KEY,
     name text NOT NULL
     );
    """

    sql_create_subjects_table = """
    CREATE TABLE IF NOT EXISTS subjects (
     id integer PRIMARY KEY,
     name text NOT NULL, 
     lector_id_fn integer NOT NULL,
     FOREIGN KEY (lector_id_fn) REFERENCES lectors (id)
     );
    """

    sql_create_marks_table = """
    CREATE TABLE IF NOT EXISTS marks (
     id integer PRIMARY KEY,
     value text NOT NULL,
     timestamp text,
     student_id_fn integer NOT NULL,
     subject_id_fn integer NOT NULL,
     FOREIGN KEY (subject_id_fn) REFERENCES subjects (id),
     FOREIGN KEY (student_id_fn) REFERENCES students (id)
    );
    """


    with create_connection(database) as conn:
        if conn is not None:
            create_table(conn, sql_create_groups_table)
            create_table(conn, sql_create_students_table)
            create_table(conn, sql_create_lectors_table)
            create_table(conn, sql_create_subjects_table)
            create_table(conn, sql_create_marks_table)

        else:
            print("Error! cannot create the database connection.")
