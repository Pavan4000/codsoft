from tkinter import *

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title('To-Do List')
        self.root.geometry('400x650+400+100')
        self.root.resizable(False, False)

        self.tasklist = [] 
        self.task_file = 'taskfile.txt'

        self.create_widgets()
        self.open_task_file()

    def create_widgets(self):
        self.heading = Label(self.root, text='All Tasks', font='lucida 30 bold', fg='black')
        self.heading.place(x=100, y=20)

        self.frame = Frame(self.root, width=400, height=50, bg='white')
        self.frame.place(x=0, y=150)

        self.task_entry = Entry(self.frame, width=18, font='lucida 20 bold', bd=0)
        self.task_entry.place(x=10, y=7)

        self.add_button = Button(self.frame, text='Add', font='lucida 20 bold', width=6, fg='white',
                                 bg='blue', bd=0, command=self.add_task)
        self.add_button.place(x=300, y=0)

        self.frame1 = Frame(self.root, bd=3, width=700, height=280, bg='black')
        self.frame1.pack(pady=(210, 0))

        self.listbox = Listbox(self.frame1, font='lucida 15', width=40, height=16, bg='light blue', fg='white',
                               cursor='hand2')
        self.listbox.pack(side=LEFT, fill=BOTH, padx=2)

        self.delete_button = Button(self.root, text='Delete', font='lucida 20 bold', bg='red', bd=0,
                                    command=self.delete_task)
        self.delete_button.pack(side=BOTTOM, padx=2)

    def open_task_file(self):
        try:
            with open(self.task_file, 'r') as taskfile:
                tasks = taskfile.readlines()
            for task in tasks:
                if task != '\n':
                    self.tasklist.append(task.strip())
                    self.listbox.insert(END, task.strip())
        except FileNotFoundError:
            with open(self.task_file, 'w') as taskfile:
                pass

    def add_task(self):
        task = self.task_entry.get()
        self.task_entry.delete(0, END)
        if task:
            with open(self.task_file, 'a') as taskfile:
                taskfile.write(f'\n{task}')
            self.tasklist.append(task)
            self.listbox.insert(END, task)

    def delete_task(self):
        task = str(self.listbox.get(ANCHOR))
        if task in self.tasklist:
            self.tasklist.remove(task)
            with open(self.task_file, 'w') as taskfile:
                for task in self.tasklist:
                    taskfile.write(task + '\n')
            self.listbox.delete(ANCHOR)


if __name__ == "__main__":
    root = Tk()
    app = ToDoListApp(root)
    root.mainloop()
