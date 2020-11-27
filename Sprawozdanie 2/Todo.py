import tkinter
import tkinter.messagebox

root = tkinter.Tk()
root.title("To-Do")

def add_task():
    task = entry_task.get()
    if task != "":
        listbox_tasks.insert(tkinter.END, task)
        entry_task.delete(0,tkinter.END)
    else:
        tkinter.messagebox.showwarning(title="warning", message="Nie można dodać pustego rekordu")

def delete_task():
    task_index = listbox_tasks.curselection()[0]
    listbox_tasks.delete(task_index)


def edit_task():
    task = entry_task.get()
    if task != "":
        task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(task_index)
        listbox_tasks.insert(0, task)
        entry_task.delete(0, tkinter.END)
    else:
        tkinter.messagebox.showwarning(title="warning", message="Nie można dodać pustego rekordu")

listbox_tasks = tkinter.Listbox(root, height=10, width=40)
listbox_tasks.pack()

entry_task = tkinter.Entry(root, width=40)
entry_task.pack()

button_add_task = tkinter.Button(root, text="Dodaj", width=35, command=add_task)
button_add_task.pack()

button_delete_task = tkinter.Button(root, text="Usuń", width=35, command=delete_task)
button_delete_task.pack()

button_edit_task = tkinter.Button(root, text="Edytuj", width=35, command=edit_task)
button_edit_task.pack()










root.mainloop()