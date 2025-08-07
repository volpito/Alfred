import json
import time
from Helpers.TimeHelpers import TimeHelpers


class Pomodoro:
    def __init__(self):
        self.jsonPath = "Components/todoList.json"
        #self.flowModoro = False

    
    def Read(self):
        with open(self.jsonPath, "r") as f:
            self.Tasks = json.load(f)


    def Write(self):
        json_str = json.dumps(self.Tasks, indent=4)
        with open(self.jsonPath, "w") as f:
            f.write(json_str)


    def AddTask(self):
        endLoop = False
        while not endLoop:
            newTask = input('To add a task, please type it here and/or press Enter\n-> ')
            if newTask:
                self.Tasks += [newTask]
                self.Write()
            else:
                endLoop = True


    def ClearTasks(self):
        self.Tasks = []
        self.Write()
        

    def StopWatch(self):
        startTime = time.time()
        TimeHelpers().CountUp(25, 4, startTime)
        

    def Run(self):
        self.Read()

        if self.Tasks:
            print(f"You have {len(self.Tasks)} uncompleted task(s).\n")
        else:
            print("No task found.\n")
            self.AddTask()
            
        if self.Tasks:        
            endLoop = False
            
            while not endLoop:
                try:
                    print("Here are your remaining task(s) :")
                    for idTask, task in enumerate(self.Tasks):
                        print(idTask, '-', task)
                    chosenID = input("\nWhat would you like to do ? (enter a number, NEW, CLEAR or EXIT)\n-> ").strip().casefold()
                    chosen = self.Tasks[int(chosenID)]
                    if chosen :
                        print(chosen)
                        self.StopWatch()

                        while input('Are you done with this task ? y|n\n-> ').strip().casefold() == 'n':
                            print(chosen)
                            self.StopWatch()

                        if input('Would you like to remove this task from your list ? y|n \n-> ').strip().casefold() == 'y':
                            self.Tasks.remove(chosen)
                            self.Write()

                except Exception as e:
                    match chosenID:
                        case "new":
                            self.AddTask()
                        case "clear":
                            self.ClearTasks()
                        case "exit":
                            endLoop = chosenID == "exit"
                        case _:
                            print(f"Error : {e}\n") 

        print('Going back to main Menu...\n')


if __name__ == '__main__':
    Pomodoro().Run()