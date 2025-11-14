from tkinter import *

window = Tk()
window.title("My first GUI")
window.minsize(width=400, height=200)
window.config(padx=20, pady=20)

def button_clicked():
    my_label2.config(text=f"{int(my_input.get())*1.609344:.2f}")

my_label = Label(text="is equal to", font=("Arcial", 18))
my_label.grid(row=1, column=0, padx=10, pady=10)

my_label2 = Label(text="0", font=("Arial", 18))
my_label2.grid(row=1, column=1, padx=10, pady=10)

my_label3 = Label(text="Km", font=("Arial", 18))
my_label3.grid(row=1, column=2, padx=10, pady=10)

my_label4 = Label(text="Miles", font=("Arial", 18))
my_label4.grid(row=0, column=2, padx=10, pady=10)


my_input = Entry(width=10, justify="center", font=("Arial", 18))
my_input.grid(row=0, column=1, padx=10, pady=10)

my_button = Button(text="Calculate", font=("Arial", 14), command=button_clicked)
my_button.grid(row=2, column=1, padx=10, pady=10)

window.mainloop()