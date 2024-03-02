#============== TASK COMPLETION CLASS =====================

#Task Class

class Task:

    def __init__(self, description):
        #task attribute
        self.description = description

    def complete(self):
        print(f"\nTask at hand {self.description} is now complete")
    # print for task being completed
            
    # deleting tasks
    def __del__(self):
    # Destructor method that prints a message when a Car object is deleted
        print(f"\n{self.description} has been deleted.")

    
    def cleanup(self):
        print(f"\nClean up, clean up, everybody everywhere {self.description}")
        # method cleanup message simulating the cleanup of resources associated with the task

        

# task object
firstTask = Task("Sweeping Complete")
        
# Completing the task - links to the complete function
firstTask.complete()

# Cleaning up resources when no longer needed
firstTask.cleanup()

#deleting Task
del firstTask


