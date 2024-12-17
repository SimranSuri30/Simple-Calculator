import tkinter as tk

# Function to update the expression in the Entry widget
def button_click(value):
    current_expression = entry.get()
    entry.delete(0, tk.END)  
    entry.insert(tk.END, current_expression + value)  

# Function to evaluate the expression and display the result
def evaluate():
    try:
        result = eval(entry.get())  
        entry.delete(0, tk.END)  
        entry.insert(tk.END, result)  
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Function to clear the expression
def clear():
    entry.delete(0, tk.END)

# Create the main window
window = tk.Tk()
window.title("Simple Calculator")

# Create the Entry widget for displaying the expression and result
entry = tk.Entry(window, width=16, font=("Arial", 24), borderwidth=2, relief="solid", justify="right")
entry.grid(row=0, column=0, columnspan=4)

# Create the calculator buttons
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ('C', 5, 0)
]

# Add buttons to the window
for (text, row, col) in buttons:
    if text == '=':
        button = tk.Button(window, text=text, width=5, height=2, font=("Arial", 18), command=evaluate)
    elif text == 'C':
        button = tk.Button(window, text=text, width=5, height=2, font=("Arial", 18), command=clear)
    else:
        button = tk.Button(window, text=text, width=5, height=2, font=("Arial", 18),
                           command=lambda value=text: button_click(value))
    button.grid(row=row, column=col, padx=5, pady=5)


window.mainloop()
