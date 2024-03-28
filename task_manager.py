#Task 17- Capstone Project
# Notes:
# 1. Use the following username and password to access the admin rights
# username: admin
# password: password
# 2. Ensure you open the whole folder for this task in VS Code otherwise the
# program will look in your root directory for the text files.

#=====importing libraries===========
import os
from datetime import datetime, date

DATETIME_STRING_FORMAT = "%Y-%m-%d"

# Create tasks.txt if it doesn't exist
if not os.path.exists("tasks.txt"):
    with open("tasks.txt", "w") as default_file:
        pass

with open("tasks.txt", 'r') as task_file:
    task_data = task_file.read().split("\n")
    task_data = [t for t in task_data if t != ""]

# task list created below
task_list = []
for t_str in task_data:
    curr_t = {}

    # Split by semicolon and manually add each component
    task_components = t_str.split(";")
    curr_t['username'] = task_components[0]
    curr_t['title'] = task_components[1]
    curr_t['description'] = task_components[2]
    curr_t['due_date'] = datetime.strptime(task_components[3], DATETIME_STRING_FORMAT)
    curr_t['assigned_date'] = datetime.strptime(task_components[4], DATETIME_STRING_FORMAT)
    curr_t['completed'] = True if task_components[5] == "Yes" else False

    task_list.append(curr_t)


#====Login Section====
'''This code reads usernames and password from the user.txt file to 
    allow a user to login.
'''
# If no user.txt file, write one with a default account
if not os.path.exists("user.txt"):
    with open("user.txt", "w") as default_file:
        default_file.write("admin;password")

# Read in user_data
with open("user.txt", 'r') as user_file:
    user_data = user_file.read().split("\n")

# Convert to a dictionary
username_password = {}
for user in user_data:
    username, password = user.split(';')
    username_password[username] = password

logged_in = False
while not logged_in:
    print("LOGIN")
    curr_user = input("Username: ")
    curr_pass = input("Password: ")
    if curr_user not in username_password.keys():
        print("User does not exist")
        continue
    elif username_password[curr_user] != curr_pass:
        print("Wrong password")
        continue
    else:
        print("Login Successful!")
        logged_in = True

# Registering a user function
def reg_user():
    '''Add a new user to the user.txt file'''
    # - Request input of a new username
    new_username = input("New Username: ")

    # - Check if the new username already exists.
    if new_username in username_password:
        print("Sorry the username you entered already exists, please enter a different username.")
        return

    # - Request input of a new password
    new_password = input("New Password: ")
    # - Request input of password confirmation.
    confirm_password = input("Confirm Password: ")

    # - Check if the new password and confirmed password are the same.
    if new_password == confirm_password:
        # - If they are the same, add them to the user.txt file.
        print("New user added")
        username_password[new_username] = new_password

        with open("user.txt", "a") as out_file:
            out_file.write(f"\n{new_username};{new_password}")

    else:
        print("Passwords do not match")

# Adding a new task function
def add_task():
    task_username = input("Name of person assigned to task: ")
    if task_username not in username_password.keys():
        print("User does not exist. Please enter a valid username")
        return
    task_title = input("Title of Task: ")
    task_description = input("Description of Task: ")

    while True:
        try:
            task_due_date = input("Due date of task (YYYY-MM-DD): ")
            due_date_time = datetime.strptime(task_due_date, DATETIME_STRING_FORMAT)
            break

        except ValueError:
            print("Invalid datetime format. Please use the format specified")

    curr_date = date.today()
    new_task = {
        "username": task_username,
        "title": task_title,
        "description": task_description,
        "due_date": due_date_time,
        "assigned_date": curr_date,
        "completed": False
    }

    task_list.append(new_task)
    with open("tasks.txt", "w") as task_file:
        task_list_to_write = []
        for t in task_list:
            str_attrs = [
                t['username'],
                t['title'],
                t['description'],
                t['due_date'].strftime(DATETIME_STRING_FORMAT),
                t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                "Yes" if t['completed'] else "No"
            ]
            task_list_to_write.append(";".join(str_attrs))
        task_file.write("\n".join(task_list_to_write))
    print("Task successfully added.")

# View all the tasks function
def view_all():
    for t in task_list:
        disp_str = f"Task: \t\t {t['title']}\n"
        disp_str += f"Assigned to: \t {t['username']}\n"
        disp_str += f"Date Assigned: \t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
        disp_str += f"Due Date: \t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
        disp_str += f"Task Description: \n {t['description']}\n"
        print(disp_str)

# View assigned tasks for user function
def view_mine(curr_user):
    task_number = 1

    for i, t in enumerate(task_list):
        if t['username'] == curr_user:
            disp_str = f"{task_number}: Task: \t\t {t['title']}\n"
            disp_str += f"Assigned to: \t {t['username']}\n"
            disp_str += f"Date Assigned: \t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            disp_str += f"Due Date: \t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            disp_str += f"Task Description: \n {t['description']}\n"
            disp_str += f"Completed: \t {'Yes' if t['completed'] else 'No'}\n"
            print(disp_str)
            task_number += 1

    while True:
        try:
            user_option = int(input("Please select a specific task you want by inputting its number or input '-1' to return to the main menu: "))

            if user_option == -1:
                print("You are now back at the the main menu.")
                break
            elif 1 <= user_option <= task_number:
                user_decision = input("Would you like to mark the task as complete(input the letter 'm') or edit the task(input the letter 'e'): ").lower()

                if user_decision == 'm':
                    task_list[user_option - 1]['completed'] = True
                    print("The task has been marked as complete.")
                elif user_decision == 'e' and not task_list[user_option - 1]['completed']:
                    new_username = input("Please input the new username, if you wish to make no changes press 'enter': ")
                    new_due_date = input("Please input the new due date in the following format'YYYY-MM-DD', if you wish to make no changes press 'enter': ")

                    if new_username:
                        task_list[user_option - 1]['username'] = new_username

                    if new_due_date:
                        try:
                            task_list[user_option - 1]['due_date'] = datetime.strptime(new_due_date, DATETIME_STRING_FORMAT)
                        except ValueError:
                            print("Sorry the format of the datetime you entered is not valid, therfore it hasn't been altered.")
                            continue

                    print("The task has now been edited.")
                else:
                    print("Sorry the option you inputted is not valid. To mark the task as complete input 'm' or to edit the task input 'e'.")
            else:
                print("Sorry the number of the task you inputted is not valid, please input a valid number.")
        except ValueError:
            print("Input is not valid. Please try again with a task number that is valid.")

    task_update(task_list)
    
# Update tasks within tasks.txt file function
def task_update(task_list):
    with open("tasks.txt", "w") as task_file:
        task_list_to_write = []
        for t in task_list:
            str_attrs = [
                t['username'],
                t['title'],
                t['description'],
                t['due_date'].strftime(DATETIME_STRING_FORMAT),
                t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                "Yes" if t['completed'] else "No"
            ]
            task_list_to_write.append(";".join(str_attrs))
        task_file.write("\n".join(task_list_to_write))

# Generate reports function
def generate_reports():
    total_tasks = len(task_list)
    completed_tasks = sum(1 for t in task_list if t['completed'])
    incomplete_tasks = total_tasks - completed_tasks
    overdue_tasks = sum(1 for t in task_list if not t['completed'] and t['due_date'] < datetime.combine(date.today(), datetime.min.time()))

    with open("task_overview.txt", "w") as task_overview_file:
        task_overview_file.write(f"Total Number of Tasks: {total_tasks}\n")
        task_overview_file.write(f"Total Number of Completed Tasks: {completed_tasks}\n")
        task_overview_file.write(f"Total Number of Incomplete Tasks: {incomplete_tasks}\n")
        task_overview_file.write(f"Overdue Tasks: {overdue_tasks}\n")
        task_overview_file.write(f"Percentage of Incomplete Tasks: {(incomplete_tasks / total_tasks) * 100:.2f}%\n")
        task_overview_file.write(f"Percentage of Overdue Tasks: {(overdue_tasks / total_tasks) * 100:.2f}%\n")

    total_users = len(username_password.keys())

    with open("user_overview.txt", "w") as user_overview_file:
        user_overview_file.write(f"Total Users: {total_users}\n")
        user_overview_file.write(f"Total Tasks: {total_tasks}\n")

        for user, password in username_password.items():
            user_tasks = [t for t in task_list if t['username'] == user]
            total_user_tasks = len(user_tasks)
            completed_user_tasks = sum(1 for t in user_tasks if t['completed'])
            incomplete_user_tasks = total_user_tasks - completed_user_tasks
            overdue_user_tasks = sum(1 for t in user_tasks if not t['completed'] and t['due_date'] < datetime.combine(date.today(), datetime.min.time()))

            user_overview_file.write(f"\nUser: {user}\n")
            user_overview_file.write(f"Total Number of Tasks Assigned: {total_user_tasks}\n")
            user_overview_file.write(f"Percentage of Total Number of Tasks: {(total_user_tasks / total_tasks) * 100:.2f}%\n")
            user_overview_file.write(f"Percentage of Completed Tasks: {(completed_user_tasks / total_user_tasks) * 100:.2f}%\n") if total_user_tasks != 0 else user_overview_file.write(f"Percentage of Completed Tasks: 0.00%\n")
            user_overview_file.write(f"Percentage of Incomplete Tasks: {(incomplete_user_tasks / total_user_tasks) * 100:.2f}%\n") if total_user_tasks != 0 else user_overview_file.write(f"Percentage of Incomplete Tasks: 0.00%\n")
            user_overview_file.write(f"Percentage of Overdue Tasks: {(overdue_user_tasks / total_user_tasks) * 100:.2f}%\n") if total_user_tasks != 0 else user_overview_file.write(f"Percentage of Overdue Tasks: 0.00%\n")


# Display statistics function
def display_statistics():
    # if statement to determine whether the reports have been generated
    if not os.path.exists("task_overview.txt") or not os.path.exists("user_overview.txt"):
        print("Reports are yet to be generated. Initializing report generation...")
        generate_reports()

    with open("task_overview.txt", 'r') as task_overview_file:
        task_overview_data = task_overview_file.read()
        print("Task Overview:\n")
        print(task_overview_data)

    with open("user_overview.txt", 'r') as user_overview_file:
        user_overview_data = user_overview_file.read()
        print("\nUser Overview:\n")
        print(user_overview_data)

# Menu options 
while True:
    # presenting the menu to the user and 
    # making sure that the user input is converted to lower case.
    print()
    menu = input('''Select one of the following Options below:
    r - Registering a user
    a - Adding a task
    va - View all tasks
    vm - View my task
    gr - Generate reports
    ds - Display statistics
    e - Exit
    : ''').lower()

    if menu == 'r':
        reg_user()

    elif menu == 'a':
        add_task()

    elif menu == 'va':
        view_all()

    elif menu == 'vm':
        view_mine(curr_user)

    elif menu == 'gr':
        generate_reports()

    elif menu == 'ds' and curr_user == 'admin':
        display_statistics()

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("Sorry You have inputted an incorrect option, please input a correct option.")
