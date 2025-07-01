import tkinter as tk

def press(num):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(num))

def equal():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Function to clear the entry
def clear():
    entry.delete(0, tk.END)

# Main GUI window
window = tk.Tk()
window.title("Simple Calculator")
window.geometry("500x600")

# Entry field for input/output
entry = tk.Entry(window, font=('Arial', 20), bd=10, relief=tk.RIDGE, justify='right')
entry.grid(row=0, column=0, columnspan=4, ipadx=10, ipady=20, padx=10, pady=10)

# Button layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
]

# Add buttons to the window
for (text, row, col) in buttons:
    if text == '=':
        action = equal
    else:
        action = lambda x=text: press(x)
    tk.Button(window, text=text, padx=20, pady=20, font=('Arial', 14),
              command=action).grid(row=row, column=col, padx=5, pady=5)

# Clear button
tk.Button(window, text='C', padx=20, pady=20, font=('Arial', 14),
          command=clear).grid(row=5, column=0, columnspan=4, sticky="nsew", padx=5, pady=5)

# Run the GUI event loop
window.mainloop()