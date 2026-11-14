# Assignment: Tkinter Calculator


import re
import tkinter as tk


def press(value):
    """Append a digit or operator to the display."""
    display_var.set(display_var.get() + str(value))


def clear():
    """Reset the display."""
    display_var.set("")


def calculate():
    """Evaluate the expression in the display and show the result."""
    expression = display_var.get()

    if expression == "":
        return

    try:
        expression = re.sub(r"\b0+(\d)", r"\1", expression)

        result = eval(expression)
        if isinstance(result, float) and result.is_integer():
            result = int(result)

        display_var.set(str(result))

    except ZeroDivisionError:
        display_var.set("Cannot divide by 0")
    except Exception:
        display_var.set("Error")




root = tk.Tk()
root.title("tk")
root.geometry("420x440")

display_var = tk.StringVar()
display = tk.Entry(
    root,
    textvariable=display_var,
    font=("Arial", 16),
    justify="right",
    state="readonly",          
    readonlybackground="white",
    width=28
)
display.grid(row=0, column=0, columnspan=3, padx=10, pady=10, ipady=6)


button_layout = [
    ["1", "2", "3"],
    ["4", "5", "6"],
    ["7", "8", "9"],
    ["0", "+", "-"],
    ["*", "/", "="],
]

for r, row_values in enumerate(button_layout, start=1):
    for c, value in enumerate(row_values):
        if value == "=":
            cmd = calculate
        else:
            cmd = lambda v=value: press(v)  

        tk.Button(
            root,
            text=value,
            font=("Arial", 14),
            width=8,
            height=2,
            command=cmd
        ).grid(row=r, column=c, padx=5, pady=5)

tk.Button(
    root,
    text="clear",
    font=("Arial", 14),
    width=8,
    height=2,
    command=clear
).grid(row=6, column=0, padx=5, pady=10)

root.mainloop()
