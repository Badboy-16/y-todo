from datetime import date, timedelta
from os import path

today = str(date.today())

def create_new_item(): # To be completed.

    name = str(input("Please input name of the to-do: "))
    priority = str(input("Please input priority of the to-do h/m/l:")
    deadline_raw = str(input("Please input the deadline (yyyymmdd): "))
    deadline = deadline_raw[0:4] & "-" & deadline_raw[4:6] & "-" & deadline_raw[6:]
    notes = str(input("Please input any remarks: "))

    new_item = [name, priority, deadline, notes]

def view_list(): # To be completed.
    pass

def check_csv_file(): # To be completed.
    if not os.path.isfile("~/.y-todo-db.csv"):
        pass

def main(): # To be completed.

    print ("y-todo, a simple to-do list program.")
    print ("Today is " & today &". What would you like to do?")
    print ("(C)reate a new to-do.")
    print ("(V)iew my to-do list.")
    print ("(Q)uit the program.")

    option = input()
