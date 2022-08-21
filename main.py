from sql import *
from tkinter import *
from tkinter import messagebox
window = Tk()
window.geometry("1024x800")
window.title("JSOS")
window.config(background="#000c17")
label1 = Label(window,text="Welcome to JSOS",font=('Calibri',60,'bold'),fg="#ffffff", bg="#000c17")
label1.pack()

def window_show_grades():
    show_window = Toplevel(window)
    show_window.title("Students all grades")
    show_window.config(background="#000c17")
    show_window.geometry("500x500")
    label1 = Label(show_window,text="Students' grades",font=('Calibri',30,'bold'),fg="#ffffff", bg="#000c17")
    label1.pack()
    select_grades = students_info()
    total_rows = len(students_info()[0])
  
    for j in range(0,len(select_grades[0])):
        T = Text(show_window, height=2)
        T.pack()
        T.insert(END, f"|{select_grades[0][j]} |{select_grades[1][j]} | {select_grades[2][j]}|")

def windows_add_student():
    
    def submit():
        student_name = entry_name.get()
        student_lastname = entry_lastname.get()
        student_address = entry_address.get()
        student_date = entry_date.get()
        
        if student_name != "" and student_lastname != "" and student_address != "" and type(student_name) !=int and type(student_lastname) != int and type(student_address) != int:
            cur.execute("INSERT INTO `infos` ( `name`, `lastname`, `year_of_birth`, `address`) VALUES (?,?,?,?)",(student_name,student_lastname,student_date,student_address))
            cur.execute("INSERT INTO `marks` ( `mark_1`, `mark_2`, `mark_3`) VALUES (?,?,?)",('0','0','0'))
            connection.commit()
            messagebox.showinfo(title="Task completed", message="Added new student")
        else:
            messagebox.showerror(title="Task incompleted", message="Something went wrong, try again")
        
        
    add_window = Toplevel(window)
    add_window.title("Adding student")
    add_window.config(background="#000c17")
    add_window.geometry("400x400")
    label1 = Label(add_window,text="Add new student",font=('Calibri',30,'bold'),fg="#ffffff", bg="#000c17")
    label1.pack()
    
    
    label_name = Label(add_window,text="Name:",font=('Times New Roman',15,'bold'),fg="#0587ff", bg="#000c17")
    label_name.pack()
    entry_name = Entry(add_window, font=("Arial",20))
    entry_name.pack()
    
    label_lastname = Label(add_window,text="Lastname:",font=('Times New Roman',15,'bold'),fg="#0587ff", bg="#000c17")
    label_lastname.pack()
    entry_lastname = Entry(add_window, font=("Arial",20))
    entry_lastname.pack()
    
    label_address = Label(add_window,text="Address:",font=('Times New Roman',15,'bold'),fg="#0587ff", bg="#000c17")
    label_address.pack()
    entry_address = Entry(add_window, font=("Arial",20))
    entry_address.pack()
    
    label_date = Label(add_window,text="Date of birth:",font=('Times New Roman',15,'bold'),fg="#0587ff", bg="#000c17")
    label_date.pack()
    entry_date = Entry(add_window, font=("Arial",20))
    entry_date.pack()
    
    submit_button = Button(add_window,text="Add student",command=submit)
    submit_button.pack()

def window_student():
    stu_window = Toplevel(window)
    stu_window.title("Infos about students")
    stu_window.config(background="#000c17")
    stu_window.geometry("500x500")
    label1 = Label(stu_window,text="Students' infos",font=('Calibri',30,'bold'),fg="#ffffff", bg="#000c17")
    label1.pack()
    all_infos_about_students = students_info()
    total_rows = len(students_info()[0])
  
    for j in range(0,len(all_infos_about_students[0])):
        T = Text(stu_window, height=2)
        T.pack()
        T.insert(END, f"|{all_infos_about_students[3][j]} |{all_infos_about_students[0][j]} | {all_infos_about_students[1][j]}| {all_infos_about_students[2][j]}| {all_infos_about_students[5][j]}| {all_infos_about_students[4][j]}|")

def window_change_grades():
    def submit():
        student_id = entry_id.get()
        grade_position = entry_position.get()
        new_grade = entry_new_grade.get()
        if  student_id != "" and grade_position != "" and grade_position != "" and new_grade != "":
            cur.execute("UPDATE marks SET mark_{}='{}' where student_id='{}'".format(grade_position,new_grade,student_id))
            connection.commit()
            messagebox.showinfo(title="Task completed", message="Changed value of mark")
        else:
            messagebox.showerror(title="Task incompleted", message="Something went wrong, try again")

            
        
        
        
        
    change_window = Toplevel(window)
    change_window.title("Changing grades")
    change_window.config(background="#000c17")
    change_window.geometry("400x400")
    label1 = Label(change_window,text="Change grade",font=('Calibri',30,'bold'),fg="#ffffff", bg="#000c17")
    label1.pack()
    
    label_id = Label(change_window,text="Id:",font=('Times New Roman',15,'bold'),fg="#0587ff", bg="#000c17")
    label_id.pack()
    entry_id = Entry(change_window, font=("Arial",20))
    entry_id.pack()
    
    label_position = Label(change_window,text="Which grade:",font=('Times New Roman',15,'bold'),fg="#0587ff", bg="#000c17")
    label_position.pack()
    entry_position = Entry(change_window, font=("Arial",20))
    entry_position.pack()
    
    label_new_grade = Label(change_window,text="New grade:",font=('Times New Roman',15,'bold'),fg="#0587ff", bg="#000c17")
    label_new_grade.pack()
    entry_new_grade = Entry(change_window, font=("Arial",20))
    entry_new_grade.pack()
    
    submit_button = Button(change_window,text="Change grade",command=submit)
    submit_button.pack()
    



btn_show_grades = Button(window,text="Show all grades",
                         font=("Calibri",30)
                         ,fg="#ffffff",
                         bg="#000c17",
                         activebackground="#000c17",
                         activeforeground="#ffffff",
                         bd=20,
                         padx=50,
                         command=window_show_grades)
btn_show_grades.pack()
btn_add_grades = Button(window,text="Add new student",
                        command=windows_add_student,
                        font=("Calibri",30),
                        fg="#ffffff", bg="#000c17",
                        activebackground="#000c17",
                        activeforeground="#ffffff",
                        bd=20,
                        padx=40 )
btn_add_grades.pack()
btn_students_info = Button(window,text="Student's infos",
                           command=window_student,
                           font=("Calibri",30),
                           fg="#ffffff",
                           bg="#000c17",
                           activebackground="#000c17",
                           activeforeground="#ffffff",
                           bd=20,
                           padx=57 )
btn_students_info.pack()
btn_change_grades = Button(window,text="Change grades",
                           command=window_change_grades,
                           font=("Calibri",30),
                           fg="#ffffff",
                           bg="#000c17",
                           activebackground="#000c17",
                           activeforeground="#ffffff",
                           bd=20,
                           padx=60 )
btn_change_grades.pack()

window.mainloop()