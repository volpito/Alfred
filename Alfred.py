import sys 
from enum import Enum
from Components.Weather_API import WeatherRequest
from Components.WakePy_Repo import WakePy
from Components.Calculator import Calculator


class Choices(Enum):
	CALCULATOR = '1'
	WEATHER = '2'
	TODO = '3'
	WAKEPY = '4'
	EXIT = '5'
	

class Hello:

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

				case Choices.TODO.name | Choices.TODO.value:
					self.PrintStrWithWhiteSpaces("Not Implemented yet")
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
	Hello(str(sys.argv[1])).Run()