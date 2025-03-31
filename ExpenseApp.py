import tkinter as tk

root = tk.Tk()
root.geometry("750x450")
root.title("Expense Tracker App")
root.configure(background="#232323")

def add_item():
    print("i want to add item")
    item = item_text.get()
    quantity= quantity_text.get()
    cost = cost_text.get()
    Total_cost = int(quantity)*int(cost)
    print(item, quantity, cost, Total_cost)
    single_item_lebal = tk.Label(frame2, text=f"{item}\t\t{quantity}\t\t{cost}\t\t{Total_cost}", bg="#232323", fg="#ffffff", font=("Arial", 20))

    single_item_lebal.pack(pady=5)

def clear_button():
    item_text.delete(0, "end")
    quantity_text.delete(0, "end")
    cost_text.delete(0, "end")

title_label = tk.Label(root, text="Expense Tracker", bg="#232323", fg="#ffffff", font=("Arial", 20))

#display the label on the window
title_label.pack(pady=20)

item_label = tk.Label(root, text="Item", bg="#232323", fg="#ffffff", font=("Arial", 20))
item_label.pack(pady=(20, 5))
#creating text box for entry
item_text = tk.Entry(root, font=("Arial", 15))
item_text.pack()

quantity_label = tk.Label(root, text="Quantity", bg="#232323", fg="#ffffff", font=("Arial", 15))
quantity_label.pack(pady=(20, 5))

quantity_text = tk.Entry(root, font=("Arial", 15))
quantity_text.pack()

cost_label = tk.Label(root, text="Cost Per Unit", bg="#232323", fg="#ffffff", font=("Arial", 15))
cost_label.pack(pady=(20, 5))

cost_text = tk.Entry(root, font=("Arial", 15))
cost_text.pack()

frame1 = tk.Frame(root, bg="#232323")

add_button = tk.Button(frame1, text="Add Item", bg="#2a2a2a", fg="#ffffff", font=("Arial", 15), command= add_item)
add_button.pack(padx=10, pady=20, side= tk.LEFT)

clear_button = tk.Button(frame1, text="Clear", bg="#2a2a2a", fg="#ffffff", font=("Arial", 15), command= clear_button)
clear_button.pack(side=tk.RIGHT)

frame1.pack()

display_label = tk.Label(root, text="Expense", bg="#232323", fg="#ffffff", font=("Arial", 20))
display_label.pack(pady=(20, 5))

frame2 = tk.Frame(root, bg="#232323")

heading_label = tk.Label(frame2, text="Item\t\tQuantity\t\tCost Per Unit\t\tTotal cost", bg="#232323", fg="#ffffff", font=("Arial", 20))
heading_label.pack(pady=5)
frame2.pack()

analyse_button = tk.Button(root, text="Analyse", bg="#2a2a2a", fg="#ffffff", font=("Arial", 15))
analyse_button.pack(pady=30)

root.mainloop()