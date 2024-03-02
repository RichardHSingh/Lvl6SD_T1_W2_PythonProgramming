#============== DATA STRUCTOR STACK =====================

# # ---------EXERCISE 1 ---------

# # Creating class
# class Stack:

#     # Constructor for the stack, written in []
#     def __init__(self):
#         self.items = []

#     # Method to add items into the stack
#     def push(self, item):
#         self.items.append(item)

#     # Checking if the stack is not empty before deleting
#     def pop(self):
#         if not self.stack_empty():
#             return self.items.pop()

#     # Method for ensuring the stack isn't already empty
#     def stack_empty(self):
#         return len(self.items) == 0

# def stack_reverse(input_items):
#     # Using a stack to reverse the items
#     reverse_stack = Stack()

#     # Pushing items into the stack
#     for item in input_items:
#         reverse_stack.push(item)

#     # Popping the items from the stack to reverse it
#     reversed_list = []
#     while not reverse_stack.stack_empty():
#         reversed_list.append(reverse_stack.pop())

#     return reversed_list


# input_items = [1, 2, 3, 4, 5]
# reversed_result = stack_reverse(input_items)

# print("Original List:", input_items)
# print("Reversed List:", reversed_result)

# # output Original List: [1, 2, 3, 4, 5]
# # output Reversed List: [5, 4, 3, 2, 1]



# ---------EXERCISE 2 ---------

# creating class to undo an action

class AlterStack:
    def __init__(self):
        self.actions = []
        self.undo_stack = []

    def add_action(self, action):
        # Add a new action to the list of actions
        self.actions.append(action)
        print(f"Action implemented: {action}")

    def undo_action(self):
        # Check if there are any actions to undo
        if not self.actions:
            print("There are no actions to alter/undo")
            return

        # Pop the last action and add it to the undo stack
        last_action = self.actions.pop()
        self.undo_stack.append(last_action)
        print(f"Altering previous action: {last_action}")

    def redo_action(self):
        # Check if there are undone actions to reverse the changes
        if not self.undo_stack:
            print("There are no actions to redo")
            return

        # Pop the last undone action and add it back to the list of actions
        last_undo = self.undo_stack.pop()
        self.actions.append(last_undo)
        print(f"Redoing previous action - make up your mind ..gosh: {last_undo}")

def action():
    alterstack = AlterStack()

    while True:
        # Display the menu options
        print("\nMenu:")
        print("1. Take action")
        print("2. Undo previous action")
        print("3. Redo previous undo")
        print("4. Continue with program")
        print("5. Exit program")

        # Get the user's choice
        choice = input("Enter your choice: ")

        # Define a dictionary mapping choices to corresponding functions
        menu_actions = {
            '1': alterstack.add_action,
            '2': alterstack.undo_action,
            '3': alterstack.redo_action,
            '4': continue_program,
            '5': exit_program
        }

        # Get the function associated with the user's choice or if the choice is invalid, do nothing
        selected_action = menu_actions.get(choice)

        if selected_action:
            # Call the selected function
            if choice == '4':
                continue_program()
            else:
                selected_action(input("Enter action: "))  # Changed here to include an input prompt
        else:
            # Handle invalid choices
            print("Invalid choice. Please try again.")

def continue_program():
    # Function to handle the "Continue" option
    print("Continuing with program...")

def exit_program():
    # Function to handle the "Exit" option
    print("Exiting program.")
    exit()

# Call the action function to start the program
action()
