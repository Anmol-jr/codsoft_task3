import tkinter as tk
import ast

def on_button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, str(current) + str(value))

def clear_entry():
    entry.delete(0, tk.END)

def calculate_result():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error: " + str(e))

def on_key_press(event):
    key = event.char
    if key.isdigit() or key in ['+', '-', '*', '/', '.', '=']:
        on_button_click(key)
    elif key == '\x08':
        clear_entry()
    elif key == '=':
        calculate_result()

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Entry widget for displaying input and results
entry = tk.Entry(root, width=20, font=('Arial', 14), bd=5, insertwidth=4)
entry.grid(row=0, column=0, columnspan=4)

# Buttons for numbers and operations
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row_val = 1
col_val = 0

for button in buttons:
    tk.Button(root, text=button, padx=20, pady=20, font=('Arial', 14),
              command=lambda btn=button: on_button_click(btn) if btn != '=' else calculate_result()).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Clear button
tk.Button(root, text='C', padx=20, pady=20, font=('Arial', 14), command=clear_entry).grid(row=row_val, column=col_val, columnspan=2)

# Bind key press event
root.bind('<Key>', on_key_press)

# Run the main loop
root.mainloop()