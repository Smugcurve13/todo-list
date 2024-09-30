FILEPATH = "todos.txt"

def get_todos(filepath = FILEPATH):
    """" Read a text file and return the list of to-do items."""
    with open(filepath,'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg,filepath = FILEPATH):                                # filepath,todos_arg are called parameters
    """" Write a To-do items list in the text file"""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)
        
if __name__ == "__main__":                                              # this if statement is used to ensure only functions are called from this file in the main.py file
    print("hello")                                                     
    print(get_todos())