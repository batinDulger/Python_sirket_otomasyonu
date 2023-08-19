import tkinter as tk
import random
import sqlite3
from tkinter import messagebox
from tkinter import PhotoImage
from PIL import Image, ImageTk


class Company():

    def __init__(self):
        self.database()
        self.Table()
        self.employees()
        self.Window()

    def database(self):
        self.con = sqlite3.connect("Company.db")
        self.cursor = self.con.cursor()

    def Table(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS admin_pannel(user_name TEXT, sifre INT)")

    def employees(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS employees_pannel(name TEXT, surname TEXT, ID INT, date_of_birth INT, working_area TEXT, salary INT)")

    def Window(self):

        self.window = tk.Tk()

        self.window.title("Comapny")
        self.window.geometry("350x350")
        self.window.iconbitmap("company_icon.ico")

       # Resmi yükleme ve küçültme
        image = Image.open("admin.png")
        resized_image = image.resize((100, 100)) 
        photo = ImageTk.PhotoImage(resized_image)

        # Resim görüntüleme
        image_label = tk.Label(self.window, image=photo)
        image_label.place(x=0, y=0)

        # Resim görüntüleme
        image_label = tk.Label(self.window, image=photo)
        image_label.place(x=15, y=15, relwidth=0, relheight=0)

        admin_label = tk.Label(self.window, text="User Name:", font=8)
        admin_label.place(x=10, y=120)
        admin_entry = tk.Entry(self.window, width=20)
        admin_entry.place(x=120,y=125)

        password_label = tk.Label(self.window, text="Password:", font=8)
        password_label.place(x=10, y=190)
        password_entry = tk.Entry(self.window, width=20, show="*")
        password_entry.place(x=120,y=195)

        def control():

            kullanici = admin_entry.get()
            
            sifre = password_entry.get()

            self.cursor.execute("SELECT * FROM admin_pannel WHERE user_name = ? AND sifre = ?",(kullanici, sifre))

            result = self.cursor.fetchone()
            if result:
                employee()
            else:
                messagebox.showerror("Error","Your username or password is incorrect")


        def employee():

            top_level = tk.Toplevel()
            top_level.title("Employees")
            top_level.geometry("400x250")

            top_level.iconbitmap("employee_icon.ico")

            def add_employee():

                top_level1 = tk.Toplevel()
                top_level1.geometry("350x350")
                top_level1Label = tk.Label(top_level1)
                top_level1Label.place(x=10,y=15)

                name_label = tk.Label(top_level1,text="Name:",font=12)
                name_label.place(x=10,y=15)

                surname_Label = tk.Label(top_level1,text="Surname:",font=12)
                surname_Label.place(x=10,y=60)

                id_random = random.randint(1000,5000)
                id_label = tk.Label(top_level1,text="ID:",font=12)
                id_label.place(x=10,y=105)

                id_label2 = tk.Label(top_level1,text=id_random,font=12)
                id_label2.place(x=50,y=105)

                date_label = tk.Label(top_level1,text="Date Of Birth:",font=12)
                date_label.place(x=10,y=150)

                working_area = tk.Label(top_level1,text="Working Area:",font=12)
                working_area.place(x=10,y=195)

                salary = tk.Label(top_level1,text="Salary:",font=12)
                salary.place(x=10,y=240)

                # Entry ekleme

                name_entry = tk.Entry(top_level1)
                name_entry.place(x=75,y=20)

                surname_entry = tk.Entry(top_level1)
                surname_entry.place(x=100,y=65)

                date_entry = tk.Entry(top_level1)
                date_entry.place(x=140,y=155)

                working_area_entry = tk.Entry(top_level1)
                working_area_entry.place(x=140,y=200)

                salary_entry = tk.Entry(top_level1)
                salary_entry.place(x=80,y=245)

                def create():

                    name = name_entry.get()
                    surname = surname_entry.get()
                    id_gir = id_random
                    date = date_entry.get()
                    working = working_area_entry.get()
                    salary = salary_entry.get()

                    self.cursor.execute("INSERT INTO employees_pannel VALUES (?,?,?,?,?,?)",(name,surname,id_gir,date,working,salary))
                    self.con.commit()

                    messagebox.showinfo("to inform","your registration has been created")

                button = tk.Button(top_level1,text="Create",font=12,width=17,command=create)
                button.place(x=10,y=280)

            top_level_button = tk.Button(top_level, text="Add Employee",width=17,font=12,command=add_employee)
            top_level_button.place(x=100,y=10)

            def delete_employee():

                top_level1 = tk.Toplevel()
                top_level1.geometry("350x350")
                top_level1Label = tk.Label(top_level1)
                top_level1Label.place(x=10,y=15)

                id_delete = tk.Label(top_level1,text="id number to be deleted:",font=12)
                id_delete.place(x=10,y=15)

                id_entry = tk.Entry(top_level1)
                id_entry.place(x=15,y=70)

                def delete():

                    enter_id = id_entry.get()
                    
                    self.cursor.execute("DELETE FROM employees_pannel WHERE ID = ?", (enter_id,))

                    messagebox.showinfo("Clear","Employee Delete")
                button = tk.Button(top_level1,text="Delete",font=12,command=delete)
                button.place(x=10,y=150)
                    

            top_level_button2 = tk.Button(top_level,text="Delete Employees",width=17,font=12,command=delete_employee)
            top_level_button2.place(x=100,y=75)

            def list_employees():

                top_level1 = tk.Toplevel()
                top_level1.geometry("350x350")
                top_level1Label = tk.Label(top_level1)
                top_level1Label.place(x=10,y=15)

                self.cursor.execute("SELECT * FROM employees_pannel")
                employee1 = self.cursor.fetchall()
                row = 10
                for i in employee1:
                    label = tk.Label(top_level1, text=i)
                    label.place(x=15, y=row)
                    row += 20

            top_level_button3 = tk.Button(top_level,text="List Employees",width=17,font=12,command=list_employees)
            top_level_button3.place(x=100,y=140)

        button_admin = tk.Button(self.window,text="Entrance",font=12, width=8, command=control)
        button_admin.place(x=10,y=280)

        self.window.mainloop()

Company()
