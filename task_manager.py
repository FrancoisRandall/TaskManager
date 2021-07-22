import datetime as dtime
login = False

# Declaring menus for initial login

admin_menu = '''

Please select one of the following options:

r - register user
a - add task
va - view all tasks
vm - view my tasks
gr - generate reports
s - statistics
e - exit

Selection: '''

normal_menu = '''

Please select one of the following options:

a - add task
va - view all tasks
vm - view my tasks
e - exit

Selection: '''  

# Start login process
            
while login == False:

# Request user input and add values to variables

    username = input("Enter your username: ")
    password = input("Enter your password: ")
    user_input = f"{username}, {password}"
    option_selection = ""

    with open ("user.txt", "r") as valid:

# Use the .read() function to read throught lines of info in the user.txt doc to compare later
# If user_input is admin's details, the admin menu will be visible

        valid = valid.read()
        if user_input == "admin, adm1n":
            login = True
            print("\nLogin successful!")
            option_selection = input(admin_menu)

# If the value of user_input in is in the value of valid, the code will run

        elif user_input in valid:
            login = True
            print("\nLogin successful!")
            option_selection = input(normal_menu)           
            
        else:
            print("\nThe login details entered are not valid. Please try again.\n")

# Admin menu function
# Option selection is included so that the menu option can be used as a whole after the initial login

def admin_menu():
    option_selection = input('''

Please select one of the following options:

r - register user
a - add task
va - view all tasks
vm - view my tasks
gr - generate reports
s - statistics
e - exit

Selection: ''')


# Register user
# If 'r' is selected, the 'reg_user()' function is called
# 'r' Can only be selected if the admin user has logged in
    
    if (option_selection == "r") and (username == "admin"):
        reg_user()

# Add task
# Used 'https://realpython.com/python-datetime/#creating-python-datetime-instances' to learn and use the 'import datetime' function
# If 'a' is selected, 'add_task()' function is called

    if option_selection == "a":
        add_task()

# View all tasks
# If 'va' is selected, 'view_all()' function is called

    if option_selection == "va":
        view_all()

# View my tasks
# If 'vm' is selected, 'view_mine()' function is called

    if option_selection == "vm":
        view_mine()

# Generate report
# task_overview

    if option_selection == "gr":
        from datetime import datetime
        with open("tasks.txt", "r") as generate_report:
            generate_report = generate_report.readlines()
            task_total = 0
            completed_tasks = 0
            incompleted_tasks = 0
            due_dates = 0
            overdue_tasks = 0
            incomplete_perc = 0
            overdue_perc = 0
            
            with open("task_overview.txt", "w") as task_ovw:
                for gr in generate_report:
                    gr = gr.strip("\n").split(", ")
                    due_dates = datetime.strptime(gr[4], "%d %b %Y")
                    task_total += 1
                    
                    if gr[5] == "Yes":
                        completed_tasks += 1
                    else: incompleted_tasks += 1

                    if (datetime.today() > due_dates) and (gr[5] == "No"):
                        overdue_tasks += 1
                    
                incomplete_perc = round((incompleted_tasks / task_total) * 100, 2)
                overdue_perc = round((overdue_tasks / task_total) * 100, 2)

# Write to txt file

                task_ovw.write(f'''Task Overview:

Task total:\t\t\t\t {task_total}
Completed Tasks:\t\t\t {completed_tasks}
Incompleted Tasks:\t\t\t {incompleted_tasks}
Overdue Tasks:\t\t\t\t {overdue_tasks}
Incomplete Task Percentage:\t\t {incomplete_perc}%
Overdue Task Percentage:\t\t {overdue_perc}%''')

# Print to user

                print(f'''
Your Task Overview has successfully been updated as follows:

Task Overview:

Task total:\t\t\t\t {task_total}
Completed Tasks:\t\t\t {completed_tasks}
Incompleted Tasks:\t\t\t {incompleted_tasks}
Overdue Tasks:\t\t\t\t {overdue_tasks}
Incomplete Task Percentage:\t\t {incomplete_perc}%
Overdue Task Percentage:\t\t {overdue_perc}%''')
                
# user_overview
# Received assistance from 'pyTony' on discord to understand the approach to take with the regards to the loops

        with open("user_overview.txt", "w") as user_overview:
            with open("user.txt", "r+") as user_report:
                user_report = user_report.readlines()
                with open("tasks.txt", "r+") as task_report:
                    task_report = task_report.readlines()

                    for ur in user_report:
                        ur = ur.split(", ")[0]
                        user_count = 0
                        task_count = 0
                        user_task_total = 0
                        user_task_perc = 0
                        task_comp = 0
                        task_incomp = 0
                        user_perc_complete = 0
                        user_perc_incomplete = 0
                        inc_overdue = 0
                        perc_inc_overdue = 0

                        user_count += 1

                        for tr in task_report:
                            tr = tr.strip("\n")
                            task_count += 1
                            if tr.startswith(ur):
                                if tr.endswith("Yes"):
                                    task_comp += 1
                                if tr.endswith("No"):
                                    task_incomp += 1
                                if (tr.endswith("No")) and (datetime.today() > due_dates):
                                    inc_overdue += 1
                                user_task_total += 1

# The below is done to negate the division by 0 (example: 0 / x)
                        
                        if user_task_total != 0:
                            user_task_perc = round((user_task_total / task_count) * 100, 2)
                        else:
                            user_task_perc = 0

                        if task_comp != 0:
                            user_perc_complete = round((task_comp / user_task_total) * 100, 2)
                        else:
                            user_perc_complete = 0

                        if task_incomp != 0:
                            user_perc_incomplete = round((task_incomp / user_task_total) * 100, 2)
                        else:
                            user_perc_incomplete = 0

                        if inc_overdue != 0:
                            perc_inc_overdue = (inc_overdue / user_task_total) * 100
                        else:
                            perc_inc_overdue = 0
                                
# Write to txt file

                        user_overview.write(f'''
{ur} Report:

Total Tasks:\t\t\t\t {user_task_total}
Percentage Tasks assigned:\t\t {user_task_perc}%
Percentage completed:\t\t\t {user_perc_complete}%
Percentage incomplete:\t\t\t {user_perc_incomplete}%
Percentage incomplete and overdue:\t {perc_inc_overdue}%
''')

# Print to user
                        
                        print(f'''
{ur} Report:

Total Tasks:\t\t\t\t {user_task_total}
Percentage Tasks assigned:\t\t {user_task_perc}%
Percentage completed:\t\t\t {user_perc_complete}%
Percentage incomplete:\t\t\t {user_perc_incomplete}%
Percentage incomplete and overdue:\t {perc_inc_overdue}%
''')

# Statistics
# 'insert_report' function added in order to generate report before statistic is displayed
# This refreshes the reports from where th 'statistics' code gets its information from

    if option_selection == "s":
        insert_report()
        
# User Stats
    
        user_stat_list = []
        user_stat_total = 0
        with open("user_overview.txt", "r") as user_stats:
            user_stats = user_stats.readlines()
            for us in user_stats:
                us = us.strip().split("\t ")
                user_stat_list.append(us)

            for ust in user_stat_list:
                if "Total Tasks:\t\t\t" in ust:
                    user_stat_total += 1
            print(f"Users:\t\t\t {user_stat_total}")

# Task stats

        task_stat_list = []
        task_stat_total = 0
        with open("task_overview.txt", "r") as task_stats:
            task_stats = task_stats.readlines()
            for ts in task_stats:
                ts = ts.strip().split("\t ")
                task_stat_list.append(ts)

            for tst in task_stat_list:
                if "Task total:\t\t\t" in tst:
                    task_stat_total = tst[1]
        print(f"Tasks:\t\t\t {task_stat_total}")

# Exit

        if option_selection == "e":
            print("\nYou have successfull logged out.")

# Normal menu function
# Nomrmal menu function is created with less menu options than admin_menu
    
def normal_menu():
    option_selection = input('''

Please select one of the following options:

a - add task
va - view all tasks
vm - view my tasks
e - exit

Selection: ''')

    if option_selection == "a":
        add_task()

    if option_selection == "va":
        view_all()

    if option_selection == "vm":
        view_mine()

    if option_selection == "e":
        print("\nYou have successfull logged out.")

# Register user function
# Only if the new_password has the same value of confirm_password, then the code will append the information to user.txt

def reg_user():
    new_username = ""
    new_password = ""
    confirm_password = ""
    users = []
    user_check = False
    
    with open("user.txt", "r+") as user_doc:
        new_username = input("\nEnter your new username: ")
        new_password = input("Enter your new password here: ")
        confirm_password = input("Confirm your new password: ")
                
        for q in user_doc:
            if new_username in q:
                user_check = True

    with open("user.txt", "a") as user_docs:
        if user_check == True:
            print("\nThis username is already taken")
            reg_user()

        elif new_password == confirm_password:
            user_docs.write(f"\n{new_username}, {new_password}")
            print("\nNew user successfully added!")
                    
        else:
            print("\nYou did not confirm the correct password. Please try again.")
            reg_user()

# Add tasks function
# Open tasks.txt to append items
# Append relevant info to tasks.txt file
# Used 'https://www.w3schools.com/python/python_datetime.asp' to get the 'command' for month name

def add_task():
    with open("tasks.txt", "a") as task_doc:
        task_username = input("\nEnter the username of the person you would like to assign the task to: ")
        task = input("Enter your task title here: ")
        task_description = input("Enter a description of your task here: ")
        assigned_date = dtime.date.today().strftime("%d-%b-%Y").replace("-", " ")
        due_date = input("Enter your task due date here (ex. 5 Nov 2021): ")
        task_complete = "No"
        print(f"\nYour task has successfully been assigned to {task_username}!")

        task_doc.write(f"\n{task_username}, {task}, {task_description}, {assigned_date}, {due_date}, {task_complete}")

# View all tasks function
# Index the relevant sections to the relevant headings

def view_all():
    with open("tasks.txt", "r+") as all_tasks:
        for i in all_tasks:
            i = i.split(", ")
            print(f'''
User:\t\t\t {i[0]}
Task:\t\t\t {i[1]}
Description:\t\t {i[2]}
Assigned date:\t\t {i[3]}
Due date:\t\t {i[4]}
Task complete:\t\t {i[5]}
''')

# View my tasks function
# If username(which the user declared in the beginning of the program) has the same value of the '0' index
# associated with the tasks.txt info, then print out the rest of the information in that list

def view_mine():
    with open("tasks.txt", "r") as my_tasks:
        my_tasks = my_tasks.readlines()
        print(f"\nThe below tasks are all assigned to {username}:")

        for x, line in enumerate(my_tasks, 1):
            line = line.split(", ")
            if username == line[0]:
                print(f'''
Task number:\t\t {x}
Username:\t\t {line[0]}
Task:\t\t\t {line[1]}
Description:\t\t {line[2]}
Assigned date:\t\t {line[3]}
Due date:\t\t {line[4]}
Task complete:\t\t {line[5]}
''')

# If '-1' is selected, the respective menu will appear, depending on the user details initially entered

    with open("tasks.txt", "r+") as my_tasks:
        my_tasks = my_tasks.readlines()
        vm_select = int(input("Type the task number if you wish to view a specific task or type '-1' to proceed to the main menu: "))

        if (vm_select == -1) and (user_input == "admin, adm1n"):
            admin_menu()
        if (vm_select == -1) and (user_input in valid):
            normal_menu()

        for z, lines in enumerate(my_tasks, 1):
            lines = lines.split(", ")
            if (vm_select == z) and (username == lines[0]):
                print(f'''
Task number:\t\t {z}
Username:\t\t {lines[0]}
Task:\t\t\t {lines[1]}
Description:\t\t {lines[2]}
Assigned date:\t\t {lines[3]}
Due date:\t\t {lines[4]}
Task complete:\t\t {lines[5]}''')

                task_option = int(input('''

Task Options (select number):
1. Mark task as complete
2. Edit task

Selection: '''))

# Mark Task as complete
# 'z' will be the task number selected

                if task_option == 1:
                    sentences = ""
                    with open("tasks.txt", "r+") as complete:
                        for m, t in enumerate(complete, 1):
                            t = t.split(", ")
                            if m == z:
                                t[5] = "Yes" + "\n"
                            sentences += ", ".join(t)
                        print(sentences)
                        with open("tasks.txt", "w") as complete:
                            complete.write(f"{sentences}")
                    

# Edit task

                elif task_option == 2:
                    edit_task = int(input('''
Edit Options (choose number):

1. Username
2. Due Date

Selection: '''))

# Username edit
# If the 'new' task number matches the specific task number selected by the user
# 'e' will replace the 0 index of that specific task

                    if edit_task == 1:
                        edit_user = ""
                        with open("tasks.txt", "r+") as user_edit:
                            for u, e in enumerate(user_edit, 1):
                                e = e.split(", ")
                                if u == z:
                                    e[0] = input("\nEnter new username here: ") 
                                edit_user += ", ".join(e)
                            print(edit_user)
                            with open("tasks.txt", "w") as user_edit:
                                user_edit.write(f"{edit_user}")

# Date edit
# Same method applied as above

                    elif edit_task == 2:
                        edit_date = ""
                        with open("tasks.txt", "r+") as date_edit:
                            for d, e in enumerate(date_edit, 1):
                                e = e.split(", ")
                                if d == z:
                                    e[4] = input("\nEnter new due date here (eg. 5 Nov 2021): ")
                                edit_date += ", ".join(e)
                            print(edit_date)
                            with open("tasks.txt", "w") as date_edit:
                                date_edit.write(f"{edit_date}")
                         
                    else:
                        print("You did not select an appropriate option.")

                else:
                    print("You did not select an appropriate option.")

# Generate report function
# Write to task_overview txt file
# The below is to calculate the total tasks, total completed tasks, total incompleted tasks, overdue tasks and incomplete task percentage

def generate_report():
    from datetime import datetime
    with open("tasks.txt", "r") as generate_report:
        generate_report = generate_report.readlines()
        task_total = 0
        completed_tasks = 0
        incompleted_tasks = 0
        due_dates = 0
        overdue_tasks = 0
        incomplete_perc = 0
        overdue_perc = 0
        
        with open("task_overview.txt", "w") as task_ovw:
            for gr in generate_report:
                gr = gr.strip("\n").split(", ")
                due_dates = datetime.strptime(gr[4], "%d %b %Y")
                task_total += 1
                
                if gr[5] == "Yes":
                    completed_tasks += 1
                else: incompleted_tasks += 1

                if (datetime.today() > due_dates) and (gr[5] == "No"):
                    overdue_tasks += 1
                
            incomplete_perc = round((incompleted_tasks / task_total) * 100, 2)
            overdue_perc = round((overdue_tasks / task_total) * 100, 2)

            task_ovw.write(f'''Task Overview:

Task total:\t\t\t\t {task_total}
Completed Tasks:\t\t\t {completed_tasks}
Incompleted Tasks:\t\t\t {incompleted_tasks}
Overdue Tasks:\t\t\t\t {overdue_tasks}
Incomplete Task Percentage:\t\t {incomplete_perc}%
Overdue Task Percentage:\t\t {overdue_perc}%''')

            print(f'''
Your Task and User Overview has successfully been updated as follows:

Task Overview:

Task total:\t\t\t\t {task_total}
Completed Tasks:\t\t\t {completed_tasks}
Incompleted Tasks:\t\t\t {incompleted_tasks}
Overdue Tasks:\t\t\t\t {overdue_tasks}
Incomplete Task Percentage:\t\t {incomplete_perc}%
Overdue Task Percentage:\t\t {overdue_perc}%

-------------------------------------------------------''')
            
# Write to user overview txt file
# The below is done to calculate the total tasks per user, total percentage tasks complete per user,
# total percentage incomplete per user, percentage which is incomplete and overdue and percentage of tasks assigned to user from total tasks
    
    with open("user_overview.txt", "w") as user_overview:
        with open("user.txt", "r+") as user_report:
            user_report = user_report.readlines()
            with open("tasks.txt", "r+") as task_report:
                task_report = task_report.readlines()

                for ur in user_report:
                    ur = ur.split(", ")[0]
                    user_count = 0
                    task_count = 0
                    user_task_total = 0
                    user_task_perc = 0
                    task_comp = 0
                    task_incomp = 0
                    user_perc_complete = 0
                    user_perc_incomplete = 0
                    inc_overdue = 0
                    perc_inc_overdue = 0

                    user_count += 1

                    for tr in task_report:
                        tr = tr.strip("\n")
                        task_count += 1
                        if tr.startswith(ur):
                            if tr.endswith("Yes"):
                                task_comp += 1
                            if tr.endswith("No"):
                                task_incomp += 1
                            if (tr.endswith("No")) and (datetime.today() > due_dates):
                                inc_overdue += 1
                            user_task_total += 1

                    if user_task_total != 0:
                        user_task_perc = round((user_task_total / task_count) * 100, 2)
                    else:
                        user_task_perc = 0

                    if task_comp != 0:
                        user_perc_complete = round((task_comp / user_task_total) * 100, 2)
                    else:
                        user_perc_complete = 0

                    if task_incomp != 0:
                        user_perc_incomplete = round((task_incomp / user_task_total) * 100, 2)
                    else:
                        user_perc_incomplete = 0

                    if inc_overdue != 0:
                        perc_inc_overdue = (inc_overdue / user_task_total) * 100
                    else:
                        perc_inc_overdue = 0
                            

                    user_overview.write(f'''
{ur} Report:

Total Tasks:\t\t\t\t {user_task_total}
Percentage Tasks assigned:\t\t {user_task_perc}%
Percentage completed:\t\t\t {user_perc_complete}%
Percentage incomplete:\t\t\t {user_perc_incomplete}%
Percentage incomplete and overdue:\t {perc_inc_overdue}%
''')
                        
                    print(f'''
{ur} Report:

Total Tasks:\t\t\t\t {user_task_total}
Percentage Tasks assigned:\t\t {user_task_perc}%
Percentage completed:\t\t\t {user_perc_complete}%
Percentage incomplete:\t\t\t {user_perc_incomplete}%
Percentage incomplete and overdue:\t {perc_inc_overdue}%
''')

# The below function is the same as 'generate_report' function
# The only difference is that the print for user is removed
# This is done to call the same function of 'generate_report' when selecting 's' for statistics
# Only the function will be used and the report will not be printed when 's' is selected

def insert_report():
   from datetime import datetime
   with open("tasks.txt", "r") as generate_report:
        generate_report = generate_report.readlines()
        task_total = 0
        completed_tasks = 0
        incompleted_tasks = 0
        due_dates = 0
        overdue_tasks = 0
        incomplete_perc = 0
        overdue_perc = 0
        
        with open("task_overview.txt", "w") as task_ovw:
            for gr in generate_report:
                gr = gr.strip("\n").split(", ")
                due_dates = datetime.strptime(gr[4], "%d %b %Y")
                task_total += 1
                
                if gr[5] == "Yes":
                    completed_tasks += 1
                else: incompleted_tasks += 1

                if (datetime.today() > due_dates) and (gr[5] == "No"):
                    overdue_tasks += 1
                
            incomplete_perc = round((incompleted_tasks / task_total) * 100, 2)
            overdue_perc = round((overdue_tasks / task_total) * 100, 2)

            task_ovw.write(f'''Task Overview:

Task total:\t\t\t\t {task_total}
Completed Tasks:\t\t\t {completed_tasks}
Incompleted Tasks:\t\t\t {incompleted_tasks}
Overdue Tasks:\t\t\t\t {overdue_tasks}
Incomplete Task Percentage:\t\t {incomplete_perc}%
Overdue Task Percentage:\t\t {overdue_perc}%''')

# user_overview
    
        with open("user_overview.txt", "w") as user_overview:
            with open("user.txt", "r+") as user_report:
                user_report = user_report.readlines()
                with open("tasks.txt", "r+") as task_report:
                    task_report = task_report.readlines()

                    for ur in user_report:
                        ur = ur.split(", ")[0]
                        user_count = 0
                        task_count = 0
                        user_task_total = 0
                        user_task_perc = 0
                        task_comp = 0
                        task_incomp = 0
                        user_perc_complete = 0
                        user_perc_incomplete = 0
                        inc_overdue = 0
                        perc_inc_overdue = 0

                        user_count += 1

                        for tr in task_report:
                            tr = tr.strip("\n")
                            task_count += 1
                            if tr.startswith(ur):
                                if tr.endswith("Yes"):
                                    task_comp += 1
                                if tr.endswith("No"):
                                    task_incomp += 1
                                if (tr.endswith("No")) and (datetime.today() > due_dates):
                                    inc_overdue += 1
                                user_task_total += 1

                        if user_task_total != 0:
                            user_task_perc = round((user_task_total / task_count) * 100, 2)
                        else:
                            user_task_perc = 0

                        if task_comp != 0:
                            user_perc_complete = round((task_comp / user_task_total) * 100, 2)
                        else:
                            user_perc_complete = 0

                        if task_incomp != 0:
                            user_perc_incomplete = round((task_incomp / user_task_total) * 100, 2)
                        else:
                            user_perc_incomplete = 0

                        if inc_overdue != 0:
                            perc_inc_overdue = (inc_overdue / user_task_total) * 100
                        else:
                            perc_inc_overdue = 0
                                

                        user_overview.write(f'''
    {ur} Report:

    Total Tasks:\t\t\t\t {user_task_total}
    Percentage Tasks assigned:\t\t {user_task_perc}%
    Percentage completed:\t\t\t {user_perc_complete}%
    Percentage incomplete:\t\t\t {user_perc_incomplete}%
    Percentage incomplete and overdue:\t {perc_inc_overdue}%
    ''')
                          
# The below if functions are still required although it is defined in the menu functions
# As the menu functions are used when called, but the below if functions are still required for the initial login
# Register user

if (option_selection == "r") and (username == "admin"):
    reg_user()

# Add task

if option_selection == "a":
    add_task()

# View all tasks

if option_selection == "va":
    view_all()

# View my tasks

if option_selection == "vm":
    view_mine()

# Generate report

if option_selection == "gr":
    generate_report()          

# Statistics

if option_selection == "s":
    insert_report()
    
# User Stats
    
    user_stat_list = []
    user_stat_total = 0
    with open("user_overview.txt", "r") as user_stats:
        user_stats = user_stats.readlines()
        for us in user_stats:
            us = us.strip().split("\t ")
            user_stat_list.append(us)

        for ust in user_stat_list:
            if "Total Tasks:\t\t\t" in ust:
                user_stat_total += 1
        print(f"Users:\t\t\t {user_stat_total}")

# Task stats

    task_stat_list = []
    task_stat_total = 0
    with open("task_overview.txt", "r") as task_stats:
        task_stats = task_stats.readlines()
        for ts in task_stats:
            ts = ts.strip().split("\t ")
            task_stat_list.append(ts)

        for tst in task_stat_list:
            if "Task total:\t\t\t" in tst:
                task_stat_total = tst[1]
    print(f"Tasks:\t\t\t {task_stat_total}")

# Exit

if option_selection == "e":
    print("\nYou have successfull logged out.")
        
