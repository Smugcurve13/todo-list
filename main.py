while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if "add" in user_action:
        todo = user_action[4:]

        with open('todos.txt','r') as file:
            todos = file.readlines()

        todos.append(todo)

        with open('todos.txt', 'w') as file:
            file.writelines(todos)

    if "show" in user_action:                                               #use "|" to add multiple words for a single case

        with open('todos.txt','r') as file:
            todos = file.readlines()

                                                                # new_todos = [item.strip('\n') for item in todos]
                                                                # use above as ref for list comprehension

        for index , item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)

    if "edit" in user_action:
        number = int(input("Number of the todo to edit:"))
        number = number - 1

        with open('todos.txt','r') as file:
            todos = file.readlines()
        
        new_todo = input("enter new todo:")
        todos[number] = new_todo + '\n'                         # use [] for index of todo in list

        with open('todos.txt', 'w') as file:
            file.writelines(todos)

    if "complete" in user_action:
        number = int(input("Number of the todo to complete: "))
        
        with open('todos.txt','r') as file:
            todos = file.readlines()
        index = number -1
        todo_to_remove = todos[index].strip('\n')
        todos.pop(index)

        with open('todos.txt', 'w') as file:
            file.writelines(todos)

        message = f"Todo {todo_to_remove} was removed from the list"
        print(message)
        
    if "exit" in user_action:
        break
        
print("bye")