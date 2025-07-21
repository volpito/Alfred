import sys 
from enum import Enum
from Requests import WeatherRequest

class Choices(Enum):
	CALCULATOR = '1'
	WEATHER = '2'
	TODO = '3'
	EXIT = '4'
	

class Hello:

	def __init__(self, name=None):
		self.name = name

	def Run(self):
		self.SayHi()
		self.UserChoice()



	def SayHi(self): 
		print("Hello there !")
		count = 0

		while not self.name and count != 3:
			self.name = input("What's your name dear?\n").strip().capitalize()
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

			ask = input().strip().upper()
			print("--")

			match ask:
				case Choices.CALCULATOR.name | Choices.CALCULATOR.value:
					self.PrintStrWithWhiteSpaces("Not Implemented yet")
					print("--")

				case Choices.WEATHER.name | Choices.WEATHER.value:
					WeatherRequest().Run()
					print("--")

				case Choices.TODO.name | Choices.TODO.value:
					self.PrintStrWithWhiteSpaces("Not Implemented yet")
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
	Hello().Run()