import random
import operator
import os
import time
from colorama import Fore, Back, Style
os.system("cls" or "clear")
print(Style.RESET_ALL)
print("################ Quizz Maker ################")
print('GitHub : https://github.com/KursK-sys')

words = {
	# put here the words / expression that you want to guess
# examples :
	"python" : "interpreted",
	"java" : "compiled",
	"ruby" : "interpreted",
	"C" : "compiled",
	"C++" : "compiled",
	"Bill" : "Gates",
	"John" : "Cena",
	"Elon" : "Musk" or "musk", #...
	"Date of WW1" : "14-18",
	"Date of WW2" : "39-45",
	"Date of WW2" : "39-45",
	"Date of WW3" : "Soon" or "soon"

}
def practice():
	print("Starting practice mode...")
	time.sleep(0.5)
	os.system("cls" or "clear")
	print("Practice mode Rules : you must write the corresponding word. Example: Elon -> Musk ")
	a=0
	count=0
	while count<20:
		c =random.choice(list(words))
		get_item_with_key = operator.itemgetter(c)
		mot = get_item_with_key(words)
		test = input(f"{c} -> ")

		if test == mot:
			print(Fore.GREEN + 'True')
			print(Style.RESET_ALL)
			a=a+1
			count=count+1
			print(f"Score : {a}")

			print(f"Stage {count} /20")
			time.sleep(1)
			os.system("cls")
		else:
			print(Fore.RED + "False\n"+ Style.RESET_ALL + f"This is : {mot}")
			print("")
			print(f"Score : {a}")
			count=count+1
			print(f"Stage {count} /20")
			time.sleep(2)
			os.system("cls")
			rep_get = operator.itemgetter(c)
			rep_mot = get_item_with_key(words)
			test2 = input(f"{c} ->" )

			if test2 == rep_mot:
				print(Fore.GREEN + "That's it!")
				print(Style.RESET_ALL)
				time.sleep(1)
				os.system("cls")
			else:
				count=count+1
				print(Fore.RED + "It's still wrong!")
				print(Style.RESET_ALL)
				print(f"Stage {count} /20")
				time.sleep(1)
				os.system("cls")

def test():
	print("Starting test mode...")
	time.sleep(0.5)
	os.system("cls" or "clear")
	print("Test mode Rules : you must write the corresponding word.")
	a=0
	count=0
	while count<20:
		c =random.choice(list(words))
		get_item_with_key = operator.itemgetter(c)
		mot = get_item_with_key(words)
		test = input(f"{c} -> ")

		if test == mot:
			print(Fore.GREEN + 'True')
			print(Style.RESET_ALL)
			a=a+1
			count=count+1
			print(f"Score : {a}")

			print(f"Stage {count} /20")
			time.sleep(1)
			os.system("cls")
		else:
			print(Fore.RED + "False")
			print(Style.RESET_ALL)
			print("")
			print(f"Score : {a}")
			count=count+1
			print(f"Stage {count} /20")
			time.sleep(2)
			os.system("cls")



	print(f"Your score is {a}/20")
	print(f"Success rate :  {100*a/count}%")
	if count>10:
		print("You are above average!")
	if count<10:
		print("You are below average...")

	print("Press enter to exit")
	exit = input()




print("Which mode do you play? [P]ractice - [T]est")
choice = input("")
try:
	if choice == "P":
		practice()
	if choice == "T":
		test()
	else:
		print("Please select a valid option")
		time.sleep(3)
		os.system("cls" or "clear")
except:
	print("Nothing here")
