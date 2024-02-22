#Initializing list dictionary
list = {}

#Command to add task to list
def addtask(task):
    list.update({task:0})
    return list

#Command to view list
def viewtasks():
    print(list)

#Command to mark tasks
def marktask(task):
    if task in list:
        list.update({task:1})
        return list
    else:
        print("Task does not exist!")
        return False