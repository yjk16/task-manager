# This program can help small businesses manage tasks assigned to each member of a team.
# Had help from mentor Sashlin Moonsamy with things including understanding what the task was actually asking for.

# Importing relevant libraries.
import datetime

# This is the log in section.
# It will convert all letters into lowercase.
# It will check whether the user enters a valid username and password from those stored in the file user.txt.
username = input("\nPlease enter your username: \n").lower()

password = input("\nPlease enter your password: \n").lower()

registered_usernames = []

registered_passwords = []

login = open("user.txt", "r+")

lines = login.readlines()

for line in lines:
    details = line.strip()
    details = details.split()

    registered_usernames.append(details[0].replace(",", ""))

    registered_passwords.append(details[1])

while username not in registered_usernames or password not in registered_passwords:

    username = input("\nI'm afraid there was an error in your entry.\nPlease try again. \nPlease enter your username:\n")
    password = input("\nPlease enter your password:\n")

login.close()

while True:

    # This is presenting the menu to the user. 
    # It will make sure that the user input is converted to lower case.
    menu = input('''\nPlease select one of the following options below:\n
    r - registering a user
    a - adding a task
    va - view all tasks
    vm - view my task
    s - view statistics
    e - exit

    I choose: ''').lower()

    # If the user chooses option 'r', and that user has the username 'admin', this section will allow the user to add a new username and password to those saved in user.txt.
    # It must first be confirmed that the username they have chosen is not already registered.
    # And that the password they have chosen has been input correctly twice.
    # If the user does not enter the username 'admin' they will not be able to acces this section and there will be a message to display this.
    if menu == 'r':

        if username == 'admin':

            new_username = input("\nPlease enter a username:\n").lower()

            while new_username in registered_usernames:
            
                new_username = input("\nI'm afraid that username is already in use.  Please choose another username:\n").lower()

            new_password = input("\nPlease enter a password:\n").lower()

            password_confirmation = input("\nPlease confirm your password:\n").lower()

            while new_password != password_confirmation:

                new_password = input("\nYour passwords did not match.\nPlease try again.\nEnter a password:\n").lower()

                password_confirmation = input("\nPlease confirm your password:\n").lower()

            register_user = open("user.txt", "a")

            register_user.write(f"\n{new_username}, {new_password}")

            register_user.close()

        else:

            print("\nI'm afraid you don't have authority to access this area.")

    # If the user chooses 'a', they will be able to add tasks.
    # They will be asked to input the relevant data.
    # This data will then be stored in tasks.txt.
    elif menu == 'a':

        adding = open("tasks.txt", "a")

        username_of_task_assignment = input("\nPlease enter the username of the person whom the task is assigned to:\t")

        title_of_task = input("\nWhat is the title of the task?\t")

        description_of_task = input("\nPlease give a description of the task:\t")

        # I used https://phoenixnap.com/kb/get-current-date-time-python to figure out how to find current date and format it in the same way as the previous entries.
        date_today = datetime.datetime.now()

        date_assigned = date_today.strftime("%d %b %Y")

        due_date = input("\nWhat is the due date of the task?\t")

        task_complete = "No\n"

        adding.write(f"{username_of_task_assignment}, {title_of_task}, {description_of_task}, {date_assigned}, {due_date}, {task_complete}")

        adding.close()

    # In this section the user will be able to view all tasks.
    # The information will be imported from tasks.txt and displayed in a user-friendly manner.
    elif menu == 'va':

        view_all = open("tasks.txt", "r+")

        lines = view_all.readlines()

        for line in lines:
            new_line = line.strip()
            new_line = line.split(", ")

            # My friend Nick helped me as I was struggling with the \n element between 'Task complete' and 'Task description'.
            print(f"\n\nTask:\t\t\t{new_line[1]}\nAssigned to:\t\t{new_line[0]}\nDate assigned:\t\t{new_line[3]}\nDue date:\t\t{new_line[4]}\nTask complete?\t\t{new_line[5]}Task description:\t{new_line[2]}")

        view_all.close()

    # In this section the user will be able to view their own tasks.
    # The information will be imported from tasks.txt and displayed in a user-friendly manner.
    # If there are currently no tasks for the user in question, a relevant message will be displayed.
    elif menu == 'vm':

        view_my_task = open("tasks.txt", "r")

        lines = view_my_task.readlines()

        for line in lines:
            details_of_task = line.strip()
            details_of_task = line.split(", ")

            if username == details_of_task[0].lower():
                print(f"\n\nTask:\t\t\t{details_of_task[1]}\nAssigned to:\t\t{details_of_task[0]}\nDate assigned:\t\t{details_of_task[3]}\nDue date:\t\t{details_of_task[4]}\nTask complete?\t\t{details_of_task[5]}Task description:\t{details_of_task[2]}")

        else:
            print("\nYou do not have any tasks recorded here at the moment.")

        view_my_task.close()

    # In this section, if the user is 'admin', they will be able to see the total number of tasks and the total number of users displayed in a user-friendly manner.
    # If they are another user, they will be denied access.
    elif menu == 's':

        if username == 'admin':

            statistics = open("tasks.txt", "r")

            lines = statistics.readlines()

            total_tasks = len(lines)

            print(f"\nTotal tasks:\t\t{total_tasks}")

            statistics.close()

            stats = open("user.txt", "r")

            lines = stats.readlines()

            total_users = len(lines)

            print(f"Total users:\t\t{total_users}")

            stats.close()

        else:
            print("\nI'm afraid you don't have authority to access this area.")

    elif menu == 'e':
        print("\nGoodbye!!!")
        exit()

    else:
        print("Something has gone wrong! Please try again.")