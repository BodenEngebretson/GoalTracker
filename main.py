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

def add_entry(Id: int, goal: str):
    data = read(db_file)

    data.append(goal)

    write(db_file, data)

def del_entry( Id: int):
    data = read(db_file)

    data.pop(Id)

    write(db_file)

if __name__ == '__main__':
    add_entry(7, "Hating")
