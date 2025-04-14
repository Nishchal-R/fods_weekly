'''Write a function to accept a list of names and return the sorted order of names back.'''

def sort(names):
    for i in range(len(names)):
        for j in range(i + 1, len(names)):
            if names[i].lower()>names[j].lower(): #comparision sorting and lower() to avoid case sensitivity
                names[i], names[j]=names[j], names[i]
    return names

names=[] #empty list to store names
print("Enter list of names. \nPress enter again to finish.")
while True:
    name=input("Enter a name:")
    if name=="": #Breaks the loop when entered blank
        break
    names.append(name) #Stores inputs in names[]
sorted=sort(names)
print(sorted)