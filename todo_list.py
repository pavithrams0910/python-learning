tasks = []

print("Enter 3 tasks")

for i in range(3):
    task = input("Enter task: ")
    tasks.append(task)

print("\nYour To-Do List")
print("----------------")

for task in tasks:
    print("-", task)
