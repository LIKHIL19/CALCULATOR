import tkinter as tk

root = tk.Tk()
calculation = ""

def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert("1.0", calculation)

def evaluate_calculation():
    global calculation
    try:
        calculation = str(eval(calculation))
        text_result.delete(1.0, "end")
        text_result.insert("1.0", calculation)
    except:
        clear_field()
        text_result.insert("1.0", "Error")

def clear_field():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")
    text_result.insert("1.0", "0")

root.geometry("400x500")
root.title("Calculator")
root.resizable(False, False)
root.config(bg="black")

text_result = tk.Text(root, height=2, font=("Arial", 24), bg="black", fg="white")
text_result.grid(row=0, column=0, columnspan=4, sticky="nsew")

for i in range(6):
    root.grid_rowconfigure(i, weight=1)
for j in range(4):
    root.grid_columnconfigure(j, weight=1)

btn_open = tk.Button(root, text="(", command=lambda: add_to_calculation("("), font=("Arial", 18), bd=0, bg="white", fg="black")
btn_open.grid(row=1, column=0, sticky="nsew")

btn_close = tk.Button(root, text=")", command=lambda: add_to_calculation(")"), font=("Arial", 18), bd=0, bg="white", fg="black")
btn_close.grid(row=1, column=1, sticky="nsew")

btn_clear = tk.Button(root, text="C", command=clear_field, font=("Arial", 18), bd=0, bg="white", fg="black")
btn_clear.grid(row=1, column=2, sticky="nsew")

btn_div = tk.Button(root, text="/", command=lambda: add_to_calculation("/"), font=("Arial", 18), bd=0, bg="white", fg="black")
btn_div.grid(row=1, column=3, sticky="nsew")

btn_7 = tk.Button(root, text="7", command=lambda: add_to_calculation(7), font=("Arial", 18), bd=0, bg="white", fg="black")
btn_7.grid(row=2, column=0, sticky="nsew")

btn_8 = tk.Button(root, text="8", command=lambda: add_to_calculation(8), font=("Arial", 18), bd=0, bg="white", fg="black")
btn_8.grid(row=2, column=1, sticky="nsew")

btn_9 = tk.Button(root, text="9", command=lambda: add_to_calculation(9), font=("Arial", 18), bd=0, bg="white", fg="black")
btn_9.grid(row=2, column=2, sticky="nsew")

btn_mul = tk.Button(root, text="*", command=lambda: add_to_calculation("*"), font=("Arial", 18), bd=0, bg="white", fg="black")
btn_mul.grid(row=2, column=3, sticky="nsew")

btn_4 = tk.Button(root, text="4", command=lambda: add_to_calculation(4), font=("Arial", 18), bd=0, bg="white", fg="black")
btn_4.grid(row=3, column=0, sticky="nsew")

btn_5 = tk.Button(root, text="5", command=lambda: add_to_calculation(5), font=("Arial", 18), bd=0, bg="white", fg="black")
btn_5.grid(row=3, column=1, sticky="nsew")

btn_6 = tk.Button(root, text="6", command=lambda: add_to_calculation(6), font=("Arial", 18), bd=0, bg="white", fg="black")
btn_6.grid(row=3, column=2, sticky="nsew")

btn_sub = tk.Button(root, text="-", command=lambda: add_to_calculation("-"), font=("Arial", 18), bd=0, bg="white", fg="black")
btn_sub.grid(row=3, column=3, sticky="nsew")

btn_1 = tk.Button(root, text="1", command=lambda: add_to_calculation(1), font=("Arial", 18), bd=0, bg="white", fg="black")
btn_1.grid(row=4, column=0, sticky="nsew")

btn_2 = tk.Button(root, text="2", command=lambda: add_to_calculation(2), font=("Arial", 18), bd=0, bg="white", fg="black")
btn_2.grid(row=4, column=1, sticky="nsew")

btn_3 = tk.Button(root, text="3", command=lambda: add_to_calculation(3), font=("Arial", 18), bd=0, bg="white", fg="black")
btn_3.grid(row=4, column=2, sticky="nsew")

btn_add = tk.Button(root, text="+", command=lambda: add_to_calculation("+"), font=("Arial", 18), bd=0, bg="white", fg="black")
btn_add.grid(row=4, column=3, sticky="nsew")

btn_0 = tk.Button(root, text="0", command=lambda: add_to_calculation(0), font=("Arial", 18), bd=0, bg="white", fg="black")
btn_0.grid(row=5, column=0, sticky="nsew")

btn_equal = tk.Button(root, text="=", command=evaluate_calculation, font=("Arial", 18), bd=0, bg="white", fg="black")
btn_equal.grid(row=5, column=1, columnspan=3, sticky="nsew")

root.mainloop()
