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

def del_entry(Id: int):
    data = read(db_file)
    
    try:
        del data[Id]
    except:
        print("Index out of Range")

    write(db_file, data)

def print_goals():
    data = read(db_file)
    for i, goal in enumerate(data):
        print(i, goal, "\n")

def root():

    game = True

    print("Welcome to my Goal Tracker Application!")

    while game:
        answer = int(input("Would you like to: \n1) Display Goals \n2) Add new Goal \n3) Delete Goal \n0) Quit \n--> "))
        print()
        
        if answer == 1:
            print_goals()
        elif answer == 2:
            print("What goal would you like to add?")
            goal = str(input("--> "))
            add_entry(goal)
        elif answer == 3:
            print("What is the Id of the Goal you want to delete?")
            x = input("--> ")
            x = int(x)
   
            try:
                del_entry(x)
            except IndexOutOfRange:
                print("Id not in List")
            except:
                print("Something Went Wrong")
        else:
            game = False

if __name__ == '__main__':
    root()
