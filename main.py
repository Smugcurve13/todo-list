todos = []

while True:
    user_action = input("Type add, show or exit: ")
    user_action = user_action.strip()

    match user_action:
        case "add":
            todo = input("Enter a todo: ")
            todos.append(todo)
        case "show" :   #use "|" to add multiple words for a single case
            for item in todos:
                print(item)
        case "exit":
            break
        case _: #use random variable or _ for giving a command to a text that isnt mentioned in case 
            print("hey , you have entered an unknown command")

print("bye")