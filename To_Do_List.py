from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("TO-DO-LIST")
root.geometry("400x650")
root.resizable(False, False)
task_list = []

#To Add a task
def addTask():
    task = task_entry.get()
    task_entry.delete(0, END)
    if task:
        with open("tasklist1.txt", 'a') as taskfile:
            taskfile.write(f"\n{task}")
        task_list.append(task)
        listbox.insert(END, task)
# For Delete a task
def deleteTask():
    global task_list
    task = str(listbox.get(ANCHOR))
    if task in task_list:
        task_list.remove(task)
        with open('tasklist1.txt', 'w') as taskfile:
            for task in task_list:
                taskfile.write(task + "\n")
        listbox.delete(ANCHOR)
#Load Tasks from file
def openTaskFile():
    try:
        global task_list
        with open("tasklist1.txt", "r") as taskfile:
            tasks = taskfile.readlines()
        for task in tasks:
            if task.strip():
                task_list.append(task.strip())
                listbox.insert(END, task.strip())
    except FileNotFoundError:
        with open('tasklist1.txt', 'w') as file:
            file.close()

# Logo Image
icon = Image.open("Logo.jpg")
icon_image = ImageTk.PhotoImage(icon)
root.iconphoto(False, icon_image)
#Top bar image
Top = Image.open("topbar.jpg")
Top = Top.resize((400, 100))
topbar = ImageTk.PhotoImage(Top)
topbar_label = Label(root, image=topbar)
topbar_label.pack()
# Title and Heading
todo_label = Label(root, text="TO-DO", font="italic 30 bold", bg="#ADD8E6")
todo_label.place(x=140, y=50)
heading_label = Label(root, text="TASKS", font="Times 20 bold", fg="white", bg="green", padx=40)
heading_label.place(x=100, y=120)
# Task Input Frame
input_frame = Frame(root, width=400, height=50, bg="white")
input_frame.place(x=0, y=170)
task = StringVar()
task_entry = Entry(input_frame, width=18, font="Times 20", bd=0, bg="gray")
task_entry.place(x=10, y=7)
add_button = Button(input_frame, text="ADD", font="Times 20 bold", width=6, bg="blue", fg="white", bd=0, command=addTask)
add_button.place(x=300, y=0)
task_entry.focus()
list_frame = Frame(root, bd=3, width=700, height=280, bg="gray")
list_frame.pack(pady=(140, 0))
listbox = Listbox(list_frame, font=('Times', 12), width=40, height=16, bg="gray", fg="black", cursor="hand2")
listbox.pack(side=LEFT, fill=BOTH, padx=2)
scrollbar = Scrollbar(list_frame)
scrollbar.pack(side=RIGHT, fill=BOTH)
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)
openTaskFile()
delete_button = Button(root, text="DELETE", bd=0, font="Times 20 bold", fg="white", bg="red", command=deleteTask)
delete_button.pack(side=BOTTOM, pady=13)

# Run the Main application
root.mainloop()