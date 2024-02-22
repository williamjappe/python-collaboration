#Initializing list dictionary
list = {}

#Command to add task to list
def addtask(task):
    list.update({task:0})
    return list

#Command to view list
def viewtasks():
    print(list)