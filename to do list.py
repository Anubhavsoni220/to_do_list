#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().system('pip install customtkinter')


# In[23]:


#To-Do List  Pythonapplication
    
import customtkinter  #for additional GUI elements
from tkinter import *
from tkinter import messagebox
from tkinter import PhotoImage , Label,Tk
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk

# Initialize the main window
app = tk.Tk()
app.title("To Do List")
app.geometry("520x400")
app.configure(bg="black")  #  background color

def add_task():  #for addinf new task
    task = task_entry.get()
    if task:
        tasks_list.insert(0,task)
        task_entry.delete(0, END)
        save_task()
    else:
        messagebox.showerror('Error',"Enter a Task")  #to guide for taking input
def remove_task():
    selected= tasks_list.curselection()
    if selected:
        tasks_list.delete(selected[0])
        save_task()

    else:
        messagebox.showerror('Error',"Choose a Task To Delete")  #show error if user didn't put task


def save_task():
    with open("Task.txt", "w") as f:
        task = tasks_list.get(0,END)
        for task in task:
            f.write(task + "/n")

def update_task():
    selected = tasks_list.curselection()
    if selected:
        new_task = task_entry.get()
        if new_task:
            tasks_list.delete(selected[0])
            tasks_list.insert(selected[0], new_task)
            task_entry.delete(0, END)
            save_task()
        else:
            messagebox.showerror('Error', "Enter a Task to Update")   #show error if user didn't put task

    else:
        messagebox.showerror('Error', "Choose a Task to Update")   #show error if user didn't put task


def load_tasks():
    try:
        with open("task.txt", "r") as f:
            task = f.readlines()
            for task in task:
                tasks_list.insert(0,task.strip)

    except FileNotFoundError:
        #messagebox.showerror('Error',"Cannot load Tasks.")
        pass

# Sidebar frame
sidebar = tk.Frame(app, bg="#87CEFA", width=200)
sidebar.pack(side="left", fill="y")

# Sidebar content
profile_pic = tk.Label(sidebar, text="Do-it", bg="white", font=("Arial", 16, "bold"))
profile_pic.pack(pady=10)

username = tk.Label(sidebar, text="Anubhav soni", bg="white", font=("Arial", 14))
username.pack()

menu_items = [ ]
for item in menu_items:
    button = tk.Button(sidebar, text=item, bg="#87CEFA", font=("Arial", 12), bd=0)
    button.pack(fill="x", pady=5, padx=5)


# Main content frame
main_content = tk.Frame(app, bg="grey", width=600, height=600)
main_content.pack(side="right", fill="both", expand=True)

# Main content heading
focus_label = tk.Label(main_content, text="Today's Objective", bg="lightyellow", font=("Arial", 30, "bold"))
focus_label.pack(pady=10)

#Button 

add_button = customtkinter.CTkButton(app,command=add_task ,text_color='black',text='Add Task',fg_color='lightgrey',
  hover_color='#87CEFA',bg_color='#CBC3E3' ,width=130)
add_button.place(x=250,y=150)

remove_button = customtkinter.CTkButton(app,command=remove_task, text_color='black' ,text='Remove Task',fg_color='#CBC3E3',
  hover_color='#87CEFA',bg_color='#CBC3E3' )
remove_button.place(x=155,y=350)

update_button = customtkinter.CTkButton(app, command=update_task,   text_color='black', text='Update Task', fg_color='#CBC3E3',
     hover_color='#87CEFA',  bg_color='#CBC3E3' )
update_button.place(x=350, y=350)


# Add task input

task_entry= customtkinter.CTkEntry(app,text_color='#000',fg_color='#CBC3E3', border_color='lightyellow' ,width=280)
task_entry.place(x=180,y=93)

tasks_list = Listbox(app,width=55,height=8)
tasks_list.place(x=155,y=200)


app.mainloop()


# In[ ]:




