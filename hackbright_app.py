import sqlite3

DB = None
CONN = None

def get_student_by_github(github):
    query = """SELECT first_name, last_name, github FROM Students WHERE github = ?"""
    DB.execute(query, (github,))
    row = DB.fetchone()
    return row

def get_project_by_title(title):
    query = """SELECT * FROM Projects WHERE title = ?"""
    DB.execute(query, (title,))
    row = DB.fetchone()
    print """\
    ID: %s
    Title: %s
    Description: %s
    Score: %s""" %(row[0],row[1], row[2], row[3])

def connect_to_db():
    global DB, CONN
    CONN = sqlite3.connect("hackbright.db")
    DB = CONN.cursor()

def make_new_student(first_name, last_name, github):
        query = """INSERT into Students values(?, ?, ?)"""
        DB.execute(query, (first_name, last_name, github))

        CONN.commit()
        print "Successfully added student: %s %s" %(first_name, last_name)

def make_new_project(title, description, max_grade):
    query = """INSERT into Projects (title, description, max_grade) values (?, ?, ?)"""
    DB.execute(query, (title, description, max_grade))

    CONN.commit()
    print "Successfully added project: %s %s %s" % (title, description, max_grade)

def get_grade_given_project(grade):
    query = """SELECT title, description, max_grade FROM Projects Where title = ?"""
    DB.execute(query, (title,))
    row = DB.fetchone()
    print """\
    Title and Description: %s %s
    Grade: %s""" % (row[0], row[1], row[2])

def give_grade_to_student(student_github, project_title, grade):
    query = """INSERT into Grades (student_github, project_title, grade) 
                values (?, ?, ?)"""
    DB.execute(query, (student_github, project_title, grade))
    CONN.commit()
    print "Successfully added grade: %s %s %s" %(student_github, project_title, grade)

        





def main():
    connect_to_db()
    command = None
    while command != "quit":
        input_string = raw_input("HBA Database> ")
        tokens = input_string.split()
        command = tokens[0]
        args = tokens[1:]

        if command == "student":
            get_student_by_github(*args) 
        elif command == "new_student":
            make_new_student(*args)
        elif command == "title":
            get_project_by_title(*args)
        elif command == "projects":
            make_new_project(*args)
        elif command == "add_grade":
            give_grade_to_student(*args)

    CONN.close()

if __name__ == "__main__":
    main()


#CREATE TABLE Projects (id INTEGER PRIMARY KEY AUTOINCREMENT, title varchar(30), description TEXT, max_grade INT);
