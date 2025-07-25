import time
import subprocess
import sys

try:
    from wakepy import keep
except ImportError:
    print("WakePy not found. Installing...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "wakepy"])
    from wakepy import keep

    print("WakePy installed successfully.")


class WakePy:
    def __init__(self, name):
        self.name = name
        

    def Run(self):
        with keep.presenting() as mode:
            #https://wakepy.readthedocs.io/stable/user-guide.html
            #print(mode.activation_result) #for detailed state check
            isBack = False

            try: timeInMin = int(input("Choose a number of minutes and/or press enter.\n-> ").strip())
            except: timeInMin = 0

            while not isBack:
                if timeInMin != 0:
                    print(f"Presenting mode enabled for {timeInMin} min.")
                    time.sleep(timeInMin * 60)
                    timeInMin = 0
                    isBack = True
                else:
                    print(f"{self.name} is AFK.\nPresenting mode engaged unil new input.")
                    isBack = bool(input())
            
            print(f"Welcome back {self.name} :)")
                                          

if __name__ == '__main__':
    WakePy().Run()