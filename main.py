def get_todos(filepath):
    with open(filepath,'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(filepath, todos_arg):                                # filepath,todos_arg are called parameters
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):

        todo = user_action[4:]

        todos = get_todos('todos.txt')                                 # here 'todos.txt' is called argument

        todos.append(todo + '\n') 

        write_todos("todos.txt", todos)

    elif user_action.startswith("show"):                                              

        todos = get_todos('todos.txt')

        for index , item in enumerate(todos):                   # new_todos = [item.strip('\n') for item in todos]
            item = item.strip('\n')                             # use above as ref for list comprehension
            row = f"{index + 1}-{item}"
            print(row)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            print(number)
            number = number - 1

            todos = get_todos('todos.txt')
            
            new_todo = input("enter new todo: ")
            todos[number] = new_todo + '\n'                         # use [] for index of todo in list

            write_todos("todos.txt", todos)
        except ValueError:
            print("Your Command is not valid")
            continue

    elif user_action.startswith("complete"):
        try:    
            number = int(user_action[9:])
            
            todos = get_todos('todos.txt')

            index = number -1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            write_todos("todos.txt", todos)

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