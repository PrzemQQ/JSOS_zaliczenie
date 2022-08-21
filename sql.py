import sqlite3 as sql
connection = sql.connect("baza.db")
connection.row_factory = sql.Row
cur = connection.cursor()
cur.executescript("""
            DROP TABLE IF EXISTS infos;
            DROP TABLE IF EXISTS marks;
            
            CREATE TABLE infos (
                student_id INTEGER PRIMARY KEY,
                name CHAR(15) NOT NULL,
                lastname CHAR(15) NOT NULL,
                year_of_birth DATE NOT NULL,
                address CHAR(25)
                );
            
            CREATE TABLE marks (
                student_id INTEGER PRIMARY KEY,
                mark_1 INTEGER,
                mark_2 INTEGER,
                mark_3 INTEGER,
                FOREIGN KEY(student_id) REFERENCES infos(student_id));
            """)
connection.commit()
students = (
    ( 'Tomasz', 'Kowalski', '2021-12-01', 'Łódź'),
    ( 'Anna', 'Nowak', '2001-12-11', 'Warszawa'),
    ( 'Joanna', 'Chyłka', '1997-09-01', 'Gdańsk'),
    ( 'Remigiusz', 'Mróz', '1985-03-14', 'Poznań')
)
cur.executemany("INSERT INTO `infos` ( `name`, `lastname`, `year_of_birth`, `address`) VALUES (?,?,?,?)",students)
marks = (
    ('1', '5', '4', '3'),
    ('2', '2', '2', '1'),
    ('3', '6', '4', '5'),
    ('4', '3', '2', '1')
)
cur.executemany("INSERT INTO `marks` (`student_id`, `mark_1`, `mark_2`, `mark_3`) VALUES (?,?,?,?)",marks)
connection.commit()
#lista uczniów
def readData():
    cur.execute("""
                SELECT  * from infos;

                """)
    students = cur.fetchall()
    for student in students:
        print(student["student_id"],student['name'],student['lastname'])

if __name__ == '__main__':
#usuwamy jednego
    readData()
    cur.execute("DELETE FROM infos WHERE student_id=?",(4,))
    cur.execute("DELETE FROM marks WHERE student_id=?",(4,))
    connection.commit()
    print("-------------------")
    #sprawdzamy liste ponownie 
    readData()

def show_all_grades():
    cur.execute(" SELECT * FROM infos")
    grades = cur.fetchall()
    student_name = []
    student_lastname = []
    student_grades = []
    for grade in grades:
        student_name.append(grade['name'])
        student_lastname.append(grade["lastname"])
        student_grades.append((grade["mark_1"],grade["mark_2"],grade["mark_3"]))
    return student_name, student_lastname,student_grades

def add_grades(student,grade):
    cur.execute("INSERT INTO MARKS VALUE(?) WHERE student_id='%s'",(grade,)%student)
 
def students_info():
    cur.execute(" SELECT * FROM infos")
    grades = cur.fetchall()
    cur.execute("SELECT * from marks")
    marks = cur.fetchall()
    student_name = []
    student_lastname = []
    student_grades = []
    student_id = []
    student_address = []
    student_date = []
    for grade in grades:
        
        student_name.append(grade[1])
        student_lastname.append(grade[2])
        student_date.append(grade[3])
        student_id.append(grade[0])
        student_address.append(grade[4])
    for mark in marks:
        student_grades.append((mark[1],mark[2],mark[3]))
    return student_name, student_lastname,student_grades, student_id, student_address, student_date
    
    
def change_grades(id,position_of_mark,newmark):
    cur.execute("UPDATE marks SET mark_{%s}=? WHERE ID=?",(newmark,id)%position_of_mark)
    
    
