while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    match user_action:
        case "add":
            todo = input("Enter a todo: ") + "\n"

            with open('todos.txt','r') as file:
                todos = file.readlines()

            todos.append(todo)

            with open('todos.txt', 'w') as file:
                file.writelines(todos)

        case "show" :                                               #use "|" to add multiple words for a single case

            with open('todos.txt','r') as file:
                todos = file.readlines()

                                                                    # new_todos = [item.strip('\n') for item in todos]
                                                                    # use above as ref for list comprehension

            for index , item in enumerate(todos):
                item = item.strip('\n')
                row = f"{index + 1}-{item}"
                print(row)

        case 'edit':
            number = int(input("Number of the todo to edit:"))
            number = number - 1

            with open('todos.txt','r') as file:
                todos = file.readlines()
            
            new_todo = input("enter new todo:")
            todos[number] = new_todo + '\n'                         # use [] for index of todo in list

            with open('todos.txt', 'w') as file:
                file.writelines(todos)

        case 'complete':
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
        case "exit":
            break
        
        case _:                                                    # use random variable or _ for giving a command to a text that isnt mentioned in case 
            print("hey , you have entered an unknown command")

print("bye")