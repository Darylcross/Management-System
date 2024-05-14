import tkinter as tk
from tkinter import ttk
from tkinter import *
import pandas as pd
import os
import openpyxl


root = Tk()
root.title("Warehouse Management System")
root.geometry("800x500")

bg=PhotoImage(file="storeroom.png")
canvas1= Canvas(root,bg='white')
canvas1.place(relx=0, rely=0, relwidth=1, relheight=1)
canvas1.create_image(0,0,image=bg,anchor="nw")
canvas1.config(width=800, height=500)

# Create welcome label
welcome_label = Label(root, text="Welcome to the warehouse management system", font=("Arial", 20))
welcome_label.place(relx=0.5, rely=0.2, anchor=CENTER)

# Create action selection label
action_label = Label(root, text="Please select the action:", font=("Arial", 15))
action_label.place(relx=0.5, rely=0.3, anchor=CENTER)

# Create Check Items button
import tkinter as tk
from tkinter import *
import pandas as pd

def open_check_items_window():
    check_items_window = Toplevel(root)
    check_items_window.title("Check Items")
    check_items_window.geometry("1920x1080")
    
    # Split the window in half vertically
    left_frame = Frame(check_items_window, bg='white', width=960, height=1080)
    left_frame.pack(side='left')
    right_frame = Frame(check_items_window, bg='white', width=960, height=1080)
    right_frame.pack(side='right')
    
    # Create label for raw materials
    raw_materials_label = Label(left_frame, text="Raw Materials", font=("Arial", 20))
    raw_materials_label.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.1)
    
    # Create label for product
    product_label = Label(right_frame, text="Product", font=("Arial", 20))
    product_label.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.1)
    
    # Create entry widgets for storage code
    raw_materials_code_entry = Entry(left_frame)
    raw_materials_code_entry.place(relx=0.1, rely=0.2, relwidth=0.8, relheight=0.1)
    product_code_entry = Entry(right_frame)
    product_code_entry.place(relx=0.1, rely=0.2, relwidth=0.8, relheight=0.1)
    
    # Create label to display item information
    raw_materials_info_label = Label(left_frame, text="")
    raw_materials_info_label.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.6)
    product_info_label = Label(right_frame, text="")
    product_info_label.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.6)

    #bind enter key to the button
    raw_materials_code_entry.bind("<Return>", lambda event: search_raw_materials())
    product_code_entry.bind("<Return>", lambda event: search_products())
    
    # Function to search for item in RawMaterials.xlsx
    def search_raw_materials():
        storage_code = raw_materials_code_entry.get()
        existing_data = pd.read_excel('RawMaterials.xlsx', engine='openpyxl')
        item = existing_data.loc[existing_data['Storage code'] == storage_code].astype(str)
        if item.empty:
            raw_materials_info_label.config(text="Item not found.")
        else:
            raw_materials_info_label.config(text=item)

    # Function to search for item in Product.xls
    # Function to search for item in Product.xlsx
    def search_products():
        storage_code = product_code_entry.get()
        existing_data = pd.read_excel('Product.xlsx',engine='openpyxl')
        item = existing_data.loc[existing_data['Storage code'] == storage_code].astype(str)
        if item.empty:
            product_info_label.config(text="Item not found.")
        else:
            product_info_label.config(text=item)

check_items_button = Button(root, text="Check Items", width=20, height=2, command=open_check_items_window)
check_items_button.place(relx=0.5, rely=0.4, anchor=CENTER)



# Create a function to read the "RawMaterials.xlsx" file
def read_raw_materials():
    if os.path.exists('RawMaterials.xlsx'):
        existing_data = pd.read_excel('RawMaterials.xlsx',engine='openpyxl')
    else:
        existing_data = pd.DataFrame(columns=['Name', 'Date of purchase', 'Name of supplier', 'Storage expiration date', 'Storage code', 'Description'])
    return existing_data

def read_products():
    if os.path.exists('Product.xlsx'):
        existing_data2 = pd.read_excel('Product.xlsx', engine='openpyxl')
    else:
        existing_data2 = pd.DataFrame(columns=['Name', 'Date of production', 'Name of customer', 'Product expiration date', 'Storage code',"List of raw materials", 'Description'])
    return existing_data2

def write_raw_materials(data):
    data.to_excel('RawMaterials.xlsx', engine='openpyxl')

def write_products(data):
    data.to_excel('Product.xlsx', engine='openpyxl')

# Create Add Items button
def open_add_items_window():
    add_items_window = Toplevel(root)
    add_items_window.title("Add Items")
    add_items_window.geometry("400x300")

    # Create "Add Product" button
    def open_add_product_window():
        add_product_window = Toplevel(add_items_window)
        add_product_window.title("Add Product")
        add_product_window.geometry("400x300")
        # add widgets to the add_product_window
        def add_to_treeview_and_excel():
            existing_data2 = read_products()
        # Get the values from the entry widgets
            name2 = name2_entry.get()
            date2 = date2_entry.get()
            customer2 = customer2_entry.get()
            exp_date2 = exp_date2_entry.get()
            storage2 = storage2_entry.get()
            list_raw_mat = list_raw_entry.get()
            description2 = description2_entry.get()

        # Append new data to existing dataframe
            new_data2 = {'Name': [name2], 
                'Date of purchase': [date2], 
                'Name of customer': [customer2], 
                'Storage expiration date': [exp_date2], 
                'Storage code': [storage2],
                'List of Raw Materials': [list_raw_mat] ,
                'Description': [description2]}
            new_data_df2 = pd.DataFrame(new_data2)
            existing_data2 = existing_data2.append(new_data_df2, ignore_index=True)
            write_products(existing_data2)

            # check if data.xlsx already exist in local directory
            with pd.ExcelWriter('Product.xlsx', engine='openpyxl') as writer:
                existing_data2.to_excel(writer, sheet_name='Sheet1', index=False)

            # Insert new data into Treeview
            tree.insert("", "end", values=(name2, date2, customer2, exp_date2, storage2, list_raw_mat ,description2))
            # Clear the contents of the entry widgets
            name2_entry.delete(0, 'end')
            date2_entry.delete(0, 'end')
            customer2_entry.delete(0, 'end')
            exp_date2_entry.delete(0, 'end')
            storage2_entry.delete(0, 'end')
            list_raw_entry.delete(0,'end')
            description2_entry.delete(0, 'end')

        root = tk.Tk()
        root.geometry("1920x1080")

        # Create the left frame
        left_frame = ttk.Frame(root)
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        #Create the labels and entry widgets in the left frame
        name2_label = tk.Label(left_frame, text="Name:", font=("Helvetica", 16))
        name2_label.pack(padx=15, pady=15)

        name2_entry = tk.Entry(left_frame, width=50, font=("Helvetica",16))
        name2_entry.pack(padx=15, pady=15)

        date2_label = tk.Label(left_frame, text="Date of product:", font=("Helvetica", 16))
        date2_label.pack(padx=15, pady=15)
        date2_entry = tk.Entry(left_frame, width=50, font=("Helvetica", 16))
        date2_entry.pack(padx=15, pady=15)

        customer2_label = tk.Label(left_frame, text="Name of customer:", font=("Helvetica", 16))
        customer2_label.pack(padx=15, pady=15)
        customer2_entry = tk.Entry(left_frame, width=50, font=("Helvetica", 16))
        customer2_entry.pack(padx=15, pady=15)

        exp_date2_label = tk.Label(left_frame, text="Product expiration date:", font=("Helvetica", 16))
        exp_date2_label.pack(padx=15, pady=15)
        exp_date2_entry = tk.Entry(left_frame, width=50, font=("Helvetica", 16))
        exp_date2_entry.pack(padx=15, pady=15)

        storage2_label = tk.Label(left_frame, text="Storage code:", font=("Helvetica", 16))
        storage2_label.pack(padx=15, pady=15)
        storage2_entry = tk.Entry(left_frame, width=50, font=("Helvetica", 16))
        storage2_entry.pack(padx=15, pady=15)

        list_raw_label = tk.Label(left_frame, text="List of raw materials:", font=("Helvetica", 16))
        list_raw_label.pack(padx=15, pady=15)
        list_raw_entry = tk.Entry(left_frame, width=50, font=("Helvetica", 16))
        list_raw_entry.pack(padx=15, pady=15)

        description2_label = tk.Label(left_frame, text="Description:", font=("Helvetica", 16))
        description2_label.pack(padx=15, pady=15)
        description2_entry = tk.Entry(left_frame, width=50, font=("Helvetica", 16))
        description2_entry.pack(padx=15, pady=15)

        add_button = tk.Button(left_frame, text="Add", font=("Helvetica", 16), command=add_to_treeview_and_excel)
        add_button.pack(padx=15, pady=15)

        right_frame = ttk.Frame(root)
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        tree = ttk.Treeview(right_frame, columns= ('Name', 'Date of production', 'Name of customer', 'Product expiration date', 'Storage code', 'List of raw materials', 'Description'))
        tree.pack(fill=tk.BOTH, expand=True)



        tree.column("Name", width=100)
        tree.column("Date of production", width=100)
        tree.column("Name of customer", width=100)
        tree.column("Product expiration date", width=100)
        tree.column("Storage code", width=100)
        tree.column("List of raw materials", width=100)
        tree.column("Description", width=100)

        scrollbar = Scrollbar(right_frame, orient="vertical", command=tree.yview)
        scrollbar.pack(side=RIGHT, fill=Y)
        tree.configure(yscrollcommand=scrollbar.set)


        tree.heading("Name", text="Name")
        tree.heading("Date of production", text="Date of production")
        tree.heading("Name of customer", text="Name of customer")
        tree.heading("Product expiration date", text="Product expiration date")
        tree.heading("Storage code", text="Storage code")
        tree.heading("List of raw materials", text="List of raw materials")
        tree.heading("Description", text="Description")

        root.mainloop()
        
    add_product_button = Button(add_items_window, text="Add Product", width=20, height=2, command=open_add_product_window)
    add_product_button.place(relx=0.5, rely=0.6, anchor=CENTER)

    # Create "Add Raw Material" button
    def open_add_raw_material_window():
        add_raw_material_window = Toplevel(add_items_window)
        add_raw_material_window.title("Add Raw Material")
        add_raw_material_window.geometry("400x300")
        def add_to_treeview_and_excel():
            existing_data = read_raw_materials()
            # Get the values from the entry widgets
            name = name_entry.get()
            date = date_entry.get()
            supplier = customer_entry.get()
            exp_date = exp_date_entry.get()
            storage = storage_entry.get()
            description = description_entry.get()

                # Append new data to existing dataframe
            new_data = {'Name': [name], 'Date of purchase': [date], 'Name of supplier': [supplier], 'Storage expiration date': [exp_date], 'Storage code': [storage], 'Description': [description]}
            new_data_df = pd.DataFrame(new_data)
            existing_data = existing_data.append(new_data_df, ignore_index=True)
            write_raw_materials(existing_data)

            # check if data.xlsx already exist in local directory
            with pd.ExcelWriter('RawMaterials.xlsx', engine='openpyxl') as writer:
                existing_data.to_excel(writer, sheet_name='Sheet1', index=False)

            # Insert new data into Treeview
            tree.insert("", "end", values=(name, date, supplier, exp_date, storage, description))
            # Clear the contents of the entry widgets
            name_entry.delete(0, 'end')
            date_entry.delete(0, 'end')
            customer_entry.delete(0, 'end')
            exp_date_entry.delete(0, 'end')
            storage_entry.delete(0, 'end')
            description_entry.delete(0, 'end')

        root = tk.Tk()
        root.geometry("1920x1080")

        # Create the left frame
        left_frame = ttk.Frame(root)
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Create the labels and entry widgets in the left frame
        name_label = tk.Label(left_frame, text="Name:", font=("Helvetica", 16))
        name_label.pack(padx=15, pady=15)
        name_entry = tk.Entry(left_frame, width=50, font=("Helvetica",16))
        name_entry.pack(padx=15, pady=15)

        date_label = tk.Label(left_frame, text="Date of purchase:", font=("Helvetica", 16))
        date_label.pack(padx=15, pady=15)
        date_entry = tk.Entry(left_frame, width=50, font=("Helvetica", 16))
        date_entry.pack(padx=15, pady=15)

        customer_label = tk.Label(left_frame, text="Name of supplier:", font=("Helvetica", 16))
        customer_label.pack(padx=15, pady=15)
        customer_entry = tk.Entry(left_frame, width=50, font=("Helvetica", 16))
        customer_entry.pack(padx=15, pady=15)

        exp_date_label = tk.Label(left_frame, text="Storage expiration date:", font=("Helvetica", 16))
        exp_date_label.pack(padx=15, pady=15)
        exp_date_entry = tk.Entry(left_frame, width=50 , font=("Helvetica", 16))
        exp_date_entry.pack(padx=15, pady=15)

        storage_label = tk.Label(left_frame, text="Storage code:", font=("Helvetica", 16))
        storage_label.pack(padx=15, pady=15)
        storage_entry = tk.Entry(left_frame, width=50, font=("Helvetica", 16))
        storage_entry.pack(padx=15, pady=15)

        description_label = tk.Label(left_frame, text="Description:", font=("Helvetica", 16))
        description_label.pack(padx=15, pady=15)
        description_entry = tk.Entry(left_frame, width=50, font=("Helvetica", 16))
        description_entry.pack(padx=15, pady=15)

        # Create the add button
        add_button = ttk.Button(left_frame, text="Add", command=add_to_treeview_and_excel)
        add_button.pack(pady=15)

        # Create the right frame
        right_frame = ttk.Frame(root)
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        # Create the Treeview
        tree = ttk.Treeview(right_frame, columns=("Name", "Date of purchase", "Name of supplier", "Storage expiration date", "Storage code", "Description"), show='headings')
        tree.pack(padx=15, pady=15)

        # Set the heading for each column
        tree.heading("Name", text="Name")
        tree.heading("Date of purchase", text="Date of purchase")
        tree.heading("Name of supplier", text="Name of supplier")
        tree.heading("Storage expiration date", text="Storage expiration date")
        tree.heading("Storage code", text="Storage code")
        tree.heading("Description", text="Description")

        root.mainloop()
        
        
        # add widgets to the add_raw_material_window
        
    add_raw_material_button = Button(add_items_window, text="Add Raw Material", width=20, height=2, command=open_add_raw_material_window)
    add_raw_material_button.place(relx=0.5, rely=0.3, anchor=CENTER)
    
add_items_button = Button(root, text="Add Items", width=20, height=2, command=open_add_items_window)
add_items_button.place(relx=0.5, rely=0.5, anchor=CENTER)

close_btn = Button(root, text="Quit", width=20,height=2,command=root.destroy)
close_btn.place(relx=0.5, rely=0.6, anchor=CENTER)

root.mainloop()





  