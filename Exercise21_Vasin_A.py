from tkinter import *
import math
def leftClickButton(event):
    weight = float(textboxWeight.get())
    height = float(textboxHeight.get())
    calculateBMI = (weight/math.pow(height/100,2))
    print(calculateBMI)
    if calculateBMI < 18.5:
        labelResult.configure(text=[calculateBMI, '= ผอมเกินไป'])
    elif calculateBMI < 22.9:
        labelResult.configure(text=[calculateBMI, "= ปกติ"])
    elif calculateBMI < 24.9:
        labelResult.configure(text=[calculateBMI, "= น้ำหนักเกิน"])
    elif calculateBMI < 29.9:
        labelResult.configure(text=[calculateBMI, "= อ้วน"])
    else:
        labelResult.configure(text=[calculateBMI, "= อ้วนมาก"])

main = Tk()
labelHeight = Label(main, text="ส่วนสูง(Cm)")
labelHeight.grid(row=0,column=0)
textboxHeight = Entry(main)
textboxHeight.grid(row=0, column=1)

labelWeight = Label(main, text="น้ำหนัก(Kg)")
labelWeight.grid(row=1,column=0)
textboxWeight = Entry(main)
textboxWeight.grid(row=1, column=1)

calculateButton = Button(main, text="คำนวณ")
calculateButton.bind('<Button-1>', leftClickButton)
calculateButton.grid(row=2, column=0)

labelResult = Label(main, text="ผลลัพธ์")
labelResult.grid(row=2, column=1)

main.mainloop()


