import sqlite3
from sqlite3 import Error


"""
connection = sqlite3.connect(file)
cursor =  connection.cursor()
cursor.execute(<requete>)
||
#INSERT INTO table (name, autre) VALUES (?, ?, ?)
cursor.execute(<requete>, <tuple>)
cursor.commit()
#dernier ID
cursor.lastrowid()

#recup le resultat d'une requete (liste)
cursor.fetchall()

ON OUBLIE PAS !
---------------
connection.close()
"""


"""
CREATION D'UNE CONNECTION
"""


def create_conection(file):
    conn = None
    try:
        conn = sqlite3.connect(file)  #:memory:
        return conn
    except Error as e:
        print(e)
    # finally:
    #    if conn:
    #        conn.close()


"""
A partir d'une connection executer une requete, ici ajout d'une table
"""


def create_table(connection, table_sql):
    try:
        c = connection.cursor()
        c.execute(table_sql)
    except Error as e:
        print(e)


"""
Insertion de data avec des requetes preparees
"""


def create_project(conn, project):
    sql = """ INSERT INTO projects(name,begin_date,end_date)
              VALUES(?,?,?) """
    cur = conn.cursor()
    cur.execute(sql, project)
    conn.commit()
    return cur.lastrowid


def create_task(conn, task):
    sql = """ INSERT INTO tasks(name,priority,status_id,project_id,begin_date,end_date)
              VALUES(?,?,?,?,?,?) """
    cur = conn.cursor()
    cur.execute(sql, task)
    conn.commit()
    return cur.lastrowid


"""
Interroger
"""


def select_all_tasks(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM tasks")

    rows = cur.fetchall()

    for row in rows:
        print(row)


def select_task_by_priority(conn, priority):
    cur = conn.cursor()
    cur.execute("SELECT * FROM tasks WHERE priority=?", (priority,))

    rows = cur.fetchall()

    for row in rows:
        print(row)


database = r"base.db"

sql_create_projects_table = """ CREATE TABLE IF NOT EXISTS projects (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        begin_date text,
                                        end_date text
                                    ); """

sql_create_tasks_table = """CREATE TABLE IF NOT EXISTS tasks (
                                    id integer PRIMARY KEY,
                                    name text NOT NULL,
                                    priority integer,
                                    status_id integer NOT NULL,
                                    project_id integer NOT NULL,
                                    begin_date text NOT NULL,
                                    end_date text NOT NULL,
                                    FOREIGN KEY (project_id) REFERENCES projects (id)
                                );"""


conn = create_conection(database)

if conn is not None:
    create_table(conn, sql_create_projects_table)
    create_table(conn, sql_create_tasks_table)
else:
    print("Error")

with conn:
    # create a new project
    project = ("Cool App with SQLite & Python", "2015-01-01", "2015-01-30")
    project_id = create_project(conn, project)

    # tasks
    task_1 = (
        "Analyze the requirements of the app",
        1,
        1,
        project_id,
        "2015-01-01",
        "2015-01-02",
    )
    task_2 = (
        "Confirm with user about the top requirements",
        2,
        1,
        project_id,
        "2015-01-03",
        "2015-01-05",
    )

    # create tasks
    create_task(conn, task_1)
    create_task(conn, task_2)

    print("lire toute les tasks")
    # read all task
    select_all_tasks(conn)

    print("lire par prio")
    # read task by priority
    select_task_by_priority(conn, 1)
