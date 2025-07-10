from tkinter import *

window = Tk()
window.title("Miles to Kilometers Converter")
window.minsize(width=200, height=100)

entry = Entry(width=10)
entry.grid(column=1,row=0)

mile_label=Label(text="Miles")
mile_label.grid(column=2,row=0)

equal_to_label=Label(text="is equal to ")
equal_to_label.grid(column=0,row=1)

result_label = Label(text="0")
result_label.grid(column=1, row=1)

km_label=Label(text="Km")
km_label.grid(column=2,row=1)

def convert():
    user_input = entry.get()
    output=float(user_input)*1.609
    result_label.config(text=output)

button = Button(text="Convert", command=convert)
button.grid(column=1,row=2)


window.mainloop()



