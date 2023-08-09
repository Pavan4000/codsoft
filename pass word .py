import tkinter as tk
import random
import string

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("400x400")
        self.root.resizable(False, False)
        self.root.title("Password Generator")

        self.passstr = tk.StringVar()
        self.user_name = tk.StringVar()
        self.pwd_len = tk.IntVar()
        self.accepted_passwords = []

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="PASSWORD GENERATOR", bg="skyblue", font="arial 18").pack()

        tk.Label(self.root, bg="pink", text="Enter user name").place(x=15, y=54)
        tk.Entry(self.root, width=10, textvariable=self.user_name).place(x=200, y=55)

        tk.Label(self.root, bg="pink", text="Enter the length of the password").place(x=15, y=97)
        tk.Entry(self.root, width=10, textvariable=self.pwd_len).place(x=200, y=100)

        tk.Label(self.root, bg="pink", text="Generated Password").place(x=15, y=140)
        tk.Entry(self.root, textvariable=self.passstr, width=30).place(x=200, y=140)

        tk.Button(self.root, text="Generate Password", bg="orange", command=self.get_pass).place(x=140, y=200)
        tk.Button(self.root, text="Accept", bg="green", command=self.saved).place(x=170, y=250)
        tk.Button(self.root, text="Reset", bg="red", command=self.remove).place(x=174, y=300)

    def get_pass(self):
        pass1 = string.ascii_letters + string.digits + string.punctuation
        password = ""
        for _ in range(self.pwd_len.get()):
            password += random.choice(pass1)
        self.passstr.set(password)

    def saved(self):
        name = self.user_name.get()
        passcode = self.passstr.get()
        self.accepted_passwords.append((name, passcode))
        print("\nUser_Name:", name)
        print("Accepted_password:", passcode)

    def remove(self):
        self.passstr.set("")
        self.pwd_len.set("")
        self.user_name.set()

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
