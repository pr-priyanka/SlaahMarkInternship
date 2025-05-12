import sqlite3
import datetime
from tkinter import *
from tkinter import messagebox as mb
from tkinter.ttk import Treeview, Scrollbar
from tkcalendar import DateEntry

# Initialize DB
conn = sqlite3.connect("ExpenseTracker.db")
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS ExpenseTracker (
                    ID INTEGER PRIMARY KEY, Date TEXT, Payee TEXT, Description TEXT, 
                    Amount REAL, ModeOfPayment TEXT)''')
conn.commit()

# Initialize Tkinter Window
root = Tk()
root.title('Expense Tracker')
root.geometry('1200x550')

# Variables
desc, amnt, payee, MoP = StringVar(), DoubleVar(), StringVar(), StringVar(value='Cash')

# Data Entry Frame
data_entry_frame = Frame(root)
data_entry_frame.place(x=0, y=30, relwidth=0.25, relheight=0.95)

Label(data_entry_frame, text='Date:').place(x=10, y=50)
date_entry = DateEntry(data_entry_frame, date=datetime.datetime.now().date())
date_entry.place(x=160, y=50)

Label(data_entry_frame, text='Payee:').place(x=10, y=230)
Entry(data_entry_frame, textvariable=payee).place(x=10, y=260)

Label(data_entry_frame, text='Description:').place(x=10, y=100)
Entry(data_entry_frame, textvariable=desc).place(x=10, y=130)

Label(data_entry_frame, text='Amount:').place(x=10, y=180)
Entry(data_entry_frame, textvariable=amnt).place(x=160, y=180)

Label(data_entry_frame, text='Mode of Payment:').place(x=10, y=310)
OptionMenu(data_entry_frame, MoP, 'Cash', 'Cheque', 'Credit Card', 'Debit Card').place(x=160, y=305)

Button(data_entry_frame, text='Add Expense', command=lambda: add_expense()).place(x=10, y=395)

# Button Frame
buttons_frame = Frame(root)
buttons_frame.place(relx=0.25, rely=0.05, relwidth=0.75, relheight=0.21)

Button(buttons_frame, text='Delete Expense', command=lambda: remove_expense()).place(x=30, y=5)
Button(buttons_frame, text='Clear Fields', command=lambda: clear_fields()).place(x=335, y=5)

# Treeview for displaying expenses
tree_frame = Frame(root)
tree_frame.place(relx=0.25, rely=0.26, relwidth=0.75, relheight=0.74)

table = Treeview(tree_frame, columns=('ID', 'Date', 'Payee', 'Description', 'Amount', 'Mode of Payment'))
table.heading('ID', text='S No.')
table.heading('Date', text='Date')
table.heading('Payee', text='Payee')
table.heading('Description', text='Description')
table.heading('Amount', text='Amount')
table.heading('Mode of Payment', text='Mode of Payment')
table.pack(fill=BOTH, expand=True)

def add_expense():
    if not (date_entry.get() and payee.get() and desc.get() and amnt.get()):
        mb.showerror('Missing Data', 'Please fill all fields.')
        return
    cursor.execute('''INSERT INTO ExpenseTracker (Date, Payee, Description, Amount, ModeOfPayment) 
                      VALUES (?, ?, ?, ?, ?)''', 
                   (date_entry.get(), payee.get(), desc.get(), amnt.get(), MoP.get()))
    conn.commit()
    refresh_table()

def remove_expense():
    selected = table.selection()
    if not selected:
        mb.showerror('No Selection', 'Please select a record to delete.')
        return
    record_id = table.item(selected)['values'][0]
    cursor.execute('DELETE FROM ExpenseTracker WHERE ID=?', (record_id,))
    conn.commit()
    refresh_table()

def clear_fields():
    date_entry.set_date(datetime.datetime.now().date())
    payee.set('')
    desc.set('')
    amnt.set(0.0)
    MoP.set('Cash')

def refresh_table():
    for row in table.get_children():
        table.delete(row)
    cursor.execute('SELECT * FROM ExpenseTracker')
    rows = cursor.fetchall()
    for row in rows:
        table.insert('', 'end', values=row)

# Load existing data
refresh_table()

root.mainloop()
