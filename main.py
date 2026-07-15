import json

db_file = 'goals.json'

def open_d():
    with open(db_file, 'r') as f:
        data = json.load(f)

    return data

def add_entry(category, Id: int, goal: str, progress: float):
    new = {"Id": Id, "Goal": goal, "Progress": progress}

    with open(db_file, 'r') as f:
        data = json.load(f)
        
    data["Goals"].append(new)
    
    if category not in data:
        data[category] = []

    with open(db_file, 'w') as f:
        json.dump(data, f, indent=2)
    


def read_d():
    with open(db_file, 'r') as f:
        data = json.load(f)

        for goal in data["Goals"]:
            print(goal['Id'], '-', goal["Goal"], '-', goal['Progress'])    


if __name__ == '__main__':
    add_entry("Goals", 6, "Think I fixed it", 0.35)
    read_d()

    
