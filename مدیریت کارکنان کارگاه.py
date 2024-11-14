from tkinter import *
import sqlite3
#===============================================#
window = Tk()
window.title("مديريت کارکنان کارگاه")
window.geometry("1050x290")
window.resizable(False, False)
window.config(bg = "lightgray")
#===============================================#
file_name = "Workers.db"

connection = sqlite3.connect(file_name)
cursor = connection.cursor()

create_table = """
CREATE TABLE IF NOT EXISTS Workers(
First_Name TEXT,
Last_Name TEXT,
The_Amount_Of_Work_Hours INTEGER,
ID_Code INTEGER,
Date_Of_Employment TEXT,
Working_Hours_This_Month INTEGER,
Salary Integer
)
"""

cursor.execute(create_table)

connection.commit()
connection.close()

print("Table Created Successfully")
#===============================================#
def on_select(event):
    entry_show_text = entry_show.get("current linestart", "current lineend")
    selected_data = entry_show_text.split("-")        

    entry_name.delete(0, END)
    entry_name.insert(END, selected_data[0])

    entry_lname.delete(0, END)
    entry_lname.insert(END, selected_data[1])

    entry_price.delete(0, END)
    entry_price.insert(END, selected_data[2])

    entry_id.delete(0, END)
    entry_id.insert(END, selected_data[3])

    entry_date.delete(0, END)
    entry_date.insert(END, selected_data[4])

    entry_work.delete(0, END)
    entry_work.insert(END, selected_data[5])
#-----------------------------------------------#
def add():
    entry_show.delete(1.0, END)
    fname = entry_name.get()
    lname = entry_lname.get()
    TAOWH = int(entry_price.get())
    ID = entry_id.get()
    date = entry_date.get()
    WHTM = int(entry_work.get())
    salary = TAOWH * WHTM
    file_name = "Workers.db"
    
    connection = sqlite3.connect(file_name)
    cursor = connection.cursor()

    records = [fname, lname, TAOWH, ID, date, WHTM, salary]

    insert_query = """INSERT INTO Workers (First_Name, Last_Name, The_Amount_Of_Work_Hours,
    ID_Code, Date_Of_Employment, Working_Hours_This_Month, Salary) VALUES (?, ?, ?, ?, ?, ?, ?)"""
    cursor.execute(insert_query, records)

    entry_name.delete(0, END)
    entry_lname.delete(0, END)
    entry_price.delete(0, END)
    entry_id.delete(0, END)
    entry_date.delete(0, END)
    entry_work.delete(0, END)

    connection.commit()
    entry_show.insert(END, "با موفق ذخيره شد")
    connection.close()
#-----------------------------------------------#
def delete():
    entry_show.delete(1.0, END)
    ID = entry_id.get()
    
    file_name = "Workers.db"
    
    connection = sqlite3.connect(file_name)
    cursor = connection.cursor()

    delete_query = "DELETE FROM Workers WHERE ID_Code = ?"
    cursor.execute(delete_query, (ID,))

    entry_name.delete(0, END)
    entry_lname.delete(0, END)
    entry_price.delete(0, END)
    entry_id.delete(0, END)
    entry_date.delete(0, END)
    entry_work.delete(0, END)
    
    connection.commit()
    entry_show.insert(END, f"با موفقيت حذف شد")
    connection.close()
#-----------------------------------------------#
def search():
    entry_show.delete(1.0, END)

    fname = entry_name.get()
    lname = entry_lname.get()
    ID = entry_id.get()
    date = entry_date.get()

    file_name = "Workers.db"
    connection = sqlite3.connect(file_name)
    cursor = connection.cursor()

    query = "SELECT * FROM Workers WHERE 1=1"
    params = []

    if fname:
        query += " AND First_Name = ?"
        params.append(fname)

    if lname:
        query += " AND Last_Name = ?"
        params.append(lname)

    if ID:
        query += " AND ID_Code = ?"
        params.append(ID)

    if date:
        query += " AND Date_Of_Employment = ?"
        params.append(date)

    cursor.execute(query, params)
    results = cursor.fetchall()
    
    for result in results:
        entry_show.insert(END, f"{result[0]}-{result[1]}-{result[2]}-{result[3]}-{result[4]}-{result[5]}-{result[6]}\n")

    entry_name.delete(0, END)
    entry_lname.delete(0, END)
    entry_price.delete(0, END)
    entry_id.delete(0, END)
    entry_date.delete(0, END)
    entry_work.delete(0, END)

    connection.close()
#-----------------------------------------------#
def see_all():
    entry_show.delete(1.0, END)
    
    file_name = "Workers.db"
    connection = sqlite3.connect(file_name)
    cursor = connection.cursor()
    
    cursor.execute("SELECT * FROM Workers")
    
    results = cursor.fetchall()
    for result in results:
        entry_show.insert(END, f"{result[0]}-{result[1]}-{result[2]}-{result[3]}-{result[4]}-{result[5]}-{result[6]}\n")
    
    connection.close()
#-----------------------------------------------#
def sort():
    entry_show.delete(1.0, END)
    
    file_name = "Workers.db"
    connection = sqlite3.connect(file_name)
    cursor = connection.cursor()
    
    cursor.execute("SELECT * FROM Workers")
    results = cursor.fetchall()
    
    sorted_results = sorted(results, key=lambda x: x[6])
        
    for result in sorted_results:
        entry_show.insert(END, f"{result[0]}-{result[1]}-{result[2]}-{result[3]}-{result[4]}-{result[5]}-{result[6]}\n")
    
    connection.close()
#-----------------------------------------------#
def exit():
    window.destroy()
#===============================================#
entry_name = Entry(window, bd = 5, relief = "sunken")
entry_name.place(height = 30, width = 155, x = 880, y = 20)
#-----------------------------------------------#
entry_lname = Entry(window, bd = 5, relief = "sunken")
entry_lname.place(height = 30, width = 155, x = 630, y = 20)
#-----------------------------------------------#
entry_price = Entry(window, bd = 5, relief = "sunken")
entry_price.place(height = 30, width = 155, x = 320, y = 20)
#-----------------------------------------------#
entry_id = Entry(window, bd = 5, relief = "sunken")
entry_id.place(height = 30, width = 155, x = 880, y = 70)
#-----------------------------------------------#
entry_date = Entry(window, bd = 5, relief = "sunken")
entry_date.place(height = 30, width = 155, x = 630, y = 70)
#-----------------------------------------------#
entry_work = Entry(window, bd = 5, relief = "sunken")
entry_work.place(height = 30, width = 155, x = 320, y = 70)
#-----------------------------------------------#
entry_salary = Entry(window, bd = 5, relief = "sunken")
entry_salary.place(height = 50, width = 140, x = 13, y = 50)
#===============================================#
label_name = Label(window, text = "نام کارگر", font = ("Arial", 16), bg = "lightgray")
label_name.place(x = 795, y = 20)
#-----------------------------------------------#
label_lname = Label(window, text = "نام خانوادگي کارگر", font = ("Arial", 16), bg = "lightgray")
label_lname.place(x = 485, y = 20)
#-----------------------------------------------#
label_price = Label(window, text = "مبلغ ساعت کار", font = ("Arial", 16), bg = "lightgray")
label_price.place(x = 200, y = 20)
#-----------------------------------------------#
label_id = Label(window, text = "کد ملي", font = ("Arial", 16), bg = "lightgray")
label_id.place(x = 807, y = 70)
#-----------------------------------------------#
label_date = Label(window, text = "تاريخ استخدام", font = ("Arial", 16), bg = "lightgray")
label_date.place(x = 505, y = 70)
#-----------------------------------------------#
label_work = Label(window, text = "ساعت کار در اين ماه", font = ("Arial", 16), bg = "lightgray")
label_work.place(x = 163, y = 70)
#-----------------------------------------------#
label_salary = Label(window, text = "حقوق اين ماه", font = ("Arial", 16), bg = "lightgray")
label_salary.place(x = 35, y = 17)
#===============================================#
BTN_See = Button(window, text = "مشاهده همه", command = see_all, font = ("Arial", 14), bd = 5, relief = "raised")
BTN_See.place(height = 40, width = 120, x = 890, y = 120)
#-----------------------------------------------#
BTN_Search = Button(window, text = "جستجو", command = search, font = ("Arial", 14), bd = 5, relief = "raised")
BTN_Search.place(height = 40, width = 120, x = 760, y = 120)
#-----------------------------------------------#
BTN_sort = Button(window, text = "مرتب کردن", command = sort, font = ("Arial", 14), bd = 5, relief = "raised")
BTN_sort.place(height = 40, width = 120, x = 890, y = 170)
#-----------------------------------------------#
BTN_add = Button(window, text = "اضافه کردن", command = add, font = ("Arial", 14), bd = 5, relief = "raised")
BTN_add.place(height = 40, width = 120, x = 760, y = 170)
#-----------------------------------------------#
BTN_delete = Button(window, text = "حذف کردن", command = delete, font = ("Arial", 14), bd = 5, relief = "raised")
BTN_delete.place(height = 40, width = 120, x = 890, y = 220)
#-----------------------------------------------#
BTN_exit = Button(window, text = "خروج", command = exit, font = ("Arial", 14), bd = 5, relief = "raised")
BTN_exit.place(height = 40, width = 120, x = 760, y = 220)
#===============================================#
scroll = Scrollbar(window, bd = 2, relief = "raised")
scroll.place(height = 150, width = 30, x = 650, y = 120)
#===============================================#
entry_show = Text(window, yscrollcommand=scroll.set)
entry_show.place(height = 170, width = 630, x = 13, y = 110)
scroll.config(command=entry_show.yview)
entry_show.bind("<ButtonRelease-1>", on_select)
#===============================================#
window.mainloop()
