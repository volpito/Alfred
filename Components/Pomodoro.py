import json
import sys
import time


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


    def ElapsedPause(self, message):
        pauseStart = time.time()

        if input(f'{message}\n-> ').strip().casefold() == 'y':
            #TimerHelpers.CountDown()
            time.sleep(5 * 60)
        else:
            self.flowModoro = True

        return time.time() - pauseStart
        

    def StopWatch(self):
        endLoop = False
        start_time = time.time()
        try:
            while not endLoop:
                elapsed = time.time() - start_time
                mins, secs = divmod(int(elapsed), 60)
                hours, mins = divmod(mins, 60)
                sys.stdout.write("\r")
                sys.stdout.write(f"Stopwatch : {hours:02}:{mins:02}:{secs:02}")
                sys.stdout.flush()
                time.sleep(1)

                if mins != 0 and (mins % 25 == 0 and secs == 0):
                    start_time = start_time + self.ElapsedPause("\nIt has been 25mn. Pause ? y|n")

                if hours == 1 and mins == 40 and secs == 0:
                    start_time = start_time + self.ElapsedPause("\nIt has been 1h40.\nHave a 20mn break ! Go stretch or get soome air\nYou deserved it :)")
                    endLoop = True

        except KeyboardInterrupt:
            print("\nStopwatch stopped.")



    def Run(self):
        self.Read()
        endLoop = False

        if self.Tasks:
            if input(f"You have {len(self.Tasks)} uncompleted task(s).\nWould you like to clear them ? y|n\n-> ").strip().casefold() == "y":
                self.Tasks = []
                self.Write()
        else:
            print("No task found.")

        while not endLoop:
            newTask = input('Would you like to add a task to the list ?\nPlease type it here and/or press Enter\n-> ')
            if newTask:
                self.Tasks += [newTask]
                self.Write()
            else:
                endLoop = True
            
        if self.Tasks:        
            endLoop = False
            
            while not endLoop:
                try:
                    print("Here are your remaining task(s) :")
                    for idTask, task in enumerate(self.Tasks):
                        print(idTask, '-', task)
                    chosenID = input("Would you like to pick one ? (enter a number or EXIT)\n-> ").strip().casefold()
                    chosen = self.Tasks[int(chosenID)]
                    if chosen :
                        print(chosen)
                        self.StopWatch()

                        while input('Are you done with this task ? y|n\n-> ').strip().casefold() == 'n':
                            self.StopWatch()

                        if input('Would you like to remove this task from your list ? y|n \n-> ').strip().casefold() == 'y':
                            self.Tasks.remove(chosen)
                            self.Write()

                except:
                    endLoop = chosenID == "exit"
                    print("Wrong entry... Try again" if not endLoop else 'Going back to main Menu...', "\n") 
                

        print("--")

                


if __name__ == '__main__':
    Pomodoro().Run()