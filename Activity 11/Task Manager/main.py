import tkinter as tk
from tkinter import messagebox

class Task:
    def __init__(self, name, due_date, priority):
        self.name = name
        self.due_date = due_date
        self.priority = priority
        self.status = "Pending"

    def mark_as_completed(self):
        self.status = "Completed"

class TaskManagerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Task Manager")
        
        self.tasks = []

        self.task_name_label = tk.Label(master, text="Task Name:")
        self.task_name_label.grid(row=0, column=0)
        self.task_name_entry = tk.Entry(master)
        self.task_name_entry.grid(row=0, column=1)

        self.due_date_label = tk.Label(master, text="Due Date:")
        self.due_date_label.grid(row=1, column=0)
        self.due_date_entry = tk.Entry(master)
        self.due_date_entry.grid(row=1, column=1)

        self.priority_label = tk.Label(master, text="Priority:")
        self.priority_label.grid(row=2, column=0)
        self.priority_entry = tk.Entry(master)
        self.priority_entry.grid(row=2, column=1)

        self.add_button = tk.Button(master, text="Add Task", command=self.add_task)
        self.add_button.grid(row=3, columnspan=2)

        self.edit_button = tk.Button(master, text="Edit Task", command=self.edit_task)
        self.edit_button.grid(row=4, columnspan=2)

        self.task_listbox = tk.Listbox(master, height=10, width=50)
        self.task_listbox.grid(row=5, columnspan=2)

        self.view_button = tk.Button(master, text="View Task Details", command=self.view_task)
        self.view_button.grid(row=6, columnspan=2)

        self.delete_button = tk.Button(master, text="Delete Task", command=self.delete_task)
        self.delete_button.grid(row=7, columnspan=2)

    def add_task(self):
        name = self.task_name_entry.get()
        due_date = self.due_date_entry.get()
        priority = self.priority_entry.get()
        if name and due_date and priority:
            task = Task(name, due_date, priority)
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, name)
            messagebox.showinfo("Success", "Task added successfully!")
            self.clear_entry_fields()
        else:
            messagebox.showerror("Error", "Please fill in all fields.")

    def edit_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            name = self.task_name_entry.get()
            due_date = self.due_date_entry.get()
            priority = self.priority_entry.get()
            if name and due_date and priority:
                task = self.tasks[selected_index[0]]
                task.name = name
                task.due_date = due_date
                task.priority = priority
                self.task_listbox.delete(selected_index)
                self.task_listbox.insert(selected_index, name)
                messagebox.showinfo("Success", "Task edited successfully!")
                self.clear_entry_fields()
            else:
                messagebox.showerror("Error", "Please fill in all fields.")
        else:
            messagebox.showerror("Error", "Please select a task to edit.")

    def view_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            task = self.tasks[selected_index[0]]
            messagebox.showinfo("Task Details", f"Name: {task.name}\nDue Date: {task.due_date}\nPriority: {task.priority}\nStatus: {task.status}")
        else:
            messagebox.showerror("Error", "Please select a task.")

    def delete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            self.tasks.pop(selected_index[0])
            self.task_listbox.delete(selected_index)
            messagebox.showinfo("Success", "Task deleted successfully!")
        else:
            messagebox.showerror("Error", "Please select a task to delete.")

    def clear_entry_fields(self):
        self.task_name_entry.delete(0, tk.END)
        self.due_date_entry.delete(0, tk.END)
        self.priority_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()
