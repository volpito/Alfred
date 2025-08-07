import sys 
from enum import Enum
from Components.Weather_API import WeatherRequest
from Components.WakePy_Repo import WakePy
from Components.Calculator import Calculator
from Components.Pomodoro import Pomodoro


class Choices(Enum):
	EXIT = '0'
	WAKEPY = '1'
	POMODORO = '2'
	WEATHER = '3'
	CALCULATOR = '4'
		
	

class Run:

	def __init__(self, name=None):
		self.name = name.capitalize()


	def Run(self):
		self.SayHi()
		self.UserChoice()


	def SayHi(self): 
		print("Hello there !")
		count = 0

		while not self.name and count != 3:
			self.name = input("What's your name dear?\n-> ").strip().capitalize()
			count+=1

		if len(self.name) == 1 or not self.name:
			self.PrintStrWithWhiteSpaces("...\nOkay smartass, I'll call you Dumdum.")
			self.name = 'Dumdum'


	def UserChoice(self):
		endLoop = False
		print(f"Nice to have you here {self.name}, how can I help you today ?")

		while not endLoop:
			print("Please choose from the following options :")
			for choice in Choices:
				print(choice.value, "-", choice.name)

			ask = input("-> ").strip().upper()
			print("--")

			match ask:
				case Choices.CALCULATOR.name | Choices.CALCULATOR.value:
					Calculator().Equal()
					print("--")

				case Choices.WEATHER.name | Choices.WEATHER.value:
					WeatherRequest().Run()
					print("--")

				case Choices.POMODORO.name | Choices.POMODORO.value:
					Pomodoro().Run()
					print("--")

				case Choices.WAKEPY.name | Choices.WAKEPY.value:						
					WakePy(self.name).Run()
					print("--")

				case Choices.EXIT.name | Choices.EXIT.value:
					endLoop = True

				case _:
					self.PrintStrWithWhiteSpaces(f"No '{ask}' command was found :(\nStarting over !\n--")

		print(f'Have a nice day {self.name}')
		return
	

	def PrintStrWithWhiteSpaces(self, str):
		print(f"\n{str}\n")


if __name__ == '__main__' :
	Run(str(sys.argv[1] if len(sys.argv) > 1 else "")).Run()