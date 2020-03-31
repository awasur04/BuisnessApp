import tkinter
import math

window = tkinter.Tk()
window.title("Project 2")


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
TotalMachineHours = 0.0
TotalFinishHours = 0.0
TotalAssemblyHours = 0.0

OrderQuantity = 0.0
CurrentOrderHours = 0.0
TotalOrderHours = 0.0
OrderNumber = 1

def button1Press():
    global InputQuantity, AssemblyCheck, OrderQuantity             
    InputQuantity = float(userInput.get())
    OrderQuantity = InputQuantity
    if AssemblyCheck.get() == 1:
        CalculateLaborHours()
    else:
        CalculateCosts()

def CalculateLaborHours():
    global AssemblyHours, InputQuantity
    AssemblyHours = AssemblyHours + InputQuantity
    CalculateCosts()

def CalculateCosts():
    global MaterialCost, Sales, Profit, TotalQty, LaborCost, InputQuantity, AssemblyCheck, MachineHours, FinishHours, AssemblyHours, TotalAssemblyHours, TotalFinishHours, TotalMachineHours, TotalOrderHours, CurrentOrderHours
    qty = InputQuantity
   
    MachineHours = MachineHours + (qty*3)
    FinishHours = FinishHours + qty
    CurrentOrderHours = CurrentOrderHours + AssemblyHours + FinishHours + MachineHours
    TotalOrderHours = TotalOrderHours + CurrentOrderHours

    if (AssemblyCheck.get() == 1):
        Sales = Sales + (qty*150) + (qty*10)
    else:
        Sales = Sales + (qty*150)
    
    MaterialCost = MaterialCost + (qty*20)
    TotalQty = TotalQty + qty
    LaborCost = LaborCost + (MachineHours*20) + (FinishHours*30) + (AssemblyHours*15)

    Profit = (Sales - (MaterialCost + LaborCost))

    TotalAssemblyHours = TotalAssemblyHours + AssemblyHours
    TotalFinishHours = TotalFinishHours + FinishHours
    TotalMachineHours = TotalMachineHours + MachineHours

    UpdateList()
    UpdateLabels()
    ResetVariables()

def ResetVariables():
    global AssemblyHours, FinishHours, MachineHours, OrderQuantity, CurrentOrderHours
    AssemblyHours = 0.0
    FinishHours = 0.0
    MachineHours = 0.0
    OrderQuantity = 0.0
    CurrentOrderHours = 0.0

def UpdateLabels():
    global MaterialCost, Sales, Profit, TotalQty, LaborCost, MachineHours, FinishHours, AssemblyHours
    label2.config(text="Material Costs: $ " + str(MaterialCost))
    label3.config(text="Labor Costs: $ " + str(LaborCost))
    label4.config(text="Sales: $ " + str(Sales))
    label5.config(text="Profit: $ " + str(Profit))
    label6.config(text="Total Qty: " + str(TotalQty))
    label7.config(text="Machinist Hours: " + str(TotalMachineHours))
    label8.config(text="Finishing Hours: " + str(TotalFinishHours))
    label9.config(text="Assembly Hours: " + str(TotalAssemblyHours))

def UpdateList():
    global OrderQuantity, TotalOrderHours, AssemblyCheck, CurrentOrderHours, OrderNumber
    Assembly = "No"
    FinishWeek = 1.0
    if (AssemblyCheck.get() == 1):
        Assembly = "Yes"
    else:
        Assembly = "No"

    FinishWeek = TotalOrderHours / 40
    ActualFinishWeek = math.ceil(FinishWeek)
    
    box1.insert('end', "Order " + str(OrderNumber) + " || Qty " + str(OrderQuantity) + " || Final Assembly " + Assembly + " || Hours " + str(CurrentOrderHours) + " || Finish Week " + str(ActualFinishWeek))
    OrderNumber += 1

label1 = tkinter.Label(window, text="Quantity ") 
label1.grid(row = 0, column = 0)
userInput = tkinter.Entry(window)
userInput.grid(row = 0, column = 1)
assembly = tkinter.Checkbutton(window, text = "Final Assembly", variable = AssemblyCheck, onvalue = 1, offvalue = 0)
assembly.grid(row = 1, column = 0)
button1 = tkinter.Button(window, text="Order", command = button1Press)
button1.grid(row = 1, column = 1)

divider1 = tkinter.Label(window, text="-----------------")           
divider1.grid(row = 2, column = 0)
label2 = tkinter.Label(window, text="Material Costs: $ 0.00")           
label2.grid(row = 3, column = 0)
label3 = tkinter.Label(window, text="Labor Costs: $ 0.00")
label3.grid(row = 4, column = 0)
label4 = tkinter.Label(window, text="Sales: $ 0.00")
label4.grid(row = 5, column = 0)
label5 = tkinter.Label(window, text="Profit: $ 0.00")
label5.grid(row = 6, column = 0)
label6 = tkinter.Label(window, text="Total Qty: 0.0")
label6.grid(row = 7, column = 0)

divider2 = tkinter.Label(window, text="-----------------")           
divider2.grid(row = 8, column = 0)
label7 = tkinter.Label(window, text="Machinist Hours: 0.0")
label7.grid(row = 9, column = 0)
label8 = tkinter.Label(window, text="Finishing Hours: 0.0")
label8.grid(row = 10, column = 0)
label9 = tkinter.Label(window, text="Assembly Hours: 0.0")
label9.grid(row = 11, column = 0)

label10 = tkinter.Label(window, text="Production Planning")
label10.grid(row=0, column=2)
box1 = tkinter.Listbox(window, height = 15, width = 70)
box1.grid(row = 1, column = 2, columnspan = 8, rowspan = 12, sticky="E", padx = 10, pady = 10)

window.mainloop()