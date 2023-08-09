# Import the required modules from tkinter
from tkinter import Tk, Entry, Button, StringVar

# Globally declare the expression variable to store the user's input
expression = ""

# Function to update the expression in the text entry box
def press(num):
    global expression
    # Concatenate the pressed button value to the existing expression
    expression = expression + str(num)
    # Update the expression in the text entry box
    equation.set(expression)

# Function to evaluate the final expression when the "=" button is pressed
def equalpress():
    try:
        global expression
        # Evaluate the expression using the eval() function
        total = str(eval(expression))
        # Display the result in the text entry box
        equation.set(total)
        # Reset the expression variable to an empty string for future calculations
        expression = ""
    except:
        # Handle any errors that may occur during the evaluation
        equation.set("Error")
        expression = ""

# Function to clear the contents of the text entry box
def clear():
    global expression
    expression = ""
    # Clear the text entry box by setting its value to an empty string
    equation.set("")

# Create the main GUI window
gui = Tk()
gui.title("Simple Calculator")  # Set the title of the window
gui.configure(background="light green")  # Set the background color

# Create a variable to store the expression for the text entry box
equation = StringVar()

# Create the text entry box to show the expression
expression_field = Entry(gui, textvariable=equation)
expression_field.grid(columnspan=4, ipadx=70)  # Place the text entry box in the window

# Create the number buttons (0-9) and place them in the window
for i in range(1, 10):
    btn = Button(gui, text=f" {i} ", fg="black", bg="red", command=lambda n=i: press(n), height=1, width=7)
    btn.grid(row=(i - 1) // 3 + 2, column=(i - 1) % 3)

# Create the button for number 0 and place it in the window
button0 = Button(gui, text=" 0 ", fg="black", bg="red", command=lambda: press(0), height=1, width=7)
button0.grid(row=5, column=0)

# Create operator buttons (+, -, *, /) and place them in the window
operators = ["+", "-", "*", "/"]
for i, operator in enumerate(operators):
    btn_operator = Button(gui, text=f" {operator} ", fg="black", bg="red", command=lambda op=operator: press(op),
                          height=1, width=7)
    btn_operator.grid(row=i + 2, column=3)

# Create the equal (=) button and place it in the window
equal = Button(gui, text=" = ", fg="black", bg="red", command=equalpress, height=1, width=7)
equal.grid(row=5, column=2)

# Create the "Clear" button and place it in the window
clear_btn = Button(gui, text="Clear", fg="black", bg="red", command=clear, height=1, width=7)
clear_btn.grid(row=5, column=1)

# Create the decimal (.) button and place it in the window
decimal = Button(gui, text=".", fg="black", bg="red", command=lambda: press('.'), height=1, width=7)
decimal.grid(row=6, column=0)

# Start the GUI event loop
gui.mainloop()
