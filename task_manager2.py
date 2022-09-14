import math
from datetime import date, datetime

#===============================================FUNCTIONS===============================================#

# Define each definition at the beginning of the program

#===============================================f(x)REGISTER USER=======================================#

def reg_user():

# Open the users2.txt file in 'r+' mode, where wen open a file for both reading and writing. The file pointer will be at the beginning of the file
# Use the readlines() function to read through each line of users2.txt
# Set an empty list with variable name 'username_list'

    user_list = open("users2.txt", "r+")
    user_list_content = user_list.readlines()
    username_list = []

# For each line in the file, split the data into a list with a ','
# Set a new variable 'users' at the index[0] of the split_data list
# Add all usernames to 'username_list' that have been formatted to a list using the append() function

    for line in user_list_content:
            split_data = line.split(", ")
            users = split_data[0]
            username_list.append(users)

# Create a new variable called 'new_user_name' that requires user input
# Convert all letters to lower for uniformity 

    while  True:
        new_user_name = input("\n\nPlease enter the new username that you wish to add:\n\n").lower()

# Set a condition that if the user is already found in 'username_list' the user will be promted to enter a new one

        if new_user_name in username_list:
            print("\nThis username already exists. Please enter a new one.\n\n")

# If the passwords do not match, request confirmation again

        else:
            new_user_password = input("\n\nPlease enter their password:\n\n")
            confirm_password = input("\n\nPlease confirm password:\n\n")

            if new_user_password != confirm_password:
                print("\n\nThe passwords do not match. Please try again.\n\n")

# If the passwords match, add the new user information to the users2.txt file
# Use the format{} function to write the user information with the same format as previous users

            elif new_user_password == confirm_password:

                print("\n\nThank you!\n\n")
                print(new_user_name + " has been added to your database.\n\n")
                new_user = f"{new_user_name}, {new_user_password}\n"
                user_list.write(new_user)
                break

# Prompt user to go back to main menu

    input("Please press -1 to go back to the main menu\n")
    
# Close the file

    user_list.close()

#===============================================f(x)ADD TASK============================================#

def add_task():

# Open the tasks2.txt file in 'a' mode where the handle is positioned at the end of the file. The data being written will be inserted at the end, after the existing data.
# Set new input variables for each task element
# Use the date() function to pull today's date
# For the due date set it in the same format as the current date

    new_task = open("tasks2.txt", "a")
    assign_task = input("\n\nPlease assign a username to the task:\n\n")
    title_task = input("\n\nPlease confirm the title of the task:\n\n")
    description = input("\n\nPlease write a description of the task:\n\n")
    current_date = date.today()
    due_date = input("\n\nPlease enter the due date for this task (format YYYY-MM-DD):\n\n")
    task_completion = input("\n\nPlease confirm if the task is completed or not (Yes or No):\n\n")

# Write the new task onto the tasks.txt file using the format{} function 

    new_task.write(f"{assign_task}, {title_task}, {description}, {current_date}, {due_date}, {task_completion}\n")

    print("\n\nThank you, your task has been added to 'tasks2.txt'\n")

# Prompt user to go back to main menu

    input("Please press -1 to go back to the main menu\n")

# Close the file

    new_task.close()

#===============================================f(x)VIEW ALL============================================#

def view_all():

# Set empty list variables for each task element so that we can index them
# # Open the tasks2.txt file as read only, where the handle is positioned at the beginning of the file. This is also the default mode in which a file is opened

    view_tasks = open("tasks2.txt", "r")
    assign_task = []
    title_task = []
    description = []
    current_date = []
    due_date = []
    task_completion = []

# Use a for loop to run through each element of the file
# For each line in the task2s.txt file use the split()function to split strings into a list 
# Set the positions for each task element 

    for lines in view_tasks:
        lines = lines.split(", ")
        assign_task = lines[0]
        title_task = lines[1]
        description = lines[2]
        current_date = lines[3]
        due_date = lines[4]
        task_completion = lines[5]

# Print out the tasks in the requested format, using indexing
# Convert each element to a string so that the print function works

        print("\n------------------------------------------------------------------------------\n")

        print("Task:\t\t\t\t" + str(title_task))

        print("Assigned to:\t\t\t" + str(assign_task))

        print("Date assigned:\t\t\t" + str(current_date))

        print("Due Date:\t\t\t" + str(due_date))

        print("Task complete?\t\t\t" + str(task_completion))

        print("Task Description:\n" + str(description))

        print("\n------------------------------------------------------------------------------\n")

# Prompt user to go back to main menu

    input("Please press -1 to go back to the main menu\n\n")
                
# Close file

    view_tasks.close()  

#===============================================f(x)VIEW MINE===========================================#

def view_mine():

# Open the tasks2.txt file in 'r+' mode, where wen open a file for both reading and writing. The file pointer will be at the beginning of the file

    view_user_task = open("tasks2.txt", "r+")

# Get username from user
# Set both found and count functions at 0 

    input_username = input("\n\nPlease enter your username:\n\n")
    found = False
    count =  0

# Using a loop to read through each line in the file
# For each line in the tasks2.txt file, use the split()function to split strings into a list 
# Set users element as position [0]
# Set the counting increments to go up by 1

    while True:

        for lines in view_user_task:
            count += 1 
            split_data = lines.split(", ")
            users = split_data[0] 

# If the input username has been found in the tasks2.txt file, print the respective task using formatting for readability
# Using the count function, format each task to be numbered as they are printed 
# Set found to True so that the loop stops running

            if users == input_username:
                print("\n------------------------------------------------------------------------------\n")

                print(f"{count}. Task:\t\t\t" + split_data[1])

                print("Assigned to:\t\t\t" + split_data[0])

                print("Date assigned:\t\t\t" + split_data[3])

                print("Due Date:\t\t\t" + split_data[4])

                print("Task complete?\t\t\t" + split_data[5])

                print("Task Description:\n" + split_data[2] + "\n")

                print("\n------------------------------------------------------------------------------\n")    
                
                found = True

# If the username has not been found, prompt user for another try or to go back to the main menu

            elif not found:
                print("\nYou have entered an incorrect username.\n")
                input_username = input("\nPlease enter your username again or press -1 to go home:\n\n")

# Set a condition that if the username has been found, the user will be able to edit their own tasks
# Prompt user to enter the task number they want to edit, converting the input to an integer 
# Because of the terminal indexing, subtract 1 from the user selection to ensure being in range
# Set an empty 'tasks' list 
# Set the handle to start at 0 or at the beggining of the file using the seek() function, for appending purposes

        if found:
            user_input = int(input("Please select a task number to edit\n\n"))
            selection = (user_input - 1)
            tasks = []
            view_user_task.seek(0)

# Add each line from the file to the 'tasks' list using append() function

            for lines in view_user_task:
                tasks.append(lines)

# Set data variable at the same index of the selection number to ensure the right task number is being edited
# Remove newline characters using strip() function
# Split the strings in 'tasks' with a ',' using split() function

            data = tasks[selection].strip("\n")
            split_data = data.split(", ")

# Set a condition that if the task completion is 'No', then the task can be edited
# Prompt user to edit a specific selection using input

            if split_data[5] == 'No':
                print("\n1. Change assigned user\n\n")
                print("2. Change due date\n\n")
                print("3. Mark task as complete\n\n")
                choice = input()

# If user selects 1. (Change assigned user), get input to change assigned user
# Set 'new_username' to be at the same index as old username
# Add the new username to the tasks list using join() function

                if choice == '1':
                    new_username = input("\nPlease enter the new username you would like to assign to the task\n\n").lower()
                    split_data[0] = new_username
                    tasks[selection] = ", ".join(split_data)

# If user selects 2. (New date), get input for new date
# Set 'new_duedate' at same index as old due date
# Add new due date using join() function

                if choice == '2':
                    new_duedate = input("\nPlease enter the new due date of the assignment\n\n")
                    split_data[4] = new_duedate
                    tasks[selection] = ", ".join(split_data)

# If user selects 3. (Completion), get input for new data
# Set 'task_complete' at same index as old completion status
# Change to 'Yes' using join() function

                if choice == '3':
                    task_complete = "Yes"
                    split_data[5] = task_complete
                    tasks[selection] =  ", ".join(split_data)

# Set an empty string called 'new_task'
# Add each line from the task to the 'tasks' list, separated with a newline character

                new_task = ""
                for lines in tasks:
                    new_task += lines + "\n"

# Set the handle to start at 0 for writing new data 
# Write new data onto tasks2.txt file 

                view_user_task.seek(0)
                view_user_task.write(new_task)

                print("\nThank you", input_username, "Your task has been updated!\n\n")

# Prompt user to go back to main menu

                input("\nPlease press -1 to go back to the main menu\n\n")

                break

        else:
            input("\nPlease press -1 to go back to the main menu\n\n")

# Close file

    view_user_task.close()
#===============================================f(x)TASK OVERVIEW=======================================#
def task_overview_1():

# Open the users2.txt and tasks2.txt file as read only, where the handle is positioned at the beginning of the file. This is also the default mode in which a file is opened
# Open new files user_overview.txt and task_verview.txt for writing only. This overwrites the file if the file exists. If the file does not exist, creates a new file for writing.

    usernames = open("users2.txt", "r")
    tasks = open("tasks2.txt", "r")
    user_overview = open("user_overview.txt", "w", encoding = "utf-8")
    task_overview = open("task_overview.txt", "w", encoding = "utf-8")

# Set new variables that have read through users2.txt and tasks2.txt

    tasks_list = tasks.readlines()
    usernames_list = usernames.readlines()

# Start all requested variables at count 0 

    total_tasks = 0
    completed_tasks = 0
    uncompleted_tasks = 0
    overdue_tasks = 0

# For each line in the tasks2.txt file, count in increments of 1
# Set completion index at [-1] to ascertain whether task is completed or not

    for line in tasks_list:
        total_tasks += 1
        line = line.strip("\n").split(", ")
        completion = line[-1]

# If 'No', count in increments of 1
# Using the datetime and date() function, calculate whether tasks are overdue or not 

        if completion == 'No':
            uncompleted_tasks += 1
            datetime_object = datetime.strptime(line[4], '%d %b %Y').date()

# If overdue, count in increments of 1

            if datetime_object < date.today():
                overdue_tasks += 1

# If complete, count in increments of 1

        else:
            completed_tasks += 1

# Set further variables for the %'s requested, using previous calculations

        percentage_incomplete = (uncompleted_tasks/total_tasks) * 100
        percentage_overdue = (overdue_tasks/total_tasks) * 100

# Print using format{}function

    print("\n\n------------------------------------TASKS OVERVIEW------------------------------------\n")
    print(f"\nthe number of total tasks is {total_tasks}\n")
    print(f"\nthe number of completed tasks is {completed_tasks}\n")
    print(f"\nthe number of incomplete tasks is {uncompleted_tasks}\n")
    print(f"\nThe number of overdue tasks is {overdue_tasks}\n")
    print(f"\nThe percentage of imcomplete tasks is {percentage_incomplete}%\n")
    print(f"\nThe percentage of overdue  tasks is {percentage_overdue}%\n")
    print("\n\n------------------------------------END OF TASKS OVERVIEW------------------------------------\n")

# Write onto the task_overview.txt file using format{} function

    task_overview.write("------------------------------------TASKS OVERVIEW------------------------------------\n")
    task_overview.write(f"\nThe number of total tasks is {total_tasks}\n")
    task_overview.write(f"\nThe number of completed tasks is {completed_tasks}\n")
    task_overview.write(f"\nThe number of incomplete tasks is {uncompleted_tasks}\n")
    task_overview.write(f"\nThe number of overdue tasks is {overdue_tasks}\n")
    task_overview.write(f"\nThe percentage of imcomplete tasks is {percentage_incomplete}%\n")
    task_overview.write(f"\nThe percentage of overdue tasks is {percentage_overdue}%\n")
    task_overview.write("\n\n------------------------------------END OF TASKS OVERVIEW------------------------------------\n")

# Prompt user to go back to main menu

    input("\nPlease press -1 to go back to the main menu\n\n")

# Close file 

    task_overview.close()
#===============================================f(x)USER OVERVIEW=======================================#
def user_overview_1():

# Open the users2.txt and tasks2.txt file as read only, where the handle is positioned at the beginning of the file. This is also the default mode in which a file is opened
# Open new file task_verview.txt for writing only. This overwrites the file if the file exists. If the file does not exist, creates a new file for writing.

    usernames = open("users2.txt", "r")
    tasks = open("tasks2.txt", "r")
    user_overview = open("user_overview.txt", "w", encoding = "utf-8")

# Set new variables that have read through users2.txt and tasks2.txt
# Count total tasks using len() function

    tasks_list = tasks.readlines()
    total_tasks = len(tasks_list)
    usernames_list = usernames.readlines()

# Set 'total_users' at count 0

    total_users = 0

# Set output variable to display total users and tasks using len() and format{}  functionss

    output = f"the number of users is {len(usernames_list)}\n"\
            f"the number of tasks is {len(tasks_list)}\n"

# For each line in 'usernames_list'
# Count total_users in increments of 1
# Set requested variables at count 0

    for line in usernames_list:
        total_users += 1
        line = line.strip("\n").split(", ")
        users = line[0]
        total_task_per_user = 0
        user_incomplete_tasks = 0
        user_completed_tasks = 0
        user_overdue_tasks = 0

# For each line in 'tasks_list', find each user's respective tasks using indexing

        for line in tasks_list:
            line = line.strip("\n").split(", ")
            task_username = line[0]

# If user is found in tasks, count in increments of 1

            if users  == task_username:
                total_task_per_user += 1

# If task  incomplete, count in increments of 1

                if line[-1] == "No":
                    user_incomplete_tasks += 1
                    datetime_object = datetime.strptime(line[4], '%d %b %Y').date()

# Using the datetime and date() function, calculate whether tasks are overdue or not 

                    if datetime_object < date.today():
                        user_overdue_tasks += 1

# If complete, count in increments of 1

                else:
                    user_completed_tasks += 1

# If user has no tasks, set each variable to 0

        if total_task_per_user == 0:
            user_task_percentage = 0
            user_percentage_complete = 0
            user_percentage_incomplete = 0
            user_percentage_overdue =  0

# If they do have tasks, do necessary calculations

        else:
            user_task_percentage = (total_task_per_user/total_tasks) * 100
            user_percentage_complete = (user_completed_tasks/total_task_per_user) * 100
            user_percentage_incomplete = (user_incomplete_tasks/total_task_per_user) * 100
            user_percentage_overdue = (user_overdue_tasks)/total_task_per_user * 100

# Using output variable and formatting, print each string in a user friendly manner
# Write each string to the user_overview.txt file 

        output += f"\n------------------------------------USER OVERVIEW------------------------------------\n"
        output += f"\n{users}:\n"
        output += f"\nThe number of overdue tasks is {user_overdue_tasks}\n"
        output += f"The percentage of user tasks is {user_task_percentage}%\n"
        output += f"The percentage of complete tasks is {user_percentage_complete}%\n"
        output +=  f"The percentage of incomplete tasks is {user_percentage_incomplete}%\n"
        output += f"The percentage of overdue tasks is {user_percentage_overdue}%\n"

    print(output)
    print("------------------------------------END OF USER OVERVIEW------------------------------------")
    user_overview.write(output)

# Prompt user to go back to main menu

    input("\nPlease press -1 to go back to the main menu\n\n")

# Close file

    user_overview.close()

#===============================================LOGIN===================================================#

print("\n------------------------------------------------------------------------------\n")

# Open users2.txt file as a read-only file, where the handle is positioned at the beginning of the file. This is also the default mode in which a file is opened.

user_list = open("users2.txt", "r+")

# Use the readlines() function to read through each line in the file
# This returns each line as a list item

find_user = user_list.readlines()

# Set empty lists for users and passwords so that we can index each element
# This allows for the computer to search through each user and password
# Set an empty variable that stores which user has logged in

users = []
passwords = []
user_name  = ""

# Use a for for loop to run through each element of the file 
# For each line in the users.txt file use the split()function to split strings into a list 
# Set the position for users in the list as[0]
# Set the positin for the passwords in the list as [1]
# Use the append() function to add each username and password to the users and passwords list

for line in find_user:
    line = line.split(", ")
    username = line[0]
    password = line[1].replace("\n", "")
    users.append(username)
    passwords.append(password)

# Use a loop to run through the input of each user
# Set a variable for the input username and user password
# Use an if statement to determine if the username is in the users2.txt file
# If the input username is in the users.txt file, then we set the index for the password to be the same as the username

while True:

    user_name = input("\nPlease enter your username:\n\n")

    if user_name in users:
        password_index = users.index(user_name)

# If username and password match to one of the lines in the users.txt file, allow them in and break the loop
        user_password = input("\n\nPlease enter your password:\n\n")
        
        if  user_password == passwords[password_index]:
            print("\n\nWelcome to Task Manager, " + user_name)
            break

# If the password is entered incorrectly, request password again and let them in if it's correct

        else:
            print("\nYou have entered an incorrect password.")
            user_password = input("\n\nPlease enter your password again:\n\n")

            if  user_password == passwords[password_index]:
                print("\n\nWelcome to Task Manager, " + user_name)
                break
            
# If the username is incorrect, request username again

    else:
        print("\nYou have entered an incorrect username.")
    
# Close the users2.txt file using the close() function

user_list.close()

#===============================================MENU=================================================#

#Use a loop to present the menu to the user
#Use the lower()function to convert inputs to lowercase

print("\n------------------------------------------------------------------------------\n")

while True:
    
    menu = input('''\n\nSelect one of the following options below:\n
                    r - Registering a user
                    a - Adding a task
                    va - View all tasks
                    vm - View my task
                    gr - Generate reports
                    s - View statistics
                    e - Exit
                    \n\n
------------------------------------------------------------------------------\n''').lower()


#===============================================REGISTER USER=========================================#

# Use an if statement if the user selects 'r'
# Set a condition that the username has to be admin in order to register a new user
# If username isn't admin, prompt to choose another option from the menu 
# Call reg_user() function

    if menu == 'r':
        
        if user_name != 'admin':
            print("\nSorry, you do not have access to register new users!\n")
            input("Please press -1 to go back to the main menu")

        else:
            reg_user() 

#===============================================ADD TASK==============================================#

# If user selects 'a' to add a task
# Call add_task() function

    if menu == 'a':
        add_task()

#===============================================VIEW ALL TASK(S)======================================#

# If the user selects the 'va' option to view all tasks
# Call view_all() function

    elif menu == 'va':
        view_all()

#===============================================VIEW MY TASK(S)=======================================#

# If the user selects 'vm' to view my task(s)
# Call view_mine() function

    elif menu == 'vm':
        view_mine()

#===============================================GENERATE REPORTS=======================================#

# If the user selects 'gr' to generate reports
# Call task_overview_1() and user_overview_1() functions

    elif menu == 'gr':
        task_overview_1()
        user_overview_1()
        
#===============================================STATISTICS=============================================#

# If user selects 's' and username is 'admin' to view stats
# Call task_overview_1() and user_overview_1() functions

    elif menu == 's' and user_name == "admin":

        print("\nWelcome, Admin!\n")

        task_overview_1()
        user_overview_1()


#===============================================EXIT===================================================#

#If  user selects 'e' to exit 
#Say goodbye

    elif menu == 'e':
        
        print('Goodbye!!!')
        exit()


