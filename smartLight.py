from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Smart calculator")
window['bg'] = "white"
window.resizable(0, 0)

def calc():
    n = var.get()
    if len(n) > 0:
        try:
            t = eval(n)
            print(f"{n} = {t}")
            output['text'] = f"Output: {t}"
            
        except Exception as e:
            messagebox.showerror("None Type data", e)
    else:
        messagebox.showerror("Input size error", "Empty input field, please give some values")

var = StringVar()

# graphical user interface for user input
input_space = Entry(window, textvariable=var, font=('Arial', 11, 'bold'),
                    width=30, fg="black", bg="white", bd=2, relief="groove")
input_space.pack(side='top', padx=12, pady=12)

# create output label
output = Label(window, text="Output appears here", font=('Arial', 11, 'bold'), bg="white", fg="green")
output.pack(side="top", padx=5, pady=5)

# button to calculate the values
btn1 = Button(window, text="Calculate(=)", font=('Arial', 11, 'bold'), width=12,
            fg='white', bg='blue', bd=0, command= lambda: calc())
btn1.pack(side='right', padx=12, pady=12)

btn2 = Button(window, text="Close", font=('Arial', 11, 'bold'), width=12,
            fg='white', bg='blue', bd=0, command= lambda: window.destroy())
btn2.pack(side='right', padx=5, pady=12)

window.mainloop()
