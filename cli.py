# from functions import get_todos, write_todos
# second method
import functions
import time

now =  time.strftime("%b, %d ,%Y %H:%M:%S")
print(now)
# todos = []

while True:
    user_action = input('Type add, show, edit, complete or exit: ')
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo= user_action[4:] 
        
        # open the existing file to list all items
        # old way to open file as read lines
        # file = open('todos.txt', 'r')
        # todos = file.readlines()
        # file.close()

        # bettersh way to open file as read lines
        # with open('todos.txt', 'r')  as file:
        #     todos = file.readlines()
        # replace above with functions

        todos = functions.get_todos()

        # Add the new items in the list
        todos.append(todo + "\n")

         # with open('todos.txt', 'w') as file:
            #     file.writelines(todos)
            # replace above function 
        functions.write_todos(todos)

    elif user_action.startswith('show'):

            # open the existing file to list all items

        # with open('todos.txt', 'r')  as file:
        #     todos = file.readlines()

        todos = functions.get_todos()
        
        new_todos = [item.strip('\n') for item in todos]

        for index, item in enumerate(new_todos):
            item = item.title()
            row = f"{index + 1}-{item}"
            print(row)
        print("length is", len(todos))

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number = number -1
            
            # replace above with functions
            todos = functions.get_todos()
                        
            new_todo = input('enter new todo: ').strip()
            todos[number] = new_todo + '\n' 

            # with open('todos.txt', 'w') as file:
            #     file.writelines(todos)
            # replace above function 
            functions.write_todos(todos)

        except ValueError:
            print('Your command is not valid')
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])
            # replace above with functions
            todos = get_todos('todos.txt')
            
            index =  number - 1
            todo_to_be_removed = todos[index].strip('\n') 

            todos.pop(index)

            # with open('todos.txt', 'w') as file:
            #     file.writelines(todos)
            # replace above function 
            functions.write_todos(todos)

            message = f"Todo {todo_to_be_removed} was removed from the list"
            print(message)
        except IndexError:
            print('Your command is not valid')
            continue

    elif user_action.startswith('exit'):
        break
    else:
        print('command is not valid')

       

print('bye!')


# lists are mutable , even methods can mutate the list does not need to assign it again to new variable
