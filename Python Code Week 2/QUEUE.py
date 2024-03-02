# #============== DATA STRUCTURES QUEUE =====================

# # ---------EXERCISE 1 ---------

# # Simple To Do List class
# class ToDoList:

#     # Constructor to initialize an empty list
#     def __init__(self):
#         # List for storing tasks
#         self.tasks = []


#     # Method to add a task to the list
#     def add_task(self, task):
#         # Append the task to the list
#         self.tasks.append(task)
#         # Print a message indicating success
#         print(f"• {task} added successfully to the list.")


#     # Method to remove a task from the list once done
#     def remove_task(self, task):
#         # Check if the task is in the list or not
#         if task in self.tasks:
#             # Remove the task from the list
#             self.tasks.remove(task)
#             # Print a message indicating success
#             print(f"\n{task} has been removed successfully from the list.")
#         else:
#             # Print a message indicating that the task was not found
#             print(f'Task entered "{task}" was not found in the list.')


#     # Method to display all tasks in the list
#     def display_tasks(self):
#         # Check if the list is empty
#         if not self.tasks:
#             # Print a message if there are no tasks
#             print('You currently have no tasks listed.\n')
#         else:
#             # Print each task in the list with its index
#             print('\nTasks in the list:')
#             for x, task in enumerate(self.tasks, start=1): 
#                 #enumerate returns pairs of index and its value
#                 print(f'{x}. {task}')


# # Create an instance of the ToDoList class
# todolist = ToDoList()

# # Display the initial state of the list
# todolist.display_tasks()

# # Add tasks to the list
# todolist.add_task("Buy groceries")
# todolist.add_task("Go Exercise")

# # Display the updated list
# todolist.display_tasks()

# # Remove tasks from the list
# todolist.remove_task("Buy groceries")
# todolist.remove_task("Gym Jao")  # This task is not in the list - see what happens

# # Display the final state of the list
# todolist.display_tasks()



# # ---------EXERCISE 2 ---------

# class GroceryQueue:

#     # Constructor to initialize an empty queue
#     def __init__(self):
#         # Queue to store customers
#         self.queue = []


#     # Method to add a customer to the end of the queue
#     def add_customer(self, customer_name):
#         # Append the customer to the end of the queue
#         self.queue.append(customer_name)
#         # Print a message indicating success
#         print(f"• New customer {customer_name} has joined the queue.")


#     # Method to serve the customer at the front of the queue
#     def serve_customer(self):
#         # Checks if the queue is not empty
#         if self.queue:
#             # Remove the customer at the front of the queue
#             served_customer = self.queue.pop(0)
#             # Print a message indicating success
#             print(f"{served_customer} has been served.")
#         else:
#             # Print a message indicating that the queue is empty
#             print("No customers are queue'd up.")


#     # Method to display all customers in the queue
#     def display_queue(self):
#         # Check if the queue is empty
#         if not self.queue:
#             # Print a message if the queue is empty
#             print('The queue is currently empty.\n')
#         else:
#             # Print each customer in the queue
#             print('\nCustomers waiting in the queue:')
#             for x, customer in enumerate(self.queue, start=1):
#                 print(f'{x}. {customer}')


# # Create an instance of the GroceryStoreQueue class
# grocery_queue = GroceryQueue()

# # Display the initial state of the queue
# grocery_queue.display_queue()

# # Add customers to the queue
# grocery_queue.add_customer("Ari")
# grocery_queue.add_customer("Seam")
# grocery_queue.add_customer("Alex")

# # Display the updated queue
# grocery_queue.display_queue()

# # Serve customers from the queue
# grocery_queue.serve_customer()
# grocery_queue.serve_customer()

# # Display the final state of the queue
# grocery_queue.display_queue()