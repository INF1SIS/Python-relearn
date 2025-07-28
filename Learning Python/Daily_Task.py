# Daily Task CLI Tool
# Needed:
# Ask what to do for the day
# Accept input from user
# Output list
# "Add More" option



tasks = []


user_input = input("What would you like to do today? ")
tasks.append(user_input)

while True:
    add_more = input("Add more tasks? (yes/no): ").strip().lower()
    if add_more == 'yes':
        additional_task = input("Please enter additional task: ")
        tasks.append(additional_task)
    elif add_more == 'no':
        break
    else:
        print("Please type 'yes' or 'no'.")
        
        
print("Updated tasks for today:")
for i, task in enumerate(tasks, start = 1):
    print(f"{i}, {task}")
    