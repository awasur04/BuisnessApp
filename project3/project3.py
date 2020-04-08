import tkinter
import math
import sqlite3
from tkinter import messagebox

window = tkinter.Tk()
window.title("Project 2")
connection = sqlite3.connect("project3Db.db")
c = connection.cursor()

Orders = []
AssemblyCheck = tkinter.IntVar()
AssemblyCheck.set(0)
InputQuantity = 0
MaterialCost = 0
LaborCost = 0
Sales = 0
Profit = 0
TotalQty = 0
MachineHours = 0
FinishHours = 0
AssemblyHours = 0
TotalMachineHours = 0
TotalFinishHours = 0
TotalAssemblyHours = 0

OrderQuantity = 0
CurrentOrderHours = 0
TotalOrderHours = 0
OrderNumber = 0
FinishWeek = 1

def init():
    global Orders, c, TotalOrderHours, OrderNumber, FinishWeek
    c.execute("SELECT * FROM orders")
    ans = c.fetchall()
    for ordernumber, qty, final, hours in ans:
        Orders.append({"OrderNumber":ordernumber, "Quantity":qty, "Final":final, "Hours":hours})

    for order in Orders:
        OrderNumber = order["OrderNumber"]
        OrderQty = order["Quantity"]
        OrderFinal = order["Final"]
        OrderHours = order["Hours"]
        TotalOrderHours = TotalOrderHours + OrderHours
        FinishWeek = TotalOrderHours / 40
        ActualFinishWeek = math.ceil(FinishWeek)
        CalculateInitCost(OrderQty, OrderFinal, OrderHours)
        box1.insert('end', "Order " + str(OrderNumber) + " || Qty " + str(OrderQty) + " || Final Assembly " + str(OrderFinal) + " || Hours " + str(OrderHours) + " || Finish Week " + str(ActualFinishWeek))

def CalculateInitCost(qty, final, hours):
    global MaterialCost, Sales, Profit, TotalQty, LaborCost, InputQuantity, AssemblyCheck, MachineHours, FinishHours, AssemblyHours, TotalAssemblyHours, TotalFinishHours, TotalMachineHours, TotalOrderHours, CurrentOrderHours
    if (final == 1):
        AssemblyHours = AssemblyHours + qty
        Sales = Sales + (qty*150) + (qty*10)
    else:
        Sales = Sales + (qty*150)
    MachineHours = MachineHours + (qty*3)
    FinishHours = FinishHours + qty
    CurrentOrderHours = CurrentOrderHours + AssemblyHours + FinishHours + MachineHours
    
    MaterialCost = MaterialCost + (qty*20)
    TotalQty = TotalQty + qty
    LaborCost = LaborCost + (MachineHours*20) + (FinishHours*30) + (AssemblyHours*15)

    Profit = (Sales - (MaterialCost + LaborCost))

    TotalAssemblyHours = TotalAssemblyHours + AssemblyHours
    TotalFinishHours = TotalFinishHours + FinishHours
    TotalMachineHours = TotalMachineHours + MachineHours
    UpdateLabels()
    ResetVariables()
    

def button1Press():
    global InputQuantity, AssemblyCheck, OrderQuantity, OrderNumber
    OrderNumber += 1       
    InputQuantity = EntryCheck(userInput.get())
    if not InputQuantity:
        messagebox.showerror("Error", "Please only input whole numbers")
    else:
        OrderQuantity = InputQuantity
        if AssemblyCheck.get() == 1:
            CalculateLaborHours()
        else:
            CalculateCosts()

def EntryCheck(input):
    if input == "": 
        return False
    try:
        InputQuantity =  int(input)
    except ValueError:
        return False
    return InputQuantity

def CalculateLaborHours():
    global AssemblyHours, InputQuantity
    AssemblyHours = AssemblyHours + InputQuantity
    CalculateCosts()

def CalculateCosts():
    global OrderNumber, MaterialCost, Sales, Profit, TotalQty, LaborCost, InputQuantity, AssemblyCheck, MachineHours, FinishHours, AssemblyHours, TotalAssemblyHours, TotalFinishHours, TotalMachineHours, TotalOrderHours, CurrentOrderHours
    qty = InputQuantity
   
    MachineHours = MachineHours + (qty*3)
    FinishHours = FinishHours + qty
    CurrentOrderHours = CurrentOrderHours + AssemblyHours + FinishHours + MachineHours
    TotalOrderHours = TotalOrderHours + CurrentOrderHours

    if (AssemblyCheck.get() == 1):
        Sales = Sales + (qty*150) + (qty*10)
        Assembly = 1
    else:
        Sales = Sales + (qty*150)
        Assembly = 2
    
    MaterialCost = MaterialCost + (qty*20)
    TotalQty = TotalQty + qty
    LaborCost = LaborCost + (MachineHours*20) + (FinishHours*30) + (AssemblyHours*15)

    Profit = (Sales - (MaterialCost + LaborCost))

    TotalAssemblyHours = TotalAssemblyHours + AssemblyHours
    TotalFinishHours = TotalFinishHours + FinishHours
    TotalMachineHours = TotalMachineHours + MachineHours

    Orders.append({"OrderNumber":OrderNumber, "Quantity":qty, "Final":Assembly, "Hours":CurrentOrderHours})

    UpdateList()
    UpdateLabels()
    ResetVariables()

def ResetVariables():
    global AssemblyHours, FinishHours, MachineHours, OrderQuantity, CurrentOrderHours
    AssemblyHours = 0
    FinishHours = 0
    MachineHours = 0
    OrderQuantity = 0
    CurrentOrderHours = 0

def UpdateLabels():
    global MaterialCost, Sales, Profit, TotalQty, LaborCost, MachineHours, FinishHours, AssemblyHours, TotalAssemblyHours, TotalFinishHours, TotalMachineHours
    label2.config(text="Material Costs: $ " + str(MaterialCost))
    label3.config(text="Labor Costs: $ " + str(LaborCost))
    label4.config(text="Sales: $ " + str(Sales))
    label5.config(text="Profit: $ " + str(Profit))
    label6.config(text="Total Qty: " + str(TotalQty))
    label7.config(text="Machinist Hours: " + str(TotalMachineHours))
    label8.config(text="Finishing Hours: " + str(TotalFinishHours))
    label9.config(text="Assembly Hours: " + str(TotalAssemblyHours))

def UpdateList():
    global OrderQuantity, TotalOrderHours, AssemblyCheck, CurrentOrderHours, OrderNumber, FinishWeek, c, connection
    Assembly = "No"
    if (AssemblyCheck.get() == 1):
        Assembly = 1
    else:
        Assembly = 0

    FinishWeek = TotalOrderHours / 40
    ActualFinishWeek = math.ceil(FinishWeek)
    
    
    box1.insert('end', "Order " + str(OrderNumber) + " || Qty " + str(OrderQuantity) + " || Final Assembly " + str(Assembly) + " || Hours " + str(CurrentOrderHours) + " || Finish Week " + str(ActualFinishWeek))
    c.execute("INSERT INTO orders VALUES (?, ?, ?, ?)", (OrderNumber, OrderQuantity, Assembly, CurrentOrderHours))

def button2Press():
    selection = box1.curselection()
    selectionIndex = int(''.join(map(str, selection)))
    delOrderNumber = Orders[selectionIndex]["OrderNumber"]
    UpdateRemovedLabels(Orders[selectionIndex])
    box1.delete(selection[0])
    query = "DELETE FROM orders WHERE id=?"
    c.execute(query, (delOrderNumber,))
    del Orders[selectionIndex]

def UpdateRemovedLabels(order):
    global MaterialCost, Sales, Profit, TotalQty, LaborCost, InputQuantity, AssemblyCheck, MachineHours, FinishHours, AssemblyHours, TotalAssemblyHours, TotalFinishHours, TotalMachineHours, TotalOrderHours, CurrentOrderHours
    ResetVariables()
    TempQty = order["Quantity"]
    TempFinal = order["Final"]

    if (int(TempFinal) == 1):
        AssemblyHours = AssemblyHours - TempQty
        Sales = Sales - (TempQty*150) - (TempQty*10)
    else:
        Sales = Sales - (TempQty*150)
    MachineHours = MachineHours - (TempQty*3)
    FinishHours = FinishHours - TempQty
    
    MaterialCost = MaterialCost - (TempQty*20)
    TotalQty = TotalQty - TempQty
    LaborCost = LaborCost + (MachineHours*20) + (FinishHours*30) + (AssemblyHours*15)

    Profit = (Sales - (MaterialCost + LaborCost))

    TotalAssemblyHours = TotalAssemblyHours + AssemblyHours
    TotalFinishHours = TotalFinishHours + FinishHours
    TotalMachineHours = TotalMachineHours + MachineHours
    UpdateLabels()

def on_closing():
    connection.commit()
    connection.close()
    window.destroy()

label1 = tkinter.Label(window, text="Quantity ") 
label1.grid(row = 0, column = 0)
userInput = tkinter.Entry(window)
userInput.grid(row = 0, column = 1)
assembly = tkinter.Checkbutton(window, text = "Final Assembly", variable = AssemblyCheck, onvalue = 1, offvalue = 0)
assembly.grid(row = 1, column = 0)
button1 = tkinter.Button(window, text="Order", command = button1Press)
button1.grid(row = 1, column = 1)
button2 = tkinter.Button(window, text="Delete Selected Order", command = button2Press)
button2.grid(row = 14, column = 2)

divider1 = tkinter.Label(window, text="-----------------")           
divider1.grid(row = 2, column = 0)
label2 = tkinter.Label(window, text="Material Costs: $ "  + str(MaterialCost))           
label2.grid(row = 3, column = 0)
label3 = tkinter.Label(window, text="Labor Costs: $ "  + str(LaborCost))
label3.grid(row = 4, column = 0)
label4 = tkinter.Label(window, text="Sales: $ " + str(Sales))
label4.grid(row = 5, column = 0)
label5 = tkinter.Label(window, text="Profit: $ "  + str(Profit))
label5.grid(row = 6, column = 0)
label6 = tkinter.Label(window, text="Total Qty: "  + str(TotalQty))
label6.grid(row = 7, column = 0)

divider2 = tkinter.Label(window, text="-----------------")           
divider2.grid(row = 8, column = 0)
label7 = tkinter.Label(window, text="Machinist Hours: " + str(TotalMachineHours))
label7.grid(row = 9, column = 0)
label8 = tkinter.Label(window, text="Finishing Hours: " + str(TotalFinishHours))
label8.grid(row = 10, column = 0)
label9 = tkinter.Label(window, text="Assembly Hours: " + str(TotalAssemblyHours))
label9.grid(row = 11, column = 0)

label10 = tkinter.Label(window, text="Production Planning")
label10.grid(row=0, column=2)
box1 = tkinter.Listbox(window, height = 15, width = 70, selectmode = "SINGLE")
box1.grid(row = 1, column = 2, columnspan = 8, rowspan = 12, sticky="E", padx = 10, pady = 10)
init()
window.protocol("WM_DELETE_WINDOW", on_closing)
window.mainloop()