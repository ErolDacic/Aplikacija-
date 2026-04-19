import customtkinter as ctk
import csv
import os

FILE = "students.csv"

if not os.path.exists(FILE):
    with open(FILE,"w",newline="") as f:
        writer=csv.writer(f)
        writer.writerow(["id","name","index","department"])


def add_student():

    with open(FILE,"a",newline="") as f:
        writer=csv.writer(f)

        writer.writerow([
            id_entry.get(),
            name_entry.get(),
            index_entry.get(),
            dept_entry.get()
        ])

    show_students()


def show_students():

    textbox.delete("1.0","end")

    with open(FILE,"r") as f:

        for row in csv.reader(f):
            textbox.insert("end",str(row)+"\n")


def delete_student():

    delete_id=id_entry.get()

    rows=[]

    with open(FILE,"r") as f:

        for row in csv.reader(f):

            if row[0] != delete_id:
                rows.append(row)

    with open(FILE,"w",newline="") as f:
        writer=csv.writer(f)
        writer.writerows(rows)

    show_students()


def update_student():

    target=id_entry.get()

    rows=[]

    with open(FILE,"r") as f:

        for row in csv.reader(f):

            if row[0]==target:

                rows.append([
                    target,
                    name_entry.get(),
                    index_entry.get(),
                    dept_entry.get()
                ])

            else:
                rows.append(row)

    with open(FILE,"w",newline="") as f:

        writer=csv.writer(f)
        writer.writerows(rows)

    show_students()


app=ctk.CTk()

app.title("Student Manager")
app.geometry("700x500")

ctk.CTkLabel(app,text="ID").grid(row=0,column=0,pady=10)
id_entry=ctk.CTkEntry(app)
id_entry.grid(row=0,column=1)

ctk.CTkLabel(app,text="Name").grid(row=1,column=0)
name_entry=ctk.CTkEntry(app)
name_entry.grid(row=1,column=1)

ctk.CTkLabel(app,text="Index").grid(row=2,column=0)
index_entry=ctk.CTkEntry(app)
index_entry.grid(row=2,column=1)

ctk.CTkLabel(app,text="Department").grid(row=3,column=0)
dept_entry=ctk.CTkEntry(app)
dept_entry.grid(row=3,column=1)

ctk.CTkButton(app,text="Add",command=add_student).grid(row=4,column=0)
ctk.CTkButton(app,text="Update",command=update_student).grid(row=4,column=1)
ctk.CTkButton(app,text="Delete",command=delete_student).grid(row=4,column=2)

ctk.CTkButton(app,text="Show All",command=show_students).grid(row=5,column=1)

textbox=ctk.CTkTextbox(app,width=500,height=250)
textbox.grid(row=6,column=0,columnspan=3,pady=20)

app.mainloop()