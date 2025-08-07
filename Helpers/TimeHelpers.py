import time
import sys
from Helpers.GenericHelpers import GenericHelpers

class TimeHelpers:

    def ElapsedPause(self, pauseTimeInMins, pauseStart):
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

                if iterations:
                    if (hours and hours % hourIntervals == 0) or (mins and mins % minIntervals == 0) or secs == 0:
                        pauseStart = time.time()
                        if GenericHelpers().Mbox('Pomodoro', f'It has been {f"{hours:02}h and "if hours else ""}{hours:02}h and {mins:02}min. Pause ?', 4) == 6:
                            startTime = startTime + self.ElapsedPause(5, pauseStart)
                        else:
                            startTime = startTime + self.ElapsedPause(0, pauseStart)
                        iterations -= 1
                
                else:
                    pauseStart = time.time()
                    GenericHelpers().Mbox('Pomodoro', f"It has been {f"{hours:02}h and "if hours else ""}{mins:02}min.\nHave a break !", 0)
                    startTime = startTime + self.ElapsedPause(20, pauseStart)                    
                    endLoop = True

        except KeyboardInterrupt:
            print("\nStopwatch stopped.")
        except Exception as e:
            print("\nError :", e)


    def CountDown(self, timeInMin):
        try:
            if timeInMin:
                for remaining in range(timeInMin * 60, 0, -1):
                    sys.stdout.write("\r")
                    sys.stdout.write("{:2d} mins remaining. Press Ctrl + C to interrupt countdown.".format(int(remaining / 60))) 
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