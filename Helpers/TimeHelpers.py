import time
import sys
from Helpers.GenericHelpers import GenericHelpers

class TimeHelpers:

    def ElapsedPause(self, pauseTimeInMins):
        pauseStart = time.time()
        self.CountDown(pauseTimeInMins)
        return time.time() - pauseStart


    def CountUp(self, intervalInMins, iterations, startTime = time.time()):
        try:
            endLoop = False
            hourIntervals, minIntervals = divmod(intervalInMins, 60)

            while not endLoop:
                elapsed = time.time() - startTime
                mins, secs = divmod(int(elapsed), 60)
                hours, mins = divmod(mins, 60)
                sys.stdout.write("\r")
                sys.stdout.write(f"Stopwatch : {hours:02}:{mins:02}:{secs:02}")
                sys.stdout.flush()
                time.sleep(1)

                if iterations != 0 and mins != 0 and (hours % hourIntervals == 0 and mins % minIntervals == 0 and secs == 0):
                    if GenericHelpers().Mbox('Pomodoro', f'It has been {hours:02}h and {mins:02}min. Pause ?', 4) == 6:
                        startTime = startTime + self.ElapsedPause(5)
                    iterations -= 1
                
                if iterations == 0:
                    GenericHelpers().Mbox('Pomodoro', f"\nIt has been {hours:02}h and {mins:02}min. Have a break.", 0)
                    startTime = startTime + self.ElapsedPause(20)                    
                    endLoop = True

        except KeyboardInterrupt:
            print("\nStopwatch stopped.")
        except Exception as e:
            print("Error :", e)


    def CountDown(self, timeInMin):
        try:
            for remaining in range(timeInMin * 60, 0, -1):
                sys.stdout.write("\r")
                sys.stdout.write("{:2d * 60} mins remaining.".format(remaining)) 
                sys.stdout.flush()
                time.sleep(1)

        except KeyboardInterrupt:
            print("\nStopwatch stopped.")

        sys.stdout.flush()
        sys.stdout.write("\r")


'''if __name__ == "__main__":
    t = TimeHelpers()
    v = time.time()
    t.CountUp(v)'''