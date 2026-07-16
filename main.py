import json

db_file = 'goals.json'

def write(filename, data):
    with open(db_file, 'w') as f:
        json.dump(data, f, indent=2)

def read(filename):
    try:
        with open(db_file, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        raise {}

def add_entry(goal: str):
    data = read(db_file)
    try:
        data.append(goal)
    finally:

        write(db_file, data)

def del_entry( Id: int):
    data = read(db_file)
    
    try:
        data.pop(Id)
    finally:
        write(db_file)

def print_goals():
    data = read(db_file)
    print(data)

def root():
    print("Welcome to my Goal Tracker Application!")
    answer = int(input("Would you like to: \n1) Display Goals\n2) Add new Goal \n3) Delete Goal\n-->"))
    
    if answer == 1:
        print_goals()
    elif answer == 2:
        print("What goal would you like to add?")
        goal = str(input("-->"))
        add_entry(goal)
    elif answer == 3:
        print("What is the Id of the Goal you want to delete?")
        x = input("-->")
        try:
            del_entry(int(x))
            print("Success")
        except:
            print("Something Went Wrong")




if __name__ == '__main__':
    root()
