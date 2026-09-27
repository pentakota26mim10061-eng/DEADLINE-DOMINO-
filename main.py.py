tasks = []


def add_task():
    print("\n--- ADD TASK ---")
    title = input("Task name: ").strip()
    if title == "":
        print("Task name cannot be empty.")
        return

    subject = input("Subject/category: ").strip()
    if subject == "":
        subject = "General"

    hours_text = input("Estimated hours: ")
    urgency = input("Urgency (1-Low, 2-Medium, 3-High): ")

    if not hours_text.isdigit():
        print("Please enter hours as a positive whole number.")
        return

    if not urgency.isdigit() or int(urgency) not in [1, 2, 3]:
        print("Urgency must be 1, 2 or 3.")
        return

    hours = int(hours_text)
    urgency = int(urgency)

    if hours <= 0:
        print("Hours must be greater than zero.")
        return

    
    score = hours * urgency

    task = [title, subject, hours, urgency, score, "Pending"]
    tasks.append(task)
    print("Task added to the Deadline Domino board.")


def show_tasks():
    print("\n--- TASK BOARD ---")
    if len(tasks) == 0:
        print("No tasks have been added.")
        return

    number = 1
    for task in tasks:
        print(str(number) + ". " + task[0])
        print("   Subject :", task[1])
        print("   Hours   :", task[2])
        print("   Urgency :", urgency_name(task[3]))
        print("   Score   :", task[4])
        print("   Status  :", task[5])
        number = number + 1


def urgency_name(level):
    if level == 1:
        return "Low"
    elif level == 2:
        return "Medium"
    else:
        return "High"


def show_next_tasks():
    print("\n--- DOMINO ORDER ---")
    if len(tasks) == 0:
        print("No tasks are available.")
        return

    pending = []
    for task in tasks:
        if task[5] == "Pending":
            pending.append(task)

    if len(pending) == 0:
        print("All tasks are completed.")
        return

    
    position = 1
    while len(ordered) > 0:
        best_index = 0
        index = 1

        while index < len(ordered):
            if ordered[index][4] > ordered[best_index][4]:
                best_index = index
            index = index + 1

        chosen = ordered[best_index]
        print(str(position) + ". " + chosen[0] +
              " | " + urgency_name(chosen[3]) +
              " | " + str(chosen[2]) + " hour(s)" +
              " | Score " + str(chosen[4]))

        del ordered[best_index]
        position = position + 1


def complete_task():
    print("\n--- COMPLETE TASK ---")
    if len(tasks) == 0:
        print("No tasks are available.")
        return

    show_tasks()
    choice = input("Enter task number to complete: ")

    if not choice.isdigit():
        print("Enter a valid task number.")
        return

    number = int(choice)

    if number < 1 or number > len(tasks):
        print("Task number is outside the board.")
        return

    tasks[number - 1][5] = "Completed"
    print("Task marked as completed.")


def delete_task():
    print("\n--- DELETE TASK ---")
    if len(tasks) == 0:
        print("No tasks are available.")
        return

    show_tasks()
    choice = input("Enter task number to delete: ")

    if not choice.isdigit():
        print("Enter a valid task number.")
        return

    number = int(choice)

    if number < 1 or number > len(tasks):
        print("Task number is outside the board.")
        return

    removed = tasks.pop(number - 1)
    print("Removed:", removed[0])


def workload_report():
    print("\n--- WORKLOAD REPORT ---")
    if len(tasks) == 0:
        print("No tasks are available.")
        return

    total_hours = 0
    pending_hours = 0
    completed_hours = 0
    high_count = 0

    for task in tasks:
        total_hours = total_hours + task[2]

        if task[5] == "Pending":
            pending_hours = pending_hours + task[2]
        else:
            completed_hours = completed_hours + task[2]

        if task[3] == 3 and task[5] == "Pending":
            high_count = high_count + 1

    print("Total planned hours :", total_hours)
    print("Pending hours       :", pending_hours)
    print("Completed hours     :", completed_hours)
    print("High-urgency pending:", high_count)

    if pending_hours == 0:
        print("Load status: CLEAR")
    elif pending_hours <= 5:
        print("Load status: LIGHT")
    elif pending_hours <= 10:
        print("Load status: BUSY")
    else:
        print("Load status: DOMINO RISK")

    print("\nTip: Start with the first task in 'Domino Order' so that a high-score task does not create a chain of unfinished work.")


def subject_summary():
    print("\n--- SUBJECT SUMMARY ---")
    if len(tasks) == 0:
        print("No tasks are available.")
        return

    subjects = []
    hours = []

    for task in tasks:
        subject_index = -1
        index = 0

        while index < len(subjects):
            if subjects[index] == task[1]:
                subject_index = index
                break
            index = index + 1

        if subject_index == -1:
            subjects.append(task[1])
            hours.append(task[2])
        else:
            hours[subject_index] = hours[subject_index] + task[2]

    index = 0
    while index < len(subjects):
        print(subjects[index], ":", hours[index], "hour(s)")
        index = index + 1


def menu():
    while True:
        print("\n" + "=" * 52)
        print("                 DEADLINE DOMINO")
        print("       Academic Workload & Task Flow Planner")
        print("=" * 52)
        print("1. Add task")
        print("2. View task board")
        print("3. Show Domino Order")
        print("4. Complete task")
        print("5. Delete task")
        print("6. Workload report")
        print("7. Subject summary")
        print("8. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            show_tasks()
        elif choice == "3":
            show_next_tasks()
        elif choice == "4":
            complete_task()
        elif choice == "5":
            delete_task()
        elif choice == "6":
            workload_report()
        elif choice == "7":
            subject_summary()
        elif choice == "8":
            print("Thank you for using Deadline Domino.")
            break
        else:
            print("Invalid choice. Please select 1 to 8.")


menu()
