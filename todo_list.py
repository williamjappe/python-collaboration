#Initializing list dictionary
list = {}

#Command to add task to list
def addtask(task):
    list.update({task:0})
    return True

#Command to view list
def viewtasks():
    print(list)
    return True

#Command to mark tasks
def marktask(task):
    if task in list:
        list.update({task:1})
        return True
    else:
        print("Task does not exist!")
        return False

#Command to delete tasks
def deletetask(task):
    if task in list:
        list.pop(task)
        return True
    else:
        print("Task does not exist!")
        return False

#Command to sort tasks
def sorttasks():
    not_completed = []
    completed = []
    for x in list:
        if list.get(x) == 0:
            not_completed.append(x)
        else:
            completed.append(x)
    print("Not Completed:", not_completed)
    print("Completed:", completed)
    return True