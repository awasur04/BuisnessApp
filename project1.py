import tkinter

window = tkinter.Tk()
window.title("Project 1")


AssemblyCheck = tkinter.IntVar()
AssemblyCheck.set(0)
InputQuantity = 0.0
MaterialCost = 0.0
LaborCost = 0.0
Sales = 0.0
Profit = 0.0
TotalQty = 0.0
MachineHours = 0.0
FinishHours = 0.0
AssemblyHours = 0.0


def button1Press():
    global InputQuantity, AssemblyCheck
    InputQuantity = float(userInput.get())
    if AssemblyCheck.get() == 1:
        CalculateLaborHours()
    else:
        CalculateCosts()

def CalculateLaborHours():
    global MachineHours, FinishHours, AssemblyHours, InputQuantity, LaborCost
    qty = InputQuantity
    MachineHours = MachineHours + (qty*3)
    FinishHours = FinishHours + qty
    AssemblyHours = AssemblyHours + qty
    LaborCost = LaborCost + (MachineHours*20) + (FinishHours*30) + (AssemblyHours*15)
    CalculateCosts()

def CalculateCosts():
    global MaterialCost, Sales, Profit, TotalQty, LaborCost, InputQuantity
    qty = InputQuantity
    Sales = Sales + (qty*150)
    MaterialCost = MaterialCost + (qty*20)
    TotalQty = TotalQty + qty
    Profit = Profit + (Sales - (MaterialCost + LaborCost))
    UpdateLabels()

def UpdateLabels():
    global MaterialCost, Sales, Profit, TotalQty, LaborCost, MachineHours, FinishHours, AssemblyHours
    label2.config(text="Material Costs: $ " + str(MaterialCost))
    label3.config(text="Labor Costs: $ " + str(LaborCost))
    label4.config(text="Sales: $ " + str(Sales))
    label5.config(text="Profit: $ " + str(Profit))
    label6.config(text="Total Qty: " + str(TotalQty))
    label7.config(text="Machinist Hours: " + str(MachineHours))
    label8.config(text="Finishing Hours: " + str(FinishHours))
    label9.config(text="Assembly Hours: " + str(AssemblyHours))


label1 = tkinter.Label(window, text="Quantity ")
label1.grid(row = 0, column = 0)
userInput = tkinter.Entry(window)
userInput.grid(row = 0, column = 1)
assembly = tkinter.Checkbutton(window, text = "Final Assembly: ", variable = AssemblyCheck, onvalue = 1, offvalue = 0)
assembly.grid(row = 0, column = 2)
button1 = tkinter.Button(window, text="Order", command = button1Press)
button1.grid(row = 1, column = 1)

label2 = tkinter.Label(window, text="Material Costs: $ 0.00")
label2.grid(row = 3, column = 1)
label3 = tkinter.Label(window, text="Labor Costs: $ 0.00")
label3.grid(row = 4, column = 1)
label4 = tkinter.Label(window, text="Sales: $ 0.00")
label4.grid(row = 5, column = 1)
label5 = tkinter.Label(window, text="Profit: $ 0.00")
label5.grid(row = 6, column = 1)
label6 = tkinter.Label(window, text="Total Qty: 0.0")
label6.grid(row = 7, column = 1)

label7 = tkinter.Label(window, text="Machinist Hours: 0.0")
label7.grid(row = 0, column = 3)
label8 = tkinter.Label(window, text="Finishing Hours: 0.0")
label8.grid(row = 1, column = 3)
label9 = tkinter.Label(window, text="Assembly Hours: 0.0")
label9.grid(row = 2, column = 3)

window.mainloop()