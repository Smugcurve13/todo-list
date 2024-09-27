def get_todos(filepath="todos.txt"):
    """" Read a text file and return the list of to-do items."""
    with open(filepath,'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg,filepath='todos.txt'):                                # filepath,todos_arg are called parameters
    """" Write a To-do items list in the text file"""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):

        todo = user_action[4:]

        todos = get_todos()                                 # here 'todos.txt' is called argument

        todos.append(todo + '\n') 

        write_todos(todos)

    elif user_action.startswith("show"):                                              

        todos = get_todos()

        for index , item in enumerate(todos):                   # new_todos = [item.strip('\n') for item in todos]
            item = item.strip('\n')                             # use above as ref for list comprehension
            row = f"{index + 1}-{item}"
            print(row)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            print(number)
            number = number - 1

            todos = get_todos()
            
            new_todo = input("enter new todo: ")
            todos[number] = new_todo + '\n'                         # use [] for index of todo in list

            write_todos(todos)
        except ValueError:
            print("Your Command is not valid")
            continue

    elif user_action.startswith("complete"):
        try:    
            number = int(user_action[9:])
            
            todos = get_todos()

            index = number -1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            write_todos(todos)

            message = f"Todo {todo_to_remove} was removed from the list"
            print(message)
        except IndexError:
            print("There is no item with that number")
            continue

    elif user_action.startswith("exit"):
        break
    else:
        print("Command is not valid.")

print("bye")