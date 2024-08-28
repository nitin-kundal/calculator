import tkinter as tk

def on_click(button_text):
    current_text = entry.get()
    if button_text == "=":
        try:
            result = eval(current_text)  # Evaluates the expression
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif button_text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, button_text)

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Entry widget for displaying the calculation
entry = tk.Entry(root, width=16, font=("Arial", 24), borderwidth=2, relief="solid")
entry.grid(row=0, column=0, columnspan=4)

# Button definitions
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

# Create and place buttons
for (text, row, col) in buttons:
    button = tk.Button(root, text=text, width=4, height=2, font=("Arial", 18),
                       command=lambda t=text: on_click(t))
    button.grid(row=row, column=col, padx=5, pady=5)

# Run the application
root.mainloop()
