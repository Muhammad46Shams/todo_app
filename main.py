
todos = []
while True:
    user_action = input('Type add, show, edit or exit: ')
    user_action = user_action.strip()
    
    match user_action:
        case 'add':
            todo= input('Enter todo:')
            todos.append(todo)
        case 'show':
            for index, item in enumerate(todos):
                item = item.title()
                row = f"{index}-{item}"
                print(row)
        case 'edit':
            number = int(input('No of the todo for edit: '))
            number = number -1
            todos[number] = input('enter new todo: ').strip()
        case 'exit':
            break
       

print('bye!')